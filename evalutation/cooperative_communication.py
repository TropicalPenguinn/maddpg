import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import scipy.stats as stats
import seaborn as sns


def reward_plot(experiments):
    reward_lst=[]
    for experiment in experiments:
        file = open('/home/airlab/PycharmProjects/maddpg2/experiments/simple_speaker_listener_' +experiment+ '/agrewards.pkl', 'rb')
        data = pickle.load(file)
        file.close()
        ag = [data[2*n] for n in range(int(len(data)/2))]
        reward_lst.append(ag)

    x = np.arange(len(reward_lst[0]))

    csv_algo_list = list()
    csv_inter_list = list()
    csv_reward_list = list()

    for i in range(3):
        name=["maddpg" for _ in range(len(reward_lst[0]))]
        csv_algo_list.extend(name)
        csv_inter_list.extend(x)
        csv_reward_list.extend(reward_lst[i])

    my_df = pd.DataFrame({"Model": csv_algo_list, "episodes": csv_inter_list, "mean reward": csv_reward_list})
    sns.lineplot(x="episodes", y="mean reward", hue="Model", data=my_df)
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
    plt.title("maddpg vs. maddpg")
    reward_plot(['mm','mm1','mm2'])

    table2 = pd.DataFrame([['maddpg'] + combine_benchmarks(['mm',
                                                            'mm1',
                                                            'mm2'
                                                            ])],

                          columns=['Agent',
                                   'Target reach %',
                                   'Average distance'
                                   ])
    print(table2)
    table2.to_csv('cooperative_communication.csv',index=False)

if __name__=="__main__":
    main()




