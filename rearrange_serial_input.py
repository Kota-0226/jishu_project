def remove_serial_input_noise(array): #arrayにはserial通信で受け取ってきたものが入る
    l = len(array)
    #array_1 = []
    for i in range(l):
        #a = array[i][:-2] #Serial.println()を使っていた時
        a = array[i][:-2].decode()
        if a != "NoSound":
            b = a.replace("S","#")
        else:
            b = a
        array[i] = b
        #array_1.append(b)
    return array

def rearrage_for_score(array1):#arrayにはserial通信で受け取ってきたものが入る
    l = len(array1)
    i = 0
    temp = array1[0]
    while 1:
        if array1[i] != temp:
            return array1[i:i+64] #初めて音が入力されてから、4小節(4[個] * 4[拍]* 4[小節])分のデータを出力
        elif i + 64 > l:
            print("Error: No sound input")
            break
        else:
            i += 1


def rearrange_string_to_note(array2): #array2には、["E#3","F3",...]とかが入ってくる！
    l = len(array2)
    i = 0
    count = 0
    only_one_note = True
    sentence = []
    for j in range(l):
        if array2[j] == 'NoSound':
            array2[j] = 'rest'
    
    while 1 :
        if i == l-1: #最後まで読み込んだら
            sentence.append(array2[i-1] + "_" + str(count+0.25) )
            break
        elif i == 0:
            i += 1
            count += 0.25
        else:
            if array2[i] == array2[i-1]: #前の入力と同じ場合
                count += 0.25
            else: #前の入力と違う場合
                only_one_note = False
                sentence.append(array2[i-1] + "_" + str(count) )
                count = 0.25
            i += 1
    if only_one_note: #もしずっと同じ音が入力され続けていたら
            sentence.append(array2[i-1] + "_" + str(16))
    return sentence





        