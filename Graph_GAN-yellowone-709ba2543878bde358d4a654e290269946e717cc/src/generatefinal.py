import csv
import numpy as np
import ast
import re
import io
from numpy import unicode

def generate_edge_type(para1, para2):

    train_data = np.loadtxt('../data/route/train3.txt', delimiter=' ')

    for row in train_data:               
        if ((row[1] == para1) & (row[2] == para2)):
            return int(row[0])
        if ((row[2] == para1) & (row[1] == para2)):
            return int(row[0])
    return -1

def find_node_ebed(node, edge):

    all_the_text = open('3rest'+edge+'.txt').read()
    arr = all_the_text.split(']')

    for item in arr:
        temp = item.split('[')
        nodeid = temp[0].split(' ')
        nodeid = nodeid[-1]
       
        if nodeid == str(node):
            temp[-1]=temp[-1].replace('\n',' ')
            final_emb = re.split(r' +', temp[-1])
            if final_emb[0] == '':
                final_emb = final_emb[1:]
            final_emb = ','.join(final_emb)
            return final_emb
    return '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'

def transfor_string_to_array(st):
    arr = ast.literal_eval(st)
    arr = np.array(arr)
    return arr


route = open('nodenum3.txt').read()
route_arr = route.split('\n')
# route_all = []
for row1 in route_arr:
    row1 = transfor_string_to_array(row1)
    route_th = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, word in enumerate(row1):
        now_node_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if word is not 'None':
            if word == row1[0]:
                word = int(word)  
                print(word) 
                continue         
            elif word == row1[-1]:
                word = int(word)
                print(word) 
                edge_type_left = generate_edge_type(word, int(row1[i-1]))
                if edge_type_left == -1:
                    str0 = find_node_ebed(word, '0')
                    emb0 = transfor_string_to_array(str0)
                    str1 = find_node_ebed(word, '1')
                    emb1 = transfor_string_to_array(str1)
                    str2 = find_node_ebed(word, '2')
                    emb2 = transfor_string_to_array(str2)
                    str3 = find_node_ebed(word, '3')
                    emb3 = transfor_string_to_array(str3)
                    str4 = find_node_ebed(word, '4')
                    emb4 = transfor_string_to_array(str4)
                    str5 = find_node_ebed(word, '5')
                    emb5 = transfor_string_to_array(str5)
                    str6 = find_node_ebed(word, '6')
                    emb6 = transfor_string_to_array(str6)
                    now_node_arr = emb0+emb1+emb2+emb3+emb4+emb5+emb6
                    now_node_arr = np.divide(now_node_arr, 7)
                    print(now_node_arr)
                else:
                    now_node = find_node_ebed(word, str(edge_type_left))
                    now_node_arr = transfor_string_to_array(now_node)
                    print(now_node_arr)
            else:
                word = int(word)
                print(word) 
                edge_type_right = generate_edge_type(word, int(row1[i+1]))
                edge_type_left = generate_edge_type(word, int(row1[i-1]))   
                print(edge_type_right)
                print(edge_type_left)
                if edge_type_left != -1:
                    now_node = find_node_ebed(word, str(edge_type_left))
                    now_node_arr = transfor_string_to_array(now_node)
                    print(now_node_arr)  

                elif edge_type_right != -1:
                    now_node = find_node_ebed(word, str(edge_type_right))
                    now_node_arr1 = transfor_string_to_array(now_node)
                    print(now_node_arr1)
                    print(now_node_arr)
                    now_node_arr = now_node_arr1 + now_node_arr 
                    if edge_type_left != -1:
                        now_node_arr = np.divide(now_node_arr, 2)
                    print(now_node_arr)  
                
                else:
                    str0 = find_node_ebed(word, '0')
                    emb0 = transfor_string_to_array(str0)
                    str1 = find_node_ebed(word, '1')
                    emb1 = transfor_string_to_array(str1)
                    str2 = find_node_ebed(word, '2')
                    emb2 = transfor_string_to_array(str2)
                    str3 = find_node_ebed(word, '3')
                    emb3 = transfor_string_to_array(str3)
                    str4 = find_node_ebed(word, '4')
                    emb4 = transfor_string_to_array(str4)
                    str5 = find_node_ebed(word, '5')
                    emb5 = transfor_string_to_array(str5)
                    str6 = find_node_ebed(word, '6')
                    emb6 = transfor_string_to_array(str6)
                    now_node_arr = emb0+emb1+emb2+emb3+emb4+emb5+emb6
                    now_node_arr = np.divide(now_node_arr, 7)
                    print(now_node_arr)

        if now_node_arr[0] == now_node_arr[1]:
            continue
        else:
            route_th = route_th + now_node_arr

    with io.open('route_node3.txt', mode="a", encoding='utf-8') as data1:  
        data1.write(unicode(route_th))
        data1.write('\n')



