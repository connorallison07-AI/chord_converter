
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
key = input("What key are the chords in? ")
newkey = input("What key do you want the chords in? ")
chords = input("Give the chords in all caps separated by spaces(sharps only): ").split()
newchords = []
steps = notes.index(newkey) - notes.index(key) #Finding the number of steps between each key, negative values will be handled later
capo = (notes.index(key) - notes.index(newkey)) % 12 #Calculating the fret a capo needs to be placed in order to stay in the original key
for chord in chords:
    if 'm' in chord: #Checking if chord is minor
        if steps >= 0: #If new key is further in notes list than key
            if notes.index(chord.rstrip('m')) + steps >= len(notes): #Taking away the minor symbol and adding it back when appending
                newchords.append(notes[notes.index(chord.rstrip('m')) + steps - len(notes)] + 'm')
            else:
                newchords.append(notes[notes.index(chord.rstrip('m')) + steps] + 'm')
        else:
            if notes.index(chord.rstrip('m')) + steps >= 0:
                newchords.append(notes[notes.index(chord.rstrip('m')) + steps] + 'm')
            else:
                newchords.append(notes[notes.index(chord.rstrip('m')) + steps + len(notes)] + 'm')
    else:
        if steps >= 0:
            if notes.index(chord) + steps >= len(notes): #If number of steps exceeds the bounds of notes
                newchords.append(notes[notes.index(chord) + steps - len(notes)]) #Wrapping to the start of notes
            else:
                    newchords.append(notes[notes.index(chord) + steps])
        else:
            if notes.index(chord) + steps >= 0:
                newchords.append(notes[notes.index(chord) + steps])
            else:
                newchords.append(notes[notes.index(chord) + steps + len(notes)])
print(chords)
print(newchords)
print(f'Note: Capo {capo} to stay in {key}.') #A note on how to not change keys by using a capo
