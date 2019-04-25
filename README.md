## Usage

```
python3 player.py test.sunvox
```

## Select only Spacemodules

Sometimes there are zillions of modules in a .sunvox-file, which don't need to be exposed to OSC.
Therefore, you can 'select' module-exposure by adding a space (' ') to a module's title in sunvox (so 'Metamodule ' instead of 'Metamodule').

## Debugging info

uncomment this in player.py

```
logging.basicConfig(level=logging.DEBUG)
```
