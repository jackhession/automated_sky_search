from pyskyqremote.skyq_remote import SkyQRemote
import time

remote = SkyQRemote(input("Sky Q Box IP addr: "))

remote.press("dismiss")
remote.press("search")

keys = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    ' ', '0','9','8','7','6','5','4','3','2','1'
]

key_map = {k: i for i, k in enumerate(keys)}
current_index = 0


def move_and_select(target_char):
    global current_index
    
    target_index = key_map[target_char]
    length = len(keys)
    
    down = (target_index - current_index) % length
    up = (current_index - target_index) % length
    
    if down <= up:
        direction = "down"
        steps = down
    else:
        direction = "up"
        steps = up
    
    for _ in range(steps):
        remote.press(direction)
        time.sleep(0.5)  # small delay so Sky Q keeps up
    
    remote.press("select")
    current_index = target_index


def type_text(text):
    for char in text.upper():
        if char in key_map:
            move_and_select(char)
            print(char)
            time.sleep(1)


# Example usage
type_text(input("Search: "))