# chord_converter

Python script that takes a musical key, a desired key, and a list of chords and outputs a new list of the corresponding chords in the new key.

## The Problem

When playing guitar, I often find chord charts that are in a key that is very difficult for me to play. Although I can mentally transpose, it takes me a long time and would be easier if I had a way to automate it.

## How It Works

- Takes the current key, the new key, and a list of chords
- Finds the number of steps from the current to new key
- Transposes every chord in the list by that number of steps
- Outputs the list of transposed chords

![System diagram](images/chord_converter_flowchart.png)

## Tech Stack

- **Language:** Python

## Setup

```bash
git clone https://github.com/connorallison07-AI/chord_converter
cd chord_converter
python chord_converter.py
```

## Usage

Run the script and provide the 3 input fields

```bash
python chord_converter.py
```

**Input Rules**

- Chords and keys must be all caps with only sharps (ex: A, Am, A# not Ab, Amaj7, Aadd9, Adim)
- Separate chords with a single space
- Only major keys
- No chords with added sharp notes or slash chords

**Example**

```
What key are the chords in? C
What key do you want the chords in? G
Give the chords in all caps separated by spaces (sharps only): C Am F G
['C', 'Am', 'F', 'G']
['G', 'Em', 'C', 'D']
```

**Limitations**

- Slash chords and chords with added sharp notes are not yet supported (ex: Cadd#7, A7#2, D/F#, G/B)

## Roadmap

Features you haven't built yet but plan to (pull these from your
"Schedule" quadrant in the Eisenhower Matrix).

- [x] Complex Chords
- [x] Capo Fret Output
- [ ] Guitar-friendly Key Recommendations

## Author

Connor Allison, https://github.com/connorallison07-AI
