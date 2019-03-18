# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:36:17 2019

@author: 78237
"""

import random
_NUM_VALIDATION = 50
_RANDOM_SEED = 0
list_path = 'G:\DATA\list.txt'
train_list_path = 'G:\DATA\list_train.txt'
val_list_path = 'G:\DATA\list_val.txt'
fd = open(list_path)
lines = fd.readlines()
fd.close()
random.seed(_RANDOM_SEED)
random.shuffle(lines)
fd = open(train_list_path, 'w')
for line in lines[_NUM_VALIDATION:]:
    fd.write(line)
fd.close()
fd = open(val_list_path, 'w')
for line in lines[:_NUM_VALIDATION]:
    fd.write(line)
fd.close()