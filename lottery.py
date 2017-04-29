# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:39:50 2017

@author: andychoi
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from sklearn.neural_network import MLPClassifier

class Lottery:
    def __init__(self,datatxt):
        self.datatxt = datatxt
        
    
    def MLL(self,tw) :
        datatxt = self.datatxt
        self.tw = tw
        row = datatxt.shape[0]
        col = datatxt.shape[1]
        lottery_num = 45
        k = np.zeros((row,lottery_num))
        for i in range(row):
            for j in range(col):
                for t in range(lottery_num):
                    if datatxt[i][j] == t+1 :
                            k[i][t] = k[i][t]+1
        
        k = k[1:]    
         
        clf = MLPClassifier(solver='lbfgs', 
                            alpha=1e-5,
                            
                             hidden_layer_sizes=(15,),
                            random_state=1)
        
        learn =np.array([np.zeros((lottery_num))])
        sol = np.array([np.zeros((lottery_num))])
        pk = np.zeros((lottery_num))
        
        test_num = row - 30 - tw
        self.test_num = test_num
        
        for i in range(test_num):
            pk = np.zeros((lottery_num))
            for j in range(tw):
                pk = pk+k[i+j]
            pk = pk/pk.sum()
            learn = np.append(learn, [pk], axis =0)
            sol = np.append(sol, [k[i+tw]], axis =0)
            
        clf.fit(learn[1:].tolist() , sol[1:].tolist())
        self.clf = clf
        self.k = k
    
    ######### test ##########
    def Test(self):
        test = np.zeros((45))
        
        test_order = self.test_num + self.tw
        k = self.k
        clf = self.clf
        tw = self.tw
        
        sig_auc = 0
        cnt = 0
        for test_num in range(test_order,k.shape[0]-tw):
            for i in range(tw):
                test = test+k[test_num+i]
            test = test/test.sum()
            output = clf.predict([test])
            output = np.transpose([test])
            
            from sklearn.metrics import roc_curve, auc
            
            output2 = k[test_num+tw]
            output3 = np.transpose(output)[0]
            fpr, tpr , _ = roc_curve(output2, output3)
            roc_auc = auc(fpr, tpr)
            
            cnt = cnt+1
        
            sig_auc = sig_auc+roc_auc

        print(sig_auc/cnt)
    
    def returnLotterynum(self):
        clf = self.clf
        tw = self.tw
        k = self.k
        test = np.zeros((45))
        
        for i in range(k.shape[0]-tw, k.shape[0]):
            test = test+k[i]
        prob = clf.predict([test])
        prob*1000
        
        sampler = np.array([])
        for i in range(45):
            for j in range(int(prob[0][i])):
                sampler = np.append(sampler,i)
            for basis in range(10):
                sampler = np.append(sampler,i)
        
        
        np.random.shuffle(sampler)
        freq = np.zeros((45))
        for i in sampler[0:100]:
            for j in range(45):
                if i == j:
                    freq[j] = freq[j]+1
        
        lotter_subs = np.array(range(1,46))
        
        for i in range(45):
            for j in range(i,45):
                if (freq[j]>freq[i]):
                    temp_f = freq[i]
                    freq[i] = freq[j]
                    freq[j] =temp_f
                    
                    temp = lotter_subs[i]
                    lotter_subs[i] = lotter_subs[j]
                    lotter_subs[j] = temp
                    

        lotter_num = np.array(range(1,46))
        
        for i in range(45):
            for j in range(i,45):
                if (prob[0][j]>prob[0][i]):
                    temp_f = prob[0][i]
                    prob[0][i] = prob[0][j]
                    prob[0][j] = temp_f
                    
                    temp = lotter_num[i]
                    lotter_num[i] = lotter_num[j]
                    lotter_num[j] = temp
                    
                              
        self.lotter_num = lotter_num
        lotter_first = lotter_num[0:10]
        lotter_scnd = lotter_num[10:20]
        lotter_trd = lotter_num[20:30]
        lotter_4nd = lotter_num[30:]
        
        np.random.shuffle(lotter_first)
        np.random.shuffle(lotter_scnd)
        np.random.shuffle(lotter_trd)
        np.random.shuffle(lotter_4nd)
        select = np.array([])
        select = np.append(select, lotter_first[0:3])
        select = np.append(select,
        lotter_scnd[0:2])
        select = np.append(select, lotter_trd[0])
        select = np.append(select,
        lotter_4nd[0])
        return select, lotter_subs[0:7]