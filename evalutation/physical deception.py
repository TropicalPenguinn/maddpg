import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import scipy.stats as stats


def reward_plot(experiment):
    file = open('/home/airlab/PycharmProjects/maddpg2/experiments/' + experiment + '/agrewards.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    adv = [data[3*n] for n in range(int(len(data)/3))]
    ag = [data[3*n + 1] for n in range(int(len(data)/3))]
    x=np.arange(len(adv))
    plt.plot(x,ag,'b')
    plt.plot(x,adv,'r',linestyle='dashed')
    plt.legend(['agent','adversary'])

def success_helper_multi(thresholds, a, b):
    a_index = 0
    b_index = 0
    a_cum = 0
    b_cum = 0
    a_output = np.zeros(len(thresholds))
    b_output = np.zeros(len(thresholds))
    for i, t in enumerate(thresholds):
        while a_index < len(a) and a[a_index] < t**2:
            a_index += 1
            a_cum += 1
        while b_index < len(b) and b[b_index] < t**2:
            b_index += 1
            b_cum += 1
        a_output[i] = a_cum
        b_output[i] = b_cum
    return (a_output / len(a), b_output / len(b))

def success_rate(experiment):
    file = open('/home/airlab/PycharmProjects/maddpg2/experiments/' + experiment + '/benchmark.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    adversary = [e[0][-1][0] for e in data]
    agent = [min(e[0][-1][1][2], e[0][-1][2][2]) for e in data]
    adversary.sort()
    agent.sort()
    return agent,adversary


def success_helper(dd,e):
    return len([d for d in dd if d<e**2])*1.0/len(dd)

def success_helper_multi(thresholds, a, b):
    a_index=0
    b_index=0
    a_cum=0
    b_cum=0
    a_output=np.zeros(len(thresholds))
    b_output=np.zeros(len(thresholds))
    for i,t in enumerate(thresholds):
        while a_index<len(a) and a[a_index]<t**2:
            a_index+=1
            a_cum+=1
        while b_index<len(b) and b[b_index]<t**2:
            b_index+=1
            b_cum+=1
        a_output[i]=a_cum
        b_output[i]=b_cum
    return (a_output/len(a),b_output/len(b))

def success_plot(experiment):
    agent,adversary=success_rate(experiment)
    x=np.arange(0,1,.05)
    y,z=success_helper_multi(x,agent,adversary)
    plt.plot(x,y,'b')
    plt.plot(x,z,'r',linestyle='dashed')

def success_row(experiments,threshold):
    ag_data=[]
    adv_data=[]
    for e in experiments:
        ag,adv=success_rate(e)
        ag_data+=ag
        adv_data+=adv
    ag_data.sort()
    adv_data.sort()
    ag_succ=success_helper(ag_data,threshold)
    adv_succ=success_helper(adv_data,threshold)
    return [ag_succ,adv_succ,ag_succ-adv_succ]



def main():
    threshold=0.4
    result=pd.DataFrame([['maddpg', 'maddpg'] + success_row([

                                                      'simple_adversary_mm1',
                                                      'simple_adversary_mm2',
                                                      'simple_adversary_mm3',
                                                      'simple_adversary_mm4'], threshold),
                  ['maddpg', 'ddpg'] + success_row(['simple_adversary_md',
                                                    'simple_adversary_md1',
                                                    'simple_adversary_md2',
                                                    'simple_adversary_md3',
                                                    'simple_adversary_md4'], threshold),
                  ['ddpg', 'maddpg'] + success_row(['simple_adversary_dm',
                                                    'simple_adversary_dm1',
                                                    'simple_adversary_dm2',
                                                    'simple_adversary_dm3',
                                                    'simple_adversary_md4'], threshold),
                  ['ddpg', 'ddpg'] + success_row(['simple_adversary_dd',
                                                  'simple_adversary_dd1',
                                                  'simple_adversary_dd2',
                                                  'simple_adversary_dd3',
                                                  'simple_adversary_dd4'], threshold),
                  ],
                 columns=['Agent policy',
                          'Adversary policy',
                          'Agent success rate',
                          'Adversary success rate',
                          'Difference of rates'])

    print(result)
    result.to_csv("physical_deception.csv",index=False)

if __name__=="__main__":
    main()