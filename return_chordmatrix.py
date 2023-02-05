import music21 as m21
import numpy as np

import make_chords as mc

def chordmatrix(string):
    transpose = mc.chord_transpose(string) #コード進行のベース音が入る                                                                                         
    chord_type = mc.pickup_chordtype(string) #コード進行の種類が入る
    return np.roll(mc.a[chord_type],transpose) #1*12のnp配列が入る

def chordProgression_matrix(chord_progression): #chord_progressionにはコード進行の文字列が[1,8]のリストとして入ってくることを想定している
    l = len(chord_progression)
    tmp = np.zeros((l,12))
    for i in range(l):
        tmp[i] = chordmatrix(chord_progression[i])
    return tmp  #なんかfloat型で出力されている気がするがまあよし


        
