
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
key = input("What key are the chords in? (Major only) ").upper()
newkey = input("What key do you want the chords in? (Major only) ").upper()
chords = input("Give the chords in all caps separated by spaces(sharps only): ").split()
newchords = []
steps = notes.index(newkey) - notes.index(key) #Finding the number of steps between each key, negative values will be handled later
capo = (notes.index(key) - notes.index(newkey)) % 12 #Calculating the fret a capo needs to be placed in order to stay in the original key
for chord in chords:
    add = "" #Any additional chord modifications
    if '#' in chord:
        root = chord[:2].upper() #Finding the root of the chord (only the root changes when changing keys)
        if len(chord) > 2:
            add = chord[2:]
    else:
        root = chord[0].upper()
        if len(chord) > 1:
            add = chord[1:]
    if steps >= 0:
        if notes.index(root) + steps >= len(notes): #If number of steps exceeds the bounds of notes
            newchords.append(notes[notes.index(root) + steps - len(notes)] + add) #Wrapping to the start of notes
        else:
                newchords.append(notes[notes.index(root) + steps] + add) #Adding back on chord mods
    else:
        if notes.index(root) + steps >= 0:
            newchords.append(notes[notes.index(root) + steps] + add)
        else:
            newchords.append(notes[notes.index(root) + steps + len(notes)] + add)
print(chords)
print(newchords)
print(f'Note: Capo {capo} to stay in {key}.') #A note on how to not change keys by using a capo
