import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import scipy.stats as stats
import os

def touch_count(experiment):
    file = open(experiment + '/benchmark.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    data = [np.sum([np.sum(fr) for fr in ep[0]]) for ep in data]
    return data


def touch_row(experiments):

    touch_result=[]
    for e in experiments:
        data=touch_count(e)
        touch_result+=data

    result=sum(touch_result)/len(touch_result)
    return [result]



def main():
    result=pd.DataFrame([['maddpg', 'maddpg'] + touch_row(['/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_mm',
                                                           '/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_mm1',
                                                           '/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_mm2',


                                                    ]),
                  ['maddpg', 'ddpg'] + touch_row(['/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_md',
                                                    '/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_md1',
                                                    '/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_md2']),
                  ['ddpg', 'maddpg'] + touch_row(['/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_dm',
                                                    '/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_dm1',
                                                    '/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_dm2']),
                  ['ddpg', 'ddpg'] + touch_row(['/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_dd',
                                                  '/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_dd1',
                                                  '/home/airlab/PycharmProjects/maddpg2/experiments/simple_tag_dd2']),
                 ],
                 columns=['Agent policy',
                          'Adversary policy',
                          'touches'])

    print(result)
    result.to_csv("simple_tag.sv",index=False)

if __name__=="__main__":

    main()