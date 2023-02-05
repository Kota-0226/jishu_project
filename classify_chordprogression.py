import music21 as m21
import numpy as np

import return_chordmatrix as rc
import calc_innerproduct as ci




print("Just enter 8 chords and it will automatically generate a melody in 4/4 time for 4 measures.")
print("Enter eight chord progressions that form the base of the melody, separated by one-byte spaces. Each chord is equivalent to two beats.")
print("In addition, the following chords can be used.")
print("maj,min,dim,aug,M7,m7,7,dim7,hdim7,mM7,M6,m6,9,M9,m9,sus2,sus4")
print("when you enter the chord progression,please following the following rules.")
print("1.Enter '-' for flat (♭)")
print("2.If you want to enter 'C major',please enter 'C'")
print("3.In other case,please enter 'RootNote + Chordname' e.g. 'C major 7' -> 'CM7'")
print("Example: C C-sus2 E#m Em Am Am Dm Dm")
print(" ")
print("Please input chords progression.")
chord_progression = input().split()
print(chord_progression)
#もしうまくいかなくてもとのやつ見たかったらこの上２行をコメントイン

chord_array = rc.chordProgression_matrix(chord_progression)
result = ci.calc_innerproduct(chord_array) + 1 #何番目のコード進行に類似しているか
print("This entered chord progression is most similar to Chord{}".format(result))





