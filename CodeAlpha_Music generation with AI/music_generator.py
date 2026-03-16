import os
import random
from music21 import converter, note, chord, stream

notes = []

# Path to dataset
dataset_path = os.path.join(os.path.dirname(__file__), "midi_dataset")

# Read MIDI files
for file in os.listdir(dataset_path):
    if file.endswith(".mid"):
        midi = converter.parse(os.path.join(dataset_path, file))

        for element in midi.flatten().notes:

            if isinstance(element, note.Note):
                notes.append(str(element.pitch))

            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

print("Total notes extracted:", len(notes))

# Generate random music sequence
generated_notes = []

start = random.randint(0, len(notes)-100)
pattern = notes[start:start+50]

for i in range(100):
    next_note = random.choice(notes)
    generated_notes.append(next_note)

# Convert generated notes to MIDI
output_notes = []
offset = 0

for pattern in generated_notes:

    if '.' in pattern:  # chord
        notes_in_chord = pattern.split('.')
        chord_notes = []

        for n in notes_in_chord:
            try:
                new_note = note.Note(int(n))
                new_note.offset = offset
                chord_notes.append(new_note)
            except:
                continue

        new_chord = chord.Chord(chord_notes)
        output_notes.append(new_chord)

    else:  # single note
        try:
            new_note = note.Note(pattern)
            new_note.offset = offset
            output_notes.append(new_note)
        except:
            continue

    offset += 0.5

# Create MIDI file
midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp='generated_music.mid')

print("Music generated successfully!")