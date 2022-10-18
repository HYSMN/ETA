import csv
import numpy as np
import ast
import re
import io
from numpy import unicode

route_feature = open('route_node2.txt').read()
route_feature_arr = route_feature.split('[')
route_feature_all = []

policy_feature = np.loadtxt('bilstm_feature2.txt')
# day_feature = np.loadtxt('label_input.txt')
day_feature = []
filename = 'routeall2.txt'
with open(filename) as f:
    reader = csv.reader(f)
    for row2 in reader:
        # print(row2[-3])
        day_feature.append(int(row2[-3]))
np.savetxt('label_input02.txt', np.array(day_feature))
        
print(day_feature)
feature_input = []

for i, item in enumerate(route_feature_arr):
    if item != '':
        if i == 15367:
            break
        to_arr = []
        item = item.strip(' ]\n')
        item = item.replace('\n', '')
        item_arr = item.split(' ')
        for it in item_arr:
            if it != '':
              to_arr.append(float(it))  
        to_arr.append(day_feature[i-1])
        final_feature = np.concatenate((policy_feature[i-1], to_arr),axis=0)
        feature_input.append(final_feature)

np.savetxt('feature_input02.txt', np.array(feature_input))
        
        



