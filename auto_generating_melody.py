import music21 as m21
import os
import glob
import sys
import subprocess

import PySimpleGUI as sg
import make_melody as mm
import make_chords as mc
import return_chordmatrix as rc
import calc_innerproduct as ci

sg.theme('DarkTeal2')

layout = [  [sg.Text('これは、入力されたコード進行から自動でOfficial髭男dismみたいなメロディーを生成してくれるものです。')],
            [sg.Text('コードは半角スペースで区切って8つ入力してください。一つのコードにつき2拍、トータルで4/4拍子で4小節のメロディーが生成されます。')],
            [sg.Text('以下のコードが使えます:maj min dim aug M7 m7 7 dim7 hdim7 mM7 M6 m6 9 M9 m9 sus2 sus4')],
            [sg.Text('ただし、以下の注意点に気を付けてください。')],
            [sg.Text('1.フラットを入力したいときは"-"と入力してください。 ex)E♭ -> E-')],
            [sg.Text('2.C majorを入力したい時は単に"C", C minorを入力したい時は"Cm"のように入力してください。')],
            [sg.Text('入力例:C C-sus2 E#m Em Am Am Dm Dm')],
            [sg.Text('それではコード進行を入力してください。')],
            [sg.Input(key='chord_progression'),sg.Button('実行', key='start')],
            [sg.Output(size=(100,30))]
            ]
    
window = sg.Window('コード進行から自動でメロディーを生成するツール', layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED: #ウィンドウのXボタンを押したときの処理
        break

    if event == 'start':
        chord_progression = list(values['chord_progression'].split())
        print("chord_progression={}".format(chord_progression))
        l = len(chord_progression)
        chord_array = rc.chordProgression_matrix(chord_progression)
        result = ci.calc_innerproduct(chord_array) + 1 #何番目のコード進行に類似しているか
        print("This entered chord progression is most similar to Chord{}".format(result))
        DS = os.sep #これは"/"を意味する                                                                                                                                        
        bs = os.path.dirname(__file__) + DS #このファイルのありか                                                                                                               
        xmlpath = bs + 'musicxml_simple' + str(result) + DS

        stream1 = mm.make_melody(xmlpath) 

        
        stream2 = m21.stream.Part()
        #print("l={}".format(l)) #ここが32になってる、おかしい,8のはず
        for i in range(l):
            key = mc.chord_transpose(chord_progression[i])
            if key > 5:
                key = -1 * (12 - key)
            n = mc.pickup_chordtype(chord_progression[i]) #コードの種類が数字で返ってくる、詳しくはmake_chords.py参照
            chord = mc.return_chord_type(n) 
            stream2.append(chord.transpose(key)) #二拍分の伴奏追加
            stream2.append(chord.transpose(key))
            #print("chord = {}".format(chord))
        

        score = m21.stream.Score()

        score.insert(0, stream1)
        score.insert(0, stream2)


        score.show('musicxml')
        #break





window.close()

"""
DS = os.sep #これは"/"を意味する                                                                                                                                        
bs = os.path.dirname(__file__) + DS #このファイルのありか                                                                                                               
xmlpath = bs + 'musicxml_simple' + str(result) + DS

stream1 = mm.make_melody(xmlpath) 




score = m21.stream.Score()

score.insert(0, stream1)
score.insert(0, stream2)


score.show('musicxml')
"""

