import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import scipy.stats as stats

def reward_plot(experiment):
    file = open('/home/airlab/PycharmProjects/maddpg2/experiments/' + experiment + '/rewards.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    a = [data[3*n] for n in range(int(len(data)/3))]
    b = [data[3 * n+1] for n in range(int(len(data) / 3))]
    c = [data[3 * n+2] for n in range(int(len(data) / 3))]
    x=np.arange(len(a))
    plt.plot(x,a,'r',linestyle='dashed')
    plt.plot(x,b,'b')
    plt.plot(x,c,'g')
    plt.legend(['adversary','listener','speaker'])
    plt.show()



def success_rate(experiment):
    file = open('/home/airlab/PycharmProjects/maddpg2/experiments/' + experiment + '/benchmark.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    adversary=[e[0][-1][0] for e in data]
    listener=[e[0][-1][1] for e in data]
    speaker=[e[0][-1][2] for e in data]

    success_adversary=[True if np.argmax(fr[0])==np.argmax(fr[1]) else False for fr in adversary]
    success_listener = [True if np.argmax(fr[0]) == np.argmax(fr[1]) else False for fr in listener]


    return success_adversary,success_listener

def success_row(experiments):
    ag_data=[]
    adv_data=[]
    for e in experiments:
        adv,ag=success_rate(e)
        ag_data+=ag
        adv_data+=adv

    ag_success=sum(ag_data)/len(ag_data)
    adv_success=sum(adv_data)/len(adv_data)
    return [ag_success,adv_success,ag_success-adv_success]


def main():
    result=pd.DataFrame([['maddpg', 'maddpg'] + success_row(['simple_crypto_mm',
                                                  'simple_crypto_mm1',
                                                  'simple_crypto_mm2']),
              ['maddpg', 'ddpg'] + success_row(['simple_crypto_md',
                                                'simple_crypto_md1',
                                                'simple_crypto_md2']),
              ['ddpg', 'maddpg'] + success_row(['simple_crypto_dm']),
              ['ddpg', 'ddpg'] + success_row(['simple_crypto_dd',
                                              'simple_crypto_dd1',
                                              'simple_crypto_dd2']),
             ],
             columns=['Alice,Bob',
                      'Eve',
                      'Bob succ ',
                      'Eve succ ',
                      'Difference succ '])

    print(result)

if __name__=="__main__":
    main()