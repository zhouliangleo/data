class sample(object):
    def __init__(self,path,num,label):
        self.path=path
        self.num=num
        self.label=lablel
import os
import glob
rootdir='pic/'
train_files=glob.glob(rootdir+'train/*/*')
val_files=glob.glob(rootdir+'/val/*/*')
train_sample=[]
val_sample=[]
dic={'Riding':0,'Transport_HeavyCarry':2,'Pull':3,'A_carring':1}
for file in train_files:
    path=file
    num=len(os.listdir(file))
    label=dic[file.rsplit('/',3)[1]]
    if(num>0):
        for i in range(1,num):
            train_sample.append('{}/{}.jpg {}'.format(path,str(i),label))
for file in val_files:
    path=file
    num=len(os.listdir(file))
    label=dic[file.rsplit('/',3)[1]]
    if(num>0):
        for i in range(1,num):
            val_sample.append('{}/{}.jpg {}'.format(path,str(i),label))
open('list2/img_2018actev_train_file.txt','w').write('\n'.join(train_sample))
open('list2/img_2018actev_val_file.txt','w').write('\n'.join(val_sample))
