#!/usr/bin/python

LineNum = 0
TotalOctaves = []
OctaveSet = []
OctaveNum = 0
OctaveLocation = 0
OutputFileName = ''
global outfile

def convert2pi(inputvar):
    #function that converts OctaveSet into Sonic Pi Code
    #print(inputvar)
    CurrentOctaveLocation = 0 #location of first octave
    OctaveCount = int(len(inputvar)/2)
    
    #print('Number of octaves',OctaveCount)

    TargetChar = ''
    ChordLength = len(inputvar[CurrentOctaveLocation*2+1])
    SimultaneousChords = 0
    adjusted_input = [[ '-' for y in range( ChordLength ) ]   #columns
                            for x in range( OctaveCount ) ]   #rows

    while(CurrentOctaveLocation < OctaveCount):
        CurrentOctave = inputvar[CurrentOctaveLocation*2]
        #print('Current Octave is',CurrentOctave)
        CurrentChord = inputvar[CurrentOctaveLocation*2+1]
        #print(CurrentChord)
        ChordLength = len(CurrentChord)
        #print(ChordLength)
        

        
        CurrentChordLocation = 0
        while(CurrentChordLocation < ChordLength):
            TargetChar = CurrentChord[CurrentChordLocation]

            if(TargetChar.isupper() and TargetChar != '-'):
                TargetChar = TargetChar.upper() + 's' + CurrentOctave
                adjusted_input[CurrentOctaveLocation][CurrentChordLocation] = TargetChar

            if(TargetChar.islower() and TargetChar != '-'):
                TargetChar = TargetChar.upper() + CurrentOctave
                adjusted_input[CurrentOctaveLocation][CurrentChordLocation] = TargetChar
                
            if(TargetChar == '-'):
                adjusted_input[CurrentOctaveLocation][CurrentChordLocation] = TargetChar

            CurrentChordLocation = CurrentChordLocation + 1

        CurrentOctaveLocation = CurrentOctaveLocation + 1

    #print(adjusted_input)
    #print(len(adjusted_input[0]))
    Columns = len(adjusted_input[0])
    Rows = len(adjusted_input)
    CurrentColumn = 0
    Command = ''

    while CurrentColumn < Columns:
        CurrentRow = 0
        SimultaneousChords = 0
        Note = ''
        PrevNote = ''
        while CurrentRow < Rows:
            CurrentNote = adjusted_input[CurrentRow][CurrentColumn]

            if(CurrentNote != '-'):
                Note = CurrentNote
                SimultaneousChords = SimultaneousChords + 1
            CurrentRow = CurrentRow + 1
            #print(CurrentColumn)
        if(SimultaneousChords == 0):
            #print('sleep one_step')
            outfile.write('sleep one_step')
        if(SimultaneousChords == 1):
            Command = 'play :' + Note + ',release: 1\n'
            #print(Command)
            outfile.write(Command)
        if(SimultaneousChords > 1):
            CurrentRow = 0
            while CurrentRow < Rows:
                CurrentNote = adjusted_input[CurrentRow][CurrentColumn]
                if(CurrentNote != '-'):
                    Command = 'in_thread do\n' + 'play :' + CurrentNote + ',release: 1\n'
                    #print(Command)
                    outfile.write(Command)
                    #print('end')
                    outfile.write('end\n')
                CurrentRow = CurrentRow + 1
        CurrentColumn = CurrentColumn + 1
        outfile.write('\n')


    return

with open('source.txt', 'r') as srcfile:

    data = srcfile.read().splitlines()
    TotalLineNum = len(data)
    #print(TotalLineNum)
    OutputFileName = data[LineNum] + '.rb'
    LineNum = 1
    print('Exporting notes to SonicPi format: ' + OutputFileName + '\n')

    outfile = open(OutputFileName,'w')
    outfile.write('# SonicPi Code Generated using Python Code ~ (c)Anirudh Vemula\n')
    outfile.write('# Piano notes obtained from https://pianoletternotes.blogspot.com\n')
    outfile.write('use_synth :piano\n')
    outfile.write('one_step = 0.2\n\n')
    
    while LineNum < TotalLineNum:
        #If empty line, ignore and proceed to next line!
        if(data[LineNum] == ''): #skip, next octave-set begins
            if(len(OctaveSet) > 0):
                convert2pi(OctaveSet)
            LineNum = LineNum + 1
            #print('\n')
            OctaveSet = []
        else:
            
            #print('Line number is',LineNum) #important
            Chords = data[LineNum]
            #print(Chords,'\n')
            OctaveLocation = data[LineNum].find('|')-1
            #print('Octave Location',OctaveLocation)
            OctaveNum = Chords[OctaveLocation]
            #print('Octave Number',OctaveNum)
            list.append(OctaveSet,OctaveNum)
            NumChords = len(data[LineNum]) - data[LineNum].find('|') - 2
            #print(NumChords)
            TotalOctaves = Chords[OctaveLocation+2:NumChords+OctaveLocation+2]
            #print('Total Octaves',TotalOctaves)
            list.append(OctaveSet,TotalOctaves)

            LineNum = LineNum + 1
    convert2pi(OctaveSet)

outfile.close()
print('Export Successful!')

