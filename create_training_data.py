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

i = 1
while True:
    if(i == 10001):
        break
    event = keyboard.read_key()
    if(event.event_type == 'up'):
        print(i)
        i += 1

        key = event.name
        if key == 'q':
            break

        raw_img = np.array(sct.grab(const.MONITOR))
        raw_img = raw_img[:, :, 0:3]

        new_output = [0, 0, 0, 0, 0]
        if key == 'd':
            new_output[const.IDX_NOTHING] = 1
        elif key == 'up': 
            new_output[const.IDX_FORWARD] = 1
        elif key == 'down': 
            new_output[const.IDX_BACKWARD] = 1
        elif key == 'right': 
            new_output[const.IDX_RIGHT] = 1
        elif key == 'left': 
            new_output[const.IDX_LEFT] = 1

        _, _, new_input = process_image.process(raw_img)
        training_inputs.append(new_input)
        training_outputs.append(new_output)

print(len(training_inputs), len(training_outputs))
# pickle.dump(training_inputs, open(const.TRAINING_INPUT, "wb"))
# pickle.dump(training_outputs, open(const.TRAINING_OUTPUT, "wb"))
