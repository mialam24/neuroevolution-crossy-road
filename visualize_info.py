import neat
import visualize
import pickle

import constants_crossy_road as const

def visualize_info(config_file, num = 0):
    # Load configuation
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # NAMES
    node_names = {const.IDX_NOTHING:'NO MOVE', 
                  const.IDX_FORWARD: 'FORWARD',
                  const.IDX_BACKWARD: 'BACKWARD',
                  const.IDX_LEFT: 'LEFT',
                  const.IDX_RIGHT: 'RIGHT'}

    with open('stats.pkl', 'rb') as s:
        stats = pickle.load(s)
    with open('winner-' + str(num) + '.pkl', 'rb') as w:
        winner = pickle.load(w)

    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

if __name__ == '__main__':
    num = 217
    config_file = 'neat-config'
    visualize_info(config_file, num)
