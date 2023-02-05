import music21 as m21
import markovify as mrkv
import os
import glob
import make_chords as mc

#参考:https://inglow.jp/techblog/python-scoremake/

def make_melody(a): #aにはとってくるサンプルデータが入ってくるディレクトリを表す！
    #読み込ませるテキスト準備用                                                                         
    note_txts = []
    
    #フォルダ内のxmlファイルを取得
    xmls = glob.glob(a + "*.mxl")
    
    for x in xmls:
        piece = m21.converter.parse(x)
        ntxt = []
        for n in piece.flat.notesAndRests:
            #n.name:音名の取得 n.duration.quaterLength:音の長さの取得(1拍,0.5拍など...)
            #ここは楽譜が単音だけ出ないとエラーを吐く
            ntxt.append(str(n.name) + '_' + str(n.duration.quarterLength))
            #count += float(n.duration.quarterLength)
            #print("n={}".format(n.duration.quarterLength))
            #1曲が終わったら追加する
        note_txts.append(' '.join(ntxt))

    #最後に、改行区切りでテキストデータを準備
    txts = '\n'.join(note_txts)

    times = 0
    while(1):
        times += 1 #何回whileを回しているか
        count = 0 #音価の長さを測るためのもの
        text_model = mrkv.NewlineText(txts,well_formed=False) #必要があれば、state_sizeを1-3で設定する。デフォは2.あと、well_formed=Falseとしないと読み込めないやつは排除されない
        #sentence = text_model.make_sentence(min_char = 50,max_char = 150)
        sentence = text_model.make_sentence(tries=100)
        #メロディをmusicXMLに変換する
        meas1 = m21.stream.Part() #楽譜オブジェクトの生成
        meas1.append(m21.meter.TimeSignature('4/4')) #拍子を4/4で固定
        print("sentence={}".format(sentence))
        melo = sentence.split() #半角スペース区切りで配列にする

        for m in melo: #[E_0.5,E_0.5,D_0.5,C#_0.5,...]のデータを順に処理
            ptch,dist = m.split('_') #アンダーバーで区切る
            if(ptch == 'rest'): #rest=休符,この場合は休符の長さだけ追加
                n = m21.note.Rest(quarterLength = float(dist))
            else: #音と音符の長さを追加
                n = m21.note.Note(ptch,quarterLength = float(dist))
            count += float(dist)
            #楽譜に追加
            meas1.append(n)

        print("times={}".format(times))
        if count == 16:
               break

    #小節線を追加する
    #meas1.makeMeasures(inPlace=True)
    #ここまででメロディーパート追加完了

    #楽譜をmusicxmlで表示する
    #meas1.show('musicxml',addEndTimds=True)

    return meas1
