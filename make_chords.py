import music21 as m21
import numpy as np

"""
a0 = major
a1 = minor
a2 = dim
a3 = aug
a4 = maj7
a5 = min7
a6 = seventh
a7 = dim7
a8 = hdim7
a9 = minmaj7
a10 = maj6
a11 = min6
a12 = ninth
a13 = maj9
a14 = min9
a15 = sus2
a16 = sus4
"""
major = m21.chord.Chord(['c3','e3','g3'])
minor = m21.chord.Chord(['c3','e-3','g3'])
dim = m21.chord.Chord(['c3','e-3','g-3'])
aug = m21.chord.Chord(['c3','e3','g#3'])
maj7 = m21.chord.Chord(['c3','e3','g3','b3'])
min7 = m21.chord.Chord(['c3','e-3','g3','b-3'])
seventh = m21.chord.Chord(['c3','e3','g3','b-3'])
dim7 = m21.chord.Chord(['c3','e-3','g-3','a3']) 
hdim7 = m21.chord.Chord(['c3','e-3','g-3','a#3'])
minmaj7 = m21.chord.Chord(['c3','e-3','g3','b3'])
maj6 = m21.chord.Chord(['c3','e3','g3','a3'])
min6 = m21.chord.Chord(['c3','e-3','g3','a3'])
ninth = m21.chord.Chord(['c3','d3','e3','g3','b-3'])
maj9 = m21.chord.Chord(['c3','d4','e-3','g3','b3'])
min9 = m21.chord.Chord(['c3','d4','e-3','g3','b-3'])
sus2 = m21.chord.Chord(['c3','d3','g3'])
sus4 = m21.chord.Chord(['c3','f3','g3'])

a = np.zeros((17,12),dtype = int)
a[0] = np.array([1,0,0,0,1,0,0,1,0,0,0,0])
a[1] = np.array([1,0,0,1,0,0,0,1,0,0,0,0])
a[2] = np.array([1,0,0,1,0,0,1,0,0,0,0,0])
a[3] = np.array([1,0,0,0,1,0,0,0,1,0,0,0])
a[4] = np.array([1,0,0,0,1,0,0,1,0,0,0,1])
a[5] = np.array([1,0,0,1,0,0,0,1,0,0,1,0])
a[6] = np.array([1,0,0,0,1,0,0,1,0,0,1,0])
a[7] = np.array([1,0,0,1,0,0,1,0,0,1,0,0])
a[8] = np.array([1,0,0,1,0,0,1,0,0,0,1,0])
a[9] = np.array([1,0,0,1,0,0,0,1,0,0,0,1])
a[10] = np.array([1,0,0,0,1,0,0,1,0,1,0,0])
a[11] = np.array([1,0,0,1,0,0,0,1,0,1,0,0])
a[12]= np.array([1,0,1,0,1,0,0,1,0,0,1,0])
a[13] = np.array([1,0,1,0,1,0,0,1,0,0,0,1])
a[14] = np.array([1,0,1,1,0,0,0,1,0,0,1,0])
a[15] = np.array([1,0,1,0,0,0,0,1,0,0,0,0])
a[16] = np.array([1,0,0,0,0,1,0,1,0,0,0,0])

chord_key = ["C","C#","C-","D","D#","D-","E","E#","E-","F","F#","F-","G","G#","G-","A","A#","A-","B","B#","B-",]

def chord_transpose(strings):
  #stringsはコードを想定。e.g. C#m,E-sus4                                                                          
    if ("C#" in strings) or ("D-" in strings) :
        return 1
    elif ("D#" in strings) or ("E-" in strings):
        return 3
    elif ("F# "in strings) or ("G-" in strings) :
        return 6
    elif ("G#" in strings) or ( "A-" in strings):
        return 8
    elif ("A#" in strings) or ("B-" in strings):
        return 10
    elif "C" in strings:
        return 0
    elif "D" in strings:
        return 2
    elif "E" in strings:
        return 4
    elif "F" in strings:
        return 5
    elif "G" in strings:
        return 7
    elif "A" in strings :
        return 9
    else:
        return 11


def pickup_chordtype(strings):
    if len(strings) == 1:
        return 0
    elif (strings[1] == "#") or (strings[1] == "-"):
        if len(strings) == 2:
            return 0
        else:
            return chordtype(strings[2:])
    else:
        return chordtype(strings[1:])



def chordtype(s):
    if s == "m":
        return 1
    elif s == "dim":
        return 2
    elif s == "aug":
        return 3
    elif s == "M7":
        return 4
    elif s == "m7":
        return 5
    elif s == "7":
        return 6
    elif s == "dim7":
        return 7
    elif s == "hdim7":
        return 8
    elif s == "mM7":
        return 9
    elif s == "6":
        return 10
    elif s == "m6":
        return 11
    elif s == "9":
        return 12
    elif s == "M9":
        return 13
    elif s == "m9":
        return 14
    elif s == "sus2":
        return 15
    elif s == "sus4":
        return 16
    else: #とりあえずどこにも当てはまらないやつが入力されたら、基本のmajorスケールのコードとして返す。             
        print("This chord ({}) isn't expected to be entered,so we regard {} as major chord.".format(s,s))
        return 0


def return_chord_type(n):
    if n==1:
        return minor
    elif n==2:
        return dim
    elif n==3:
        return aug
    elif n==4:
        return maj7
    elif n==5:
        return min7
    elif n==6:
        return seventh
    elif n==7:
        return dim7
    elif n==8:
        return hdim7
    elif n==9:
        return minmaj7
    elif n==10:
        return maj6
    elif n==11:
        return min6
    elif n==12:
        return ninth
    elif n==13:
        return maj9
    elif n==14:
        return min9
    elif n==15:
        return sus2
    elif n==16:
        return sus4
    else:
        return major
