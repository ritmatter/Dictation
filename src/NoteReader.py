

class NoteReader:
    
    def __init__(self, noteFile):
        self.noteFile = noteFile
        self.noteBook = self.initializeNoteBook(noteFile);
        
    def initializeNoteBook(self, noteFile):
        noteBook = {}
        f = open(noteFile, 'r')
        for line in f:
            note = line.split(",")[0]
            freq = float(line.split(",")[1].strip())
            noteBook[note] = freq
        f.close()
        return noteBook
    
    def readNoteBook(self):
        for key in self.noteBook.keys():
            print "{},{}".format(key, self.noteBook[key])
            
    def writeNoteBook(self, noteFile):
        f = open(noteFile, 'w')
        for key in self.noteBook.keys():
            f.write(key + ',' + str(self.noteBook[key]) + '\n')
        f.close()