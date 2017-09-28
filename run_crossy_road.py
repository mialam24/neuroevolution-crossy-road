import time
import numpy as np
import cv2
from scipy import misc
import mss
import pickle

import os
import neat
import visualize

import constants_crossy_road as const
import movement_crossy_road as move
import process_image_crossy_road as process_image
import score_crossy_road as score

sct = mss.mss()
gen_num = 0

def setup():
    while(True):
        last_time = time.time()
    
        raw_img = np.array(sct.grab(const.MONITOR))
        raw_img = raw_img[:, :, 0:3]
        _, processed_img, _ = process_image.process(raw_img)
        
        cv2.imshow('Processed Image', processed_img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)

def cross_the_road(genome_id, net):
    global gen_num
    time.sleep(3)
    move.restart()

    while(True):
        last_time = time.time()
    
        raw_img = np.array(sct.grab(const.MONITOR))
        raw_img = raw_img[:, :, 0:3]

        game_status, processed_img, network_input = process_image.process(raw_img)
        cv2.rectangle(processed_img, 
                (0,493), (441, 493 - 25), 
                [255, 255, 255], -1)
        cv2.putText(processed_img,
                "Generation: " + str(gen_num) + 
                " Genome ID: " + str(genome_id), 
                (5,493 - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 
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
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = cross_the_road(genome_id, net)

def run(config_file):
    global gen_num

    # Load configuation
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    for i in range(const.NUM_GENERATIONS):
        # Run for 1 generation at a time.
        winner = p.run(eval_genomes, 1)

        # Save winner and stats
        with open('winner-' + str(i), 'wb') as f:
            pickle.dump(winner, f)

        with open('stats-' + str(i), 'wb') as f:
            pickle.dump(stats, f)

        gen_num += 1

def visualize_info(config_path, num = 0):
    # checkpoint_name = "neat-checkpoint-" + str(num)
    # p = neat.Checkpointer.restore_checkpoint(checkpoint_name)

    # Load configuation
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    # NAMES
    node_names = {const.IDX_NOTHING:'NO MOVE', 
                  const.IDX_FORWARD: 'FORWARD',
                  const.IDX_BACKWARD: 'BACKWARD',
                  const.IDX_LEFT: 'LEFT',
                  const.IDX_RIGHT: 'RIGHT'}

    with open('trial-0/stats-' + str(num), 'rb') as s:
        stats = pickle.load(s)
    with open('trial-0/winner-' + str(num), 'rb') as w:
        winner = pickle.load(w)

    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

if __name__ == '__main__':
    local_dir = os.getcwd()
    # config_path = os.path.join(local_dir, 'neat-config')
    # setup()
    # run(config_path)
    config_path = os.path.join(local_dir, 'trial-0/neat-config')
    visualize_info(config_path, 4)
