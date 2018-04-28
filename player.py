#!/usr/bin/env python3
# on chromebook run this: apt-get install pulseaudio; pulseaudio --start
import sys
import os
os.path.join(os.path.dirname(__file__))
import playerlib

if len(sys.argv) == 1:
    print ('Usage: ./player.py <file.sunvox>')
    sys.exit(0)

file = sys.argv[1]
debug = False

playerlib.play(file,debug)
