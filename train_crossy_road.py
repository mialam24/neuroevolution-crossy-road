import neat
import pickle

import constants_crossy_road as const

training_input = []
training_output = []

def load_training_data():
    global training_input, training_output
    training_input = pickle.load( open( const.TRAINING_INPUT, "rb" ) )
    training_output = pickle.load( open( const.TRAINING_OUTPUT, "rb" ) )

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 50.0
        net = neat.nn.RecurrentNetwork.create(genome, config)
        for i in range(len(training_input)):
            output = net.activate(training_input[i])
            for j in range(len(output)):
                fitness_less = (output[j] - training_output[i][j]) ** 2
                genome.fitness -= fitness_less * 0.001

def run(config_file):
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
    p.add_reporter(neat.Checkpointer(10))

    for gen_num in range(const.NUM_GENERATIONS):
        winner = p.run(eval_genomes, 1)

        # Save winner and stats
        with open('winner-' + str(gen_num) + '.pkl', 'wb') as f:
            pickle.dump(winner, f)

        with open('stats.pkl', 'wb') as f:
            pickle.dump(stats, f)

if __name__ == '__main__':
    config_file = 'neat-config'

    load_training_data()
    run(config_file)
