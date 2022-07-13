import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import scipy.stats as stats



def reward_plot(experiment):
    file = open('/home/airlab/PycharmProjects/maddpg2/experiments/simple_speaker_listener_' +experiment+ '/rewards.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    ag = [data[n] for n in range(int(len(data)))]
    x = np.arange(len(ag))
    plt.plot(x, ag, 'b')
    plt.show()


def benchmark_data(benchmark):
    file = open('/home/airlab/PycharmProjects/maddpg2/experiments/simple_speaker_listener_' + benchmark + '/benchmark.pkl',
                'rb')
    data = pickle.load(file)
    file.close()
    dist = [np.average([-fr[0] for fr in ep[0]]) for ep in data]
    return dist

def success_helper(dd,e=0.4):
    return len([d for d in dd if d<e**2])*1.0/len(dd)

def combine_benchmarks(benchmarks):
    dist=[]

    for b in benchmarks:
        d=benchmark_data(b)
        dist+=d

    return [success_helper(dist,0.5),np.average(dist)]


def main():
    table2 = pd.DataFrame([['maddpg'] + combine_benchmarks(['mm',
                                                            'mm1',
                                                            'mm2'
                                                            ])],

                          columns=['Agent',
                                   'Target reach %',
                                   'Average distance'
                                   ])
    print(table2)


if __name__=="__main__":
    main()



