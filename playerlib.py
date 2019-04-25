#!/usr/bin/env python3
# on chromebook run this: apt-get install pulseaudio; pulseaudio --start

def play(file,debug):
    import sunvox.api
    import logging
    import types
    import functools
    import os
    import sys
    from pythonosc import dispatcher
    from pythonosc import osc_server

    # trick for py2/3 compatibility
    if 'basestring' not in globals():
       basestring = str
    ENCODING = 'utf-8'
    open("mappings.txt","w").close() # empty mapping file
    log = logging.getLogger(__name__)
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    _ = types.SimpleNamespace( obj=types.SimpleNamespace, partial=functools.partial )

    #os.environ.set('SUNVOX_DLL_BASE', os.path.dirname(__file__)+'/sunvox/lib')
    flags = (
        sunvox.api.SV_INIT_FLAG.ONE_THREAD
    #    sunvox.api.SV_INIT_FLAG.USER_AUDIO_CALLBACK
    )
    sunvox.api.init(None, 44100, 2, (False) )
    slot = sunvox.api.Slot()
    slot.load_filename(file.encode('utf8'))
    module_count = slot.get_number_of_modules()
    print('{} audio-modules loaded'.format(module_count))


    #
    # OSC mappings
    #
    # see https://pypi.python.org/pypi/python-osc
    #
    dispatcher = dispatcher.Dispatcher()

    def mapOSC(addr,cb,id,info=""):
        print('initing OSC parameter: /{}'.format(id).ljust(60) + '{}'.format(info))
        mappings = open("mappings.txt","a+")
        mappings.write(str(addr) + "\t" + str(info) + "\n")
        mappings.close()
        dispatcher.map(addr,cb,id)

    def play(unused_addr, args):
        slot.play_from_beginning()

    def note_on(sv,module_index,addr,args,channel=0,note=60,velocity=120,glide=2):
        log.debug("incoming: {}: {} {} {}".format(addr,note,velocity,glide))
        #if isinstance(note, basestring):
        #    note = getattr(sv.NOTECMD, note), 
        ctl = 0 
        ctlvalue = 0
        slot.send_event(channel, note, velocity, module_index, ctl, ctlvalue)


    def note_off(sv,module_index,addr,args,channel=0,note=60):
        log.debug("note_off")
        ctl = 0 
        ctlvalue = 0
        slot.send_event(channel, sv.NOTECMD.NOTE_OFF, 0, module_index, ctl,ctlvalue )

    def ctl(sv,module_index,ctlnum,addr,args,value=0):
        log.debug("incoming ctl: {}: {} {} mod:{}".format(addr,ctlnum,value,module_index))
        slot.send_event(0, 0, 0, module_index, ctlnum, value)

    def sanitizeString(str):
        return str.lower().replace(" ","_").replace("(","").replace(")","")

    mapOSC("/play", play, "play")
    spacemodules = False
    for i in range(module_count):
        modulename = slot.get_module_name(i).decode(ENCODING)
        if modulename.endswith(' '):
            spacemodules = True


    for i in range(module_count):
        nctrls = slot.get_number_of_module_ctls(i)
        modulename = slot.get_module_name(i).decode(ENCODING)
        if not len(modulename):
            continue
        if spacemodules and not modulename.endswith(' '):
            continue
        log.debug('module {}: {}'.format(i,modulename))
        id_on  = sanitizeString('{}/note_on'.format(modulename))
        id_off = sanitizeString('{}/note_off'.format(modulename))
        osc_note_on  = _.partial( note_on,  sunvox.api,1+i )
        osc_note_off = _.partial( note_off, sunvox.api,1+i )
        mapOSC('/{}'.format(id_on), osc_note_on, id_on,"[channel=0..64] [note=1..127] [velocity=127] [glide=2]")
        mapOSC('/{}'.format(id_off), osc_note_off, id_off,"[channel=0..64] [note=1..127]")
        for j in range(nctrls):
            id_ctl = sanitizeString( '{}/{}'.format(modulename,slot.get_module_ctl_name(i,j).decode(ENCODING)) )
            osc_ctl  = _.partial( ctl, sunvox.api, 1+i, (1+j) << 8 )
            mapOSC('/{}'.format(id_ctl), osc_ctl, id_ctl,"[value=0..37565]")

    print("special notenumbers:")
    print("    0   = EMPTY BUFFER")
    print("    128 = NOTE_OFF")
    print("  * 129 = ALL_NOTES_OFF")
    print("  * 130 = CLEAN_SYNTHS")
    print("  * 131 = STOP")
    print("  * 132 = PLAY")
    print("  * 133 = SET_PITCH")
    print("  * 134 = PREV_TRACK")
    print("          ")
    print("      * = only applicable when module is a pattern/recursive")
    print("")
    print("wrote mappings.txt")

    server = osc_server.ThreadingOSCUDPServer( ("0.0.0.0",9001), dispatcher)
    print("Serving OSC on {}".format(server.server_address))
    server.serve_forever()

    print('Press Enter to stop playback')
    input()
    slot.stop()
    sunvox.api.deinit()
