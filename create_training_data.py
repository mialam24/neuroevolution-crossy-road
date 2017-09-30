import keyboard 
import mss
import numpy as np
import pickle

import constants_crossy_road as const
import process_image_crossy_road as process_image

training_inputs = []
training_outputs = []

sct = mss.mss()

while True:
    event = keyboard.read_key()
    if(event.event_type == 'up'):
        key = event.name
        if key == 'up':
            break

cnt_nothing = -1
cnt_up = -1
cnt_down = -1
cnt_left = -1
cnt_right = -1
ignore_nothing = False
ignore_up = False
ignore_down = False
ignore_left = False
ignore_right = False
while True:
    total = cnt_nothing + cnt_up + cnt_down + cnt_left + cnt_right
    if(total > 10000):
        break

    print("U", cnt_up, "D", cnt_down, 
            "R", cnt_right, "L", cnt_left, "N", cnt_nothing)
    event = keyboard.read_key()
    if(event.event_type == 'up'):
        key = event.name
        if key == 'q':
            break

        raw_img = np.array(sct.grab(const.MONITOR))
        raw_img = raw_img[:, :, 0:3]

        new_output = [0, 0, 0, 0, 0]
        if key == 'd':
            if ignore_nothing: continue
            new_output[const.IDX_NOTHING] = 1
            cnt_nothing += 1
        elif key == 'up': 
            if ignore_up: continue
            new_output[const.IDX_FORWARD] = 1
            cnt_up += 1
        elif key == 'down': 
            if ignore_down: continue
            new_output[const.IDX_BACKWARD] = 1
            cnt_down += 1
        elif key == 'right': 
            if ignore_right: continue
            new_output[const.IDX_RIGHT] = 1
            cnt_right += 1
        elif key == 'left': 
            if ignore_left: continue
            new_output[const.IDX_LEFT] = 1
            cnt_left += 1
        elif key == 'f':
            last_elem = training_outputs.pop()
            training_inputs = training_inputs[:-1]
            if(last_elem[const.IDX_NOTHING] == 1):
                cnt_nothing -= 1
            elif(last_elem[const.IDX_FORWARD] == 1):
                cnt_up -= 1
            elif(last_elem[const.IDX_RIGHT] == 1):
                cnt_right -= 1
            elif(last_elem[const.IDX_LEFT] == 1):
                cnt_left -= 1
            elif(last_elem[const.IDX_BACKWARD] == 1):
                cnt_down -= 1
            continue
        elif key == 'g':
            ignore_up = not ignore_up
            continue
        elif key == 'h':
            ignore_down = not ignore_down
            continue
        elif key == 'j':
            ignore_left = not ignore_left
            continue
        elif key == 'k':
            ignore_right = not ignore_right
            continue
        elif key == 'l':
            ignore_nothing = not ignore_nothing
            continue

        _, _, new_input = process_image.process(raw_img)
        training_inputs.append(new_input)
        training_outputs.append(new_output)

print(len(training_inputs), len(training_outputs))
pickle.dump(training_inputs, open(const.TRAINING_INPUT, "wb"))
pickle.dump(training_outputs, open(const.TRAINING_OUTPUT, "wb"))
