# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:16:21 2019

@author: HP
"""

import pandas as pd
import numpy as  np
from statistics import mean
import statistics
from collections import Counter

for no in range(1,55):
 input_file = "/home/luciffer/Downloads/user_data/user"
 if no < 10 :
    input_file += ("0" + str(no))
 else :
    input_file += str(no)
 output_file  = input_file + "/user" + str(no) + ".txt"
 fttp = input_file + "/user" + str(no) + "_t.txt"
 fsp =  input_file + "/user" + str(no) + "_s.txt"
 fcp =  input_file + "/user" + str(no) + "_c.txt"
 input_file += ("/user" + str(no) + "_output.txt")
 data = pd.read_csv(output_file, sep=",", header=None)
 feat = pd.read_csv(input_file, sep=" ", header=None)
 data.columns = ["a", "b", "c", "d", "e", "f","g","h", "i"]
 data['c'] = pd.to_datetime(data['c'])
 data['h'] = np.log(1+data['h'])
 feat.columns = ["i","t","p"]
 L = list(feat['t'])
 ind = list(feat['i'])
 lphi = list(feat['p'])
 for i in range(len(L)):
     if L[i] == 'T':
         ft = open(fttp,"a+")
         ts = data.loc[data['a'] == ind[i]]['c']
         itd = []
         for j in range(len(ts.index) - 1) :
             itd.append((ts.iloc[j+1] - ts.iloc[j]).total_seconds())
         msi = mean(itd)
         rmsi = 0; 
         c1 = min(itd)
         c2 = max(itd)
         class1 = []
         class2 = []
         for _ in range(100):
             class1.clear()
             class2.clear()
             for j in range(len(itd)):
                 dis_c1 = abs(itd[j] - c1)
                 dis_c2 = abs(itd[j] - c2)
                 if dis_c1 < dis_c2 :
                    class1.append(itd[j])
                 else :
                    class2.append(itd[j])
             if len(class1)!=0 :
                c1 = mean(class1)
             if len(class2)!=0 :
                c2 = mean(class2)
         itd.sort()
         if len(class1) > len(class2) :
            if c1 < c2 :
               rmsi = mean(itd[0:(8*len(itd))//10])
            else :
               rmsi = mean(itd[(2*len(itd))//10:])
         else :
            if c2 < c1 :
               rmsi = mean(itd[0:(8*len(itd))//10])
            else :
               rmsi = mean(itd[(2*len(itd))//10:])
         kc = len((data.loc[data['a'] == ind[i]]['d']).index)
         spl = len((data.loc[(data['a'] == ind[i]) & (data['d'] == -5)]['d']).index)
         bck = len((data.loc[(data['a']==ind[i])&(data['d'] == -2)]).index)
         
         splch = spl/kc
         bckch = bck/kc
         ssd = (ts.iloc[len(ts.index)-1] - ts.iloc[0]).total_seconds()
         label = data.loc[data['a']==ind[i]].iloc[0,4]
         if label != -99 :
            print(msi,rmsi,splch,bckch,ssd,label,file = ft)
         ft.close()
 
 
     elif L[i] == 'S':
         fs = open(fsp,"a+")
         ps = data.loc[data['a'] == ind[i]]['g']
         ts = data.loc[data['a'] == ind[i]]['c']
         ps = list(ps)
         coun = Counter(ps)
         mps = mean(ps)
         modeps = coun.most_common(1)[0][0]
         stdps = 0;
         if len(ps) == 1:
            stdps = 0.0
         else :
            stdps = statistics.stdev(ps)
         swypeper = 1.0
         ssd = (ts.iloc[len(ts.index)-1] - ts.iloc[0]).total_seconds()
         label = data.loc[data['a']==ind[i]].iloc[0,4]
         if label != -99 :
            print(mps,stdps,modeps,swypeper,ssd,label,file = fs)
         fs.close()
     else :
         fc = open(fcp,"a+")
         ss = data.loc[(data['a']==ind[i])&(data['h'] > lphi[i])]
         st = data.loc[(data['a']==ind[i])&(data['h'] <= lphi[i])]
         ps = list(ss['g'])
         coun = Counter(ps)
         mps = mean(ps)
         modeps = coun.most_common(1)[0][0]
         stdps = 0
         if len(ps) == 1:
            stdps = 0.0
         else :
            stdps = statistics.stdev(ps)
         swypeper = len(ss.index)/(len(ss.index)+len(st.index))
         itd = []
         for j in range(len(st.index) - 1) :
             itd.append((st.iloc[j+1,2]-st.iloc[j,2]).total_seconds())
         msi = mean(itd)
         rmsi = 0
         c1 = min(itd)
         c2 = max(itd)
         cs1 = []
         cs2 = []
         for _ in range(100):
             cs1.clear()
             cs2.clear()
             for j in range(len(itd)):
                 dis_c1 = abs(itd[j] - c1)
                 dis_c2 = abs(itd[j] - c2)
                 if dis_c1 < dis_c2 :
                    cs1.append(itd[j])
                 else :
                    cs2.append(itd[j])
             if len(cs1)!=0 :
                c1 = mean(cs1)
             if len(cs2)!=0 :
                c2 = mean(cs2)
         itd.sort()
         if len(cs1) > len(cs2) :
            if c1 < c2 :
               rmsi = mean(itd[0:(8*len(itd))//10])
            else :
               rmsi = mean(itd[(2*len(itd))//10:])
         else :
            if c2 < c1 :
               rmsi = mean(itd[0:(8*len(itd))//10])
            else :
               rmsi = mean(itd[(2*len(itd))//10:])
         
         splch = len((st.loc[st['d'] == -5]).index)/len(st.index)
         bckch = len((st.loc[st['d']==-2]).index)/len(st.index)
         ssd =(st.iloc[len(st.index)-1,2] - st.iloc[0,2]).total_seconds()
         ssd += (ss.iloc[len(ss.index)-1,2] - ss.iloc[0,2]).total_seconds()
         label = data.loc[data['a']==ind[i]].iloc[0,4]
         if label != -99 :
            print(msi,rmsi,splch,bckch,mps,stdps,modeps,swypeper,ssd,label,file = fc)
         fc.close()
 print("done" + str(no))
