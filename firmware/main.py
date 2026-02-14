# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Keymap:
# 1️⃣ Copy       = Cmd + C
# 2️⃣ Paste      = Cmd + V
# 3️⃣ Play/Pause = KC.MPLY
# 4️⃣ Skip Track = KC.MNXT
keyboard.keymap = [
    [
        KC.Macro(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  # Copy
        KC.Macro(Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)),  # Paste
        KC.MPLY,                                                # Play/Pause
        KC.MNXT,                                                # Skip
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
