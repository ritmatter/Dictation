from aubio import source, pitch
import math

class PitchReader:
    
    def __init__(self, tolerance, sample_rate, down_sample, win_size, hop_size):
        self.tolerance = tolerance
        self.sample_rate = sample_rate
        self.down_sample = down_sample
        self.win_size = win_size
        self.pitch_data = self.initPitchData()
        self.hop_size = hop_size
        
    def initPitchData(self):
        pitch_data = []
        for x in range(0, 3):
            pitch_data.append([])
        return pitch_data
        
    def hearingThreshold(self, frequency):
        if frequency == 0:
            return 0;
        
        freqConst = float(frequency)/1000.0
        return 3.64 * freqConst**(-0.8) - 6.5 * math.exp(-0.6 * (freqConst - 3.3)**2) + 10**(-3) * freqConst**4
        
    def analyzePitches(self, music_file):
        s = source(music_file, self.sample_rate, self.hop_size)
        pitch_o = pitch("yin", self.win_size, self.hop_size, self.sample_rate)
        pitch_o.set_unit("freq")    
        pitch_o.set_tolerance(self.tolerance)
        
        total_frames = 0     # total number of frames read
        while True:
            samples, read = s()
            curr_pitch = pitch_o(samples)[0]
            confidence = pitch_o.get_confidence()
            silence = self.hearingThreshold(curr_pitch)
            self.pitch_data[0].append(curr_pitch)
            self.pitch_data[1].append(confidence)
            self.pitch_data[2].append(silence)
            
            total_frames += read
            if read < self.hop_size: 
                break
        return self.pitch_data
    
    def writePitches(self, write_file):
        f = open(write_file, 'w')
        for i in range (0, len(self.pitch_data[0])):
            f.write(str(self.pitch_data[0][i]) + "  " + str(self.pitch_data[1][i]) + "  " + str(self.pitch_data[2][i]) + '\n')
        f.close()
            
            