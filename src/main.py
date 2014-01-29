#!/usr/bin/python2.7

import sys
from NoteReader import NoteReader
from PitchReader import PitchReader
from PitchToNoteConverter import PitchToNoteConverter

file_name = sys.argv[1]

down_sample = 1
sample_rate = 44100 / down_sample
win_size = 4096 / down_sample # fft size
hop_size = 512  / down_sample # hop size
tolerance = 0.8

# pitchReader = PitchReader(tolerance, sample_rate, down_sample, win_size, hop_size)
# pitchReader.pitch_data = pitchReader.analyzePitches(file_name)
# pitchReader.writePitches("pitches.txt")

noteReader = NoteReader("notes.txt")
pitchToNoteConverter = PitchToNoteConverter(noteReader.freq_list, [])
