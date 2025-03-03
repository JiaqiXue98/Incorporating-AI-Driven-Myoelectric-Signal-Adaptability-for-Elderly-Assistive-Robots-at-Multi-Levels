
import pandas as pd 
import numpy as np
import os


    


def read_data(data_path, split = "train"):
    """ Read data """

    # Fixed params
    n_channels=4
    n_class = 2
    n_steps =500 #64
    overlap= 495



    rawdata=np.loadtxt(data_path)
    array=rawdata
    print('array.shape',array.shape)


    num=((len(array)-n_steps)//(n_steps-overlap))+1
    print(num)

    labels_h=np.zeros((num,1))
    labels_e=np.zeros((num,1))

      
    for i in range(num):
        labels_h[i][0] =array[n_steps-1+i*(n_steps-overlap)][n_channels]
        labels_e[i][0] =array[n_steps-1+i*(n_steps-overlap)][n_channels+1]
   
 

    X = np.zeros((len(labels_h), n_steps, n_channels))#three dimensional array  len(labels)

    for j in range(num):

        start=j*n_steps-j*overlap
        X[j,...] = array[start:start+n_steps,0:n_channels] #error

    return X, labels_h, labels_e

