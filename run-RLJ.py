from algorithm import Algorithm
from analysis import Analysis


if __name__ == '__main__':

    tool = Analysis('results_algorithm/')
    name = 'RLJ'
    algorithm = Algorithm(name, param=5)
    runtime = algorithm.execute(network_path='networks/',
                                sub_filename='sub-ts.txt',
                                req_num=1000)
    tool.save_evaluations(algorithm.evaluation, '%s-ts-2.txt' % name)
    print(runtime)
# ts
# wm
