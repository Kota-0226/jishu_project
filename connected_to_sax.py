# coding: utf-8

import serial
import music21 as m21
import time
import sys
import os
import threading
import rearrange_serial_input as rsi


#from pynput.keyboard import Key

#メトロノーム関連、予備拍を出す
""" 設定パート """
BPM = 120 #BPMを入力,今回はこれで固定
tone = 0 #音の高さ 整数を入力 0=ド 1変わると半音変わる　2=レ 4=ミ 9=ラ
duration = 50 #1音の長さ：通常 50, 推奨 10~100 長くしすぎるとBPMに影響
cycle = 10 #繰り返し回数
""" 設定パートここまで """

tone_d = tone-9
freq = int(440*2**(tone_d/12)) #周波数
sleep_time = (60/BPM) - (duration/1000) #停止時間

print("After the preliminary beat is eight beats in, begin scoring")

#シリアル通信関連

ser = serial.Serial('/dev/cu.usbserial-1430', 9600) 
not_used = ser.readline()
start = time.time()
score_data = []

#threadlock = threading.Lock()
#print("If you want to stop scoring, please press Enter Key")

#予備拍がなっているうちはserial通信を読み込まないようにする
#threadlock.acquire()

for i in range(24): #テンポを8拍予備で出す,その後16拍打ち続ける
    os.system('play -n synth %s sin %s' % (duration/1000, freq)) #440hz, 100ミリ秒の音
    time.sleep(sleep_time) 

#threadlock.release()
print(time.time()-start)
#一秒に10回の値がArduino nanoから送られてくる。
for i in range(110):
    val_arduino = ser.readline()
    # val_decoded = float(repr(val_arduino.decode())[1:-5])
    val_decoded = val_arduino
    score_data.append(val_decoded)
    print(val_decoded)
    #print(score_data)

ser.close()

#まずはバイナリデータを普通のstringに戻す
score_data_two = rsi.remove_serial_input_noise(score_data)

#ここで、初めて音が入力されてから4/4で4小節分の情報(一拍4*4*4 = 64)だけを取ってくる
score_data_three = rsi.rearrage_for_score(score_data_two) 

#ここで音高+音長に変換
melo = rsi.rearrange_string_to_note(score_data_three)

print(melo)
meas = m21.stream.Stream() #楽譜
meas.append(m21.meter.TimeSignature('4/4'))


#melo = sentence.split() #半角スペース区切りで配列にする

for m in melo: #[E_0.5,E_0.5,D_0.5,C#_0.5,...]のデータを順に処理
    ptch,dist = m.split('_') #アンダーバーで区切る
    if(ptch == 'rest'): #rest=休符,この場合は休符の長さだけ追加
        n = m21.note.Rest(quarterLength = float(dist))
    else: #音と音符の長さを追加
        n = m21.note.Note(ptch,quarterLength = float(dist))
        #楽譜に追加
    meas.append(n)

meas.show('musicxml')
