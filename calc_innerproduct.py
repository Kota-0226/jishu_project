import numpy as np

import basic_chordmatrix as bc


def calc_innerproduct(chord_matrix):
    score = 0
    index = 0
    
    for i in range(9):
        sum = 0
        #print("calc_innerproduct")
        for j in range(8):
            tmp = np.dot(bc.Chord[i][j],chord_matrix[j])
            #bc.Chord[i]は9(基本コード進行の数) * 8(コードの数) * 12(各コードの音に対応する,1,0が入っている)からなる。
            #chord_matrixは(8,12)になる
            sum += tmp
            #print("tmp = {}".format(tmp))
        if sum > score:
            score = sum
            index = i
        #print("inner_product with Chord{} = {}".format(i+1,sum))
    print("score={}".format(score))
    return index
    
