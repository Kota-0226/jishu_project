import numpy as np
import music21 as m21

import return_chordmatrix as rc

"""
ここでは基本的なコード進行９つのmatrixを作る
Chord1 = C C F F G G G G
Chord2 = F F G7 G7 Em Em Am Am
Chord3 = Am Am F F G G C C
Chord4 = Am Am Dm Dm G G Am Am
Chord5 = C C Am Am F F G7 G7
Chord6 = F F G G Am Am Am Am 
Chord7 = C C Am Am Dm Dm G7 G7
Chord8 = Am Am Em Em F F G7 G7
Chord9 = C G Am Em F C F G
"""

C = rc.chordmatrix("C")
F = rc.chordmatrix("F")
G = rc.chordmatrix("G")
G7 = rc.chordmatrix("G7")
Em = rc.chordmatrix("Em")
Am = rc.chordmatrix("Am")
Dm = rc.chordmatrix("Dm")



Chord_1 = rc.chordProgression_matrix(["C","C","F","F","G","G","G","G"])
Chord_2 = rc.chordProgression_matrix(["F","F","G7","G7","Em","Em","Am","Am"])
Chord_3 = rc.chordProgression_matrix(["Am","Am","F","F","G","G","C","C"])
Chord_4 = rc.chordProgression_matrix(["Am","Am","Dm","Dm","G","G","Am","Am"])
Chord_5 = rc.chordProgression_matrix(["C","C","Am","Am","F","F","G7","G7"])
Chord_6 = rc.chordProgression_matrix(["F","F","G","G","Am","Am","Am","Am"])
Chord_7 = rc.chordProgression_matrix(["C","C","Am","Am","Dm","Dm","G7","G7"])
Chord_8 = rc.chordProgression_matrix(["Am","Am","Em","Em","F","F","G7","G7"])
Chord_9 = rc.chordProgression_matrix(["C","G","Am","Em","F","C","F","G"])

Chord = np.array([Chord_1,Chord_2,Chord_3,Chord_4,Chord_5,Chord_6,Chord_7,Chord_8,Chord_9])
#print(Chord)



