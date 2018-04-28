#!/bin/bash

osc --host 127.0.0.1:9001 "/bassline/note_on" 0 60 127 2
osc --host 127.0.0.1:9001 "/filter/freq" 300
read -p "press a key to continue" k
sleep 3.0s
osc --host 127.0.0.1:9001 "/bassline/note_off" 0 60

read -p "press a key to continue" k
osc --host 127.0.0.1:9001 "/bassline/note_on" 0 60 127 2
osc --host 127.0.0.1:9001 "/solosynth/note_on" 1 60 127 2
sleep 3.0s
osc --host 127.0.0.1:9001 "/bassline/note_off" 0 60
osc --host 127.0.0.1:9001 "/solosynth/note_off" 1 60

read -p "press a key to continue" k
osc --host 127.0.0.1:9001 "/bassline/note_on" 0 64 127 2
osc --host 127.0.0.1:9001 "/solosynth/note_on" 1 64 127 2
sleep 3.0s
osc --host 127.0.0.1:9001 "/bassline/note_off" 0 64
osc --host 127.0.0.1:9001 "/solosynth/note_off" 1 64

read -p "press a key to continue" k
osc --host 127.0.0.1:9001 "/bassline/note_on" 0 64 127 2
osc --host 127.0.0.1:9001 "/solosynth/note_on" 1 64 127 2
osc --host 127.0.0.1:9001 "/drums/note_on" 2 64 127 2
sleep 3.0s
osc --host 127.0.0.1:9001 "/bassline/note_on" 0 64
osc --host 127.0.0.1:9001 "/solosynth/note_on" 1 64
osc --host 127.0.0.1:9001 "/drums/note_on" 2 64

#osc --host 127.0.0.1:9001 "/play"
