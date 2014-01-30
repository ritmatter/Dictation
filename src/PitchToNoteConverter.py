import math

CHANGE = 0.056

class PitchToNoteConverter:
    
    
    def __init__(self, note_book, pitch_reader):
        self.clumped_pitches = self.initClumpedPitches()
        self.note_reader = note_book
        self.pitch_reader = pitch_reader
        
    def initClumpedPitches(self):
        clumped_pitches = []
        for x in range(0, 3):
            clumped_pitches.append([])
        return clumped_pitches
        
    def withinRange(self, a, b):
        if (a == 0 and b == 0):
            return True
        if (a == 0 and b != 0 or a != 0 and b == 0):
            return False
        if (math.fabs(a-b)/b <= 0.056):
            return True
        return False;
    
    def mapNotes(self):
        for i in range(0, len(self.clumped_pitches[0])):
            self.clumped_pitches[0][i] = self.note_reader.mapNote(self.clumped_pitches[0][i])
        return self.clumped_pitches
         
    def clumpPitches(self):
        consec = 3
        seg_len = 1
        seg_start = 0
        seg_head = self.pitch_reader.pitch_data[0][0]
        for i in range(1, len(self.pitch_reader.pitch_data[0])):
            curr_pitch = self.pitch_reader.pitch_data[0][i]
            #prev_pitch = self.pitch_reader.pitch_data[0][i-1]
            if not self.withinRange(curr_pitch, seg_head):
                if consec <= 0:
                    avg_pitch = self.avgPitch(seg_start, seg_len)
                    seg_time = self.segTime(seg_len)
                    self.clumped_pitches[0].append(avg_pitch)
                    self.clumped_pitches[1].append(seg_time)
                    print "{}, {}, {}".format(avg_pitch, seg_time, seg_head)
                    seg_len = 3
                    seg_start = i-2
                    seg_head = self.pitch_reader.pitch_data[0][i-2]
                    consec = 3
                else:
                    consec -= 1
            else:
                if consec >= 3:
                    seg_len += 1
                else:
                    consec += 1
                    
            #print "{}, {}, {}".format(curr_pitch, seg_head, consec)
        
        avg_pitch = self.avgPitch(seg_start, seg_len)
        seg_time = self.segTime(seg_len)
        self.clumped_pitches[0].append(avg_pitch)
        self.clumped_pitches[1].append(seg_time)                  
        return self.clumped_pitches
    
    def segTime(self, seg_len):
        samples = (seg_len - 1) * self.pitch_reader.hop_size + self.pitch_reader.win_size
        return samples/(1.0 * self.pitch_reader.sample_rate)
        
    def avgPitch(self, seg_start, seg_len):
        total = 0
        for i in range(seg_start, seg_start + seg_len - 1):
            total += self.pitch_reader.pitch_data[0][i]
        avg_pitch = total/seg_len
        return self.closestMatch(avg_pitch)    
        
    def closestMatch(self, freq):
        return self.findClosestMatch(freq, 0, len(self.note_reader.freq_list)-1)
    
    def findClosestMatch(self, freq, l, h):
        if h <= l or h-l == 1:
            if math.fabs(self.note_reader.freq_list[h] - freq) < math.fabs(self.note_reader.freq_list[l] - freq):
                return self.note_reader.freq_list[h]
            return self.note_reader.freq_list[l]
        
        m = (h+l)/2
        if freq > self.note_reader.freq_list[m]:
            return self.findClosestMatch(freq, m, h)
        elif freq < self.note_reader.freq_list[m]:
            return self.findClosestMatch(freq, l, m)
        else:
            return self.note_reader.freq_list[m]
            