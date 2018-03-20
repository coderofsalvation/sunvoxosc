#!/bin/bash

osc --host 127.0.0.1:9001 "/note_on/bassline" 0 60 127 2
sleep 3.0s
osc --host 127.0.0.1:9001 "/note_off/bassline" 0 60

read -p "press a key to continue" k
osc --host 127.0.0.1:9001 "/note_on/bassline" 0 60 127 2
osc --host 127.0.0.1:9001 "/note_on/solosynth" 1 60 127 2
sleep 3.0s
osc --host 127.0.0.1:9001 "/note_off/bassline" 0 60
osc --host 127.0.0.1:9001 "/note_off/solosynth" 1 60

read -p "press a key to continue" k
osc --host 127.0.0.1:9001 "/note_on/bassline" 0 64 127 2
osc --host 127.0.0.1:9001 "/note_on/solosynth" 1 64 127 2
sleep 3.0s
osc --host 127.0.0.1:9001 "/note_off/bassline" 0 64
osc --host 127.0.0.1:9001 "/note_off/solosynth" 1 64

read -p "press a key to continue" k
osc --host 127.0.0.1:9001 "/note_on/bassline" 0 64 127 2
osc --host 127.0.0.1:9001 "/note_on/solosynth" 1 64 127 2
osc --host 127.0.0.1:9001 "/note_on/drums" 2 64 127 2
sleep 3.0s
osc --host 127.0.0.1:9001 "/note_off/bassline" 0 64
osc --host 127.0.0.1:9001 "/note_off/solosynth" 1 64
osc --host 127.0.0.1:9001 "/note_off/drums" 2 64

#osc --host 127.0.0.1:9001 "/play"
