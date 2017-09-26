import numpy as np

def process(raw_inputs, irrelavent):
    raw_inputs = np.array(raw_inputs)
    mask = np.ones(len(raw_inputs), dtype=bool)
    mask[irrelavent] = False
    processed_input = raw_inputs[mask,...]

    return processed_input
