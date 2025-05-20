from midiutil import MIDIFile

tempo = 90
track = 0
channel = 0
volume = 100
duration_whole = 4
duration_eighth = 0.5

chord_map = {
    "CM": [60, 64, 67],
    "DM": [62, 66, 69],
    "dm": [62, 65, 69],
    "EM": [64, 68, 71],
    "EM7": [64, 68, 71, 74],
    "em": [64, 67, 71],
    "FM": [65, 69, 72],
    "GM": [67, 71, 74],
    "am": [69, 72, 76],
    "AM": [69, 73, 76],
}

sequence = [
    ("CM", duration_whole), ("EM7", duration_whole), ("FM", duration_whole), ("EM", duration_whole), ("am", duration_whole),
    ("am", duration_whole), ("AM", duration_whole), ("dm", duration_whole), ("GM", duration_whole),
    ("CM", duration_whole), ("EM7", duration_whole), ("FM", duration_whole), ("em", duration_whole),
    ("FM", duration_whole), ("DM", duration_whole), ("GM", duration_whole),
    ("CM", duration_eighth*2), ("EM7", duration_eighth*2), ("am", duration_eighth*2), ("FM", duration_eighth*2),
    ("GM", duration_eighth*2), ("am", duration_eighth*2), ("FM", duration_eighth*2), ("GM", duration_eighth*2),
    ("CM", duration_eighth*2)
]

midi = MIDIFile(1)
midi.addTempo(track, 0, tempo)

time = 0
for chord, dur in sequence:
    for note in chord_map[chord]:
        midi.addNote(track, channel, note, time, dur, volume)
    time += dur

with open("lasting_love_chords.mid", "wb") as f:
    midi.writeFile(f)

print("MIDI file created: lasting_love_chords.mid")
