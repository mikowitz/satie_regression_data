import abjad
import os
from regression.pitch_class import pitch_classes
from regression.interval import intervals

octaves = [""]
for i in range(1, 5):
    octaves += [
        "'" * i,
        "," * i
    ]


def pitches():
    return [pc + o for pc in pitch_classes() for o in octaves]


def write_pitch_new_data():
    print("Generating data for Pitch.new")
    f = open("data/pitch/new.txt", "w")
    for inp in pitches():
        p = abjad.NamedPitch(inp)
        f.write(":".join([
            inp,
            p.name,
            p.pitch_class.name,
            str(p.number),
            str(p.octave.number)
        ]))
        f.write("\n")
    f.close()


def write_pitch_to_interval_data():
    print("Generating data for Pitch.to_interval")
    f = open("data/pitch/to_interval.txt", "w")
    for inp in pitches():
        p = abjad.NamedPitch(inp)
        i = abjad.NamedInterval(p)
        f.write(":".join([
            inp,
            i.name,
        ]))
        f.write("\n")
    f.close()


def write_pitch_add_data():
    print("Generating data for Pitch.add")
    f = open("data/pitch/add.txt", "w")
    pitch_pairs = [(p1, p2) for p1 in pitches() for p2 in pitches()]
    pairs_len = len(pitch_pairs)
    for (idx, (inp1, inp2)) in enumerate(pitch_pairs):
        p1 = abjad.NamedPitch(inp1)
        p2 = abjad.NamedPitch(inp2)
        p3 = p1 + p2
        f.write(":".join([
            inp1,
            inp2,
            p3.name
        ]))
        f.write("\n")
        if idx > 0 and (idx % 10000 == 0 or idx == pairs_len):
            print("  {}/{}".format(idx, pairs_len))
    f.close()


def write_pitch_subtract_data():
    print("Generating data for Pitch.subtract")
    f = open("data/pitch/subtract.txt", "w")
    pitch_pairs = [(p1, p2) for p1 in pitches() for p2 in pitches()]
    pairs_len = len(pitch_pairs)
    for (idx, (inp1, inp2)) in enumerate(pitch_pairs):
        p1 = abjad.NamedPitch(inp1)
        p2 = abjad.NamedPitch(inp2)
        interval = p1 - p2
        f.write(":".join([
            inp1,
            inp2,
            interval.name
        ]))
        f.write("\n")
        if idx > 0 and (idx % 10000 == 0 or idx == pairs_len):
            print("  {}/{}".format(idx, pairs_len))
    f.close()


def write_pitch_transpose_data():
    print("Generating data for Pitch.transpose")
    f = open("data/pitch/transpose.txt", "w")
    pairs = [(pitch, interval)
             for pitch in pitches()
             for interval in intervals(15)]
    pairs_len = len(pairs)
    for (idx, (inp1, inp2)) in enumerate(pairs):
        pitch = abjad.NamedPitch(inp1)
        interval = abjad.NamedInterval(inp2)
        p2 = pitch.transpose(interval)
        f.write(":".join([
            inp1,
            inp2,
            p2.name
        ]))
        f.write("\n")
        if idx > 0 and (idx % 10000 == 0 or idx == pairs_len):
            print("  {}/{}".format(idx, pairs_len))

    f.close()


def generate_data():
    os.makedirs("data/pitch", exist_ok=True)
    write_pitch_new_data()
    write_pitch_to_interval_data()
    write_pitch_add_data()
    write_pitch_subtract_data()
    write_pitch_transpose_data()
