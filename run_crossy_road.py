import time
import numpy as np
import cv2
import mss

import neat

import constants_crossy_road as const
import movement_crossy_road as move
import process_image_crossy_road as process_image
import score_crossy_road as score

sct = mss.mss()
gen_num = 0
individual_num = 0

def setup():
    while(True):
        last_time = time.time()
    
        raw_img = np.array(sct.grab(const.MONITOR))
        raw_img = raw_img[:, :, 0:3]
        _, processed_img, _ = process_image.process(raw_img)
        processed_img = cv2.copyMakeBorder(processed_img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        
        cv2.imshow('Processed Image', processed_img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)

def cross_the_road(genome_id, net):
    global gen_num
    global individual_num
    time.sleep(3)
    move.restart()

    while(True):
        last_time = time.time()
    
        raw_img = np.array(sct.grab(const.MONITOR))
        raw_img = raw_img[:, :, 0:3]

        game_status, processed_img, network_input = process_image.process(raw_img)
        processed_img = cv2.copyMakeBorder(processed_img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        cv2.rectangle(processed_img, 
                (0, 493 - 16), (193, 493 - 16 - 25), 
                [255, 255, 255], -1)
        cv2.rectangle(processed_img, 
                (0,493 + 5), (449, 493 - 16), 
                [255, 255, 255], -1)
        cv2.putText(processed_img,
                "Generation: " + str(gen_num), 
                (10,493 - 21), cv2.FONT_HERSHEY_COMPLEX_SMALL, 
                1, [0, 0, 0], 2)
        cv2.putText(processed_img,
                "Individual: " + str(individual_num) + 
                " Genome ID: " + str(genome_id), 
                (10,493), cv2.FONT_HERSHEY_COMPLEX_SMALL, 
                1, [0, 0, 0], 2)
        cv2.imshow('Processed Image', processed_img)
        # Press "q" to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            quit()

        if(game_status == const.GAME_STATUS_GREAT_SCORE):
            move.escape()
        if(game_status != const.GAME_STATUS_PLAYING):
            break
        
        network_output = net.activate(network_input)
        index = network_output.index(max(network_output))
        
        if(index == const.IDX_FORWARD):
            move.forward()
        elif(index == const.IDX_BACKWARD):
            move.backward()
        elif(index == const.IDX_LEFT):
            move.left()
        elif(index == const.IDX_RIGHT):
            move.right()
        else:
            pass

    return score.get_score()

def eval_genomes(genomes, config):
    global individual_num
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = cross_the_road(genome_id, net)
        individual_num += 1

def run(config_file, num):
    global gen_num
    global individual_num

    # Load configuation
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-' + str(num))

    for i in range(const.NUM_GENERATIONS):
        p.run(eval_genomes, 1)

        gen_num += 1
        individual_num = 0

if __name__ == '__main__':
    num = 209
    config_file = 'neat-config'
    setup()
    run(config_file, num)
