class NoteReader:
    
    def __init__(self, note_file):
        self.note_file = note_file
        self.note_book = self.initializeNoteBook(note_file);
        self.freq_list = self.initializeFreqList()
        
    def initializeNoteBook(self, note_file):
        note_book = {}
        f = open(note_file, 'r')
        for line in f:
            freq = float(line.split(",")[0])
            note = line.split(",")[1].strip()
            note_book[freq] = note
        f.close()
        return note_book
    
    def initializeFreqList(self):
        freq_list = []
        for key in self.note_book.keys():
            freq_list.append(key)
        return sorted(freq_list)
    
    def mapNote(self, freq):
        return self.note_book[freq]
    
    def printNoteBook(self):
        for key in self.note_book.keys():
            print "{},{}".format(key, self.note_book[key])
            
    def writeNoteBook(self, note_file):
        f = open(note_file, 'w')
        for key in self.note_book.keys():
            f.write(str(key) + ',' + self.note_book[key] + '\n')
        f.close()