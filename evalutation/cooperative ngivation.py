import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import scipy.stats as stats

def reward_plot(experiment):
    file = open('/home/airlab/PycharmProjects/maddpg2/experiments/' + experiment + '/agrewards.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    ag = [data[3*n] for n in range(int(len(data)/3))]
    x = np.arange(len(ag))
    plt.plot(x, ag, 'b')

def benchmark_data(benchmark):
    file = open('/home/airlab/PycharmProjects/maddpg2/experiments/' + benchmark, 'rb')
    data = pickle.load(file)
    file.close()
    # For each episode, average over frames of sum over landmarks of minimum over agents
    # of distance from agent to landmark.
    dist = [np.average([fr[0][2] for fr in ep[0]]) for ep in data]
    # For each episode, number of collisions
    coll = [np.sum([(ag[1] - 1)*1.0/2 for fr in ep[0] for ag in fr]) for ep in data]
    return (dist, coll)

def confidence_interval(a):
    return stats.norm.interval(0.95, loc=np.mean(a), scale=stats.sem(a))

def combine_benchmarks(benchmarks):
    dist = []
    coll = []
    for b in benchmarks:
        d, c = benchmark_data(b)
        dist += d
        coll += c
    return [np.average(dist), np.average(coll)]

def main():
    table2 = pd.DataFrame([['maddpg'] + combine_benchmarks(['simple_spread_3m0/benchmark.pkl',
                                                            'simple_spread_3m0/benchmark0.pkl',
                                                            'simple_spread_3m1/benchmark.pkl',
                                                            'simple_spread_3m2/benchmark.pkl',
                                                           ]),
                           ['ddpg'] + combine_benchmarks(['simple_spread_3d0/benchmark.pkl',
                                                          'simple_spread_3d1/benchmark.pkl',
                                                          'simple_spread_3d2/benchmark.pkl',
                                                         ]),
                          ],
                          columns=['Agent policy',
                                   'Average distance',
                                   'Number of collisions'
                                  ])

    print(table2)
    table2.to_csv('cooperative_ngivation.csv',index=False)

if __name__=="__main__":
    main()
