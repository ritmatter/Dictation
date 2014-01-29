import math

CHANGE = 0.056

class PitchToNoteConverter:
    
    
    def __init__(self, freq_list, pitch_data, noteBook):
        self.freq_list = freq_list
        self.pitch_data = pitch_data
        self.clumped_pitches = self.initClumpedPitches()
        self.noteBook = noteBook
        
    def initClumpedPitches(self):
        clumped_pitches = []
        for x in range(0, 3):
            clumped_pitches.append([])
        return clumped_pitches
        
    def withinRange(self, a, b):
        if (math.fabs(a-b)/b <= CHANGE):
            return True
        return False;
        
    def clumpPitches(self, freq):
        conseq = 0
        for i in range(1, len(self.pitch_data[0])):
            if self.withinRange(self.pitch_data[0][i], self.pitch_data[i-1]):
                if (conseq < 3):
                    conseq += 1
            else:
                conseq = 0
        
    def closestMatch(self, freq):
        return self.findClosestMatch(freq, 0, len(self.freq_list)-1)
    
    def findClosestMatch(self, freq, l, h):
        if h <= l or h-l == 1:
            if math.fabs(self.freq_list[h] - freq) < math.fabs(self.freq_list[l] - freq):
                return self.freq_list[h]
            return self.freq_list[l]
        
        m = (h+l)/2
        if freq > self.freq_list[m]:
            return self.findClosestMatch(freq, m, h)
        elif freq < self.freq_list[m]:
            return self.findClosestMatch(freq, l, m)
        else:
            return self.freq_list[m]
            