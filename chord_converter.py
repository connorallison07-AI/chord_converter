
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
key = input("What key are the chords in? ")
newkey = input("What key do you want the chords in? ")
chords = input("Give the chords in all caps separated by spaces(sharps only): ").split()
newchords = []
steps = notes.index(newkey) - notes.index(key) #Finding the number of steps between each key, negative values will be handled later
for chord in chords:
    if notes.index(chord) + steps >= len(notes): #Handling wrap-around cases
        newchords.append(notes[notes.index(chord) + steps - len(notes)])
    else:
        newchords.append(notes[notes.index(chord) + steps])
print(chords)
print(newchords)
