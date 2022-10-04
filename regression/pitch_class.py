import abjad
import os
from regression.accidental import (
    accidentals,
    fix_name as acc_name
)

diatonics = ["c", "d", "e", "f", "g", "a", "b"]


def pitch_classes():
    return [d + acc for d in diatonics for acc in accidentals()]


def write_pc_new_data():
    print("Generating data for PitchClass.new")
    f = open("data/pitch_class/new.txt", "w")
    for inp in pitch_classes():
        pc = abjad.NamedPitchClass(inp)
        f.write(":".join([
            inp,
            pc.name,
            str(pc.number),
            accidental_name(pc.accidental.name),
            pc._get_diatonic_pc_name()
        ]))
        f.write("\n")
    f.close()


def write_pc_alteration_data():
    print("Generating data for PitchClass.alteration")
    f = open("data/pitch_class/alteration.txt", "w")
    for inp in pitch_classes():
        pc = abjad.NamedPitchClass(inp)
        f.write(":".join([
            inp,
            str(pc._get_alteration())
        ]))
        f.write("\n")
    f.close()


def write_pc_add_data():
    print("Generating data for PitchClass.add")
    pc_pairs = [(pc1, pc2) for pc1 in pitch_classes()
                for pc2 in pitch_classes()]
    f = open("data/pitch_class/add.txt", "w")
    for (inp1, inp2) in pc_pairs:
        pc1 = abjad.NamedPitchClass(inp1)
        pc2 = abjad.NamedPitchClass(inp2)
        pc3 = pc1 + pc2
        f.write(":".join([
            inp1,
            inp2,
            pc3.name
        ]))
        f.write("\n")
    f.close()


def write_pc_subtract_data():
    print("Generating data for PitchClass.subtract")
    pc_pairs = [(pc1, pc2) for pc1 in pitch_classes()
                for pc2 in pitch_classes()]
    f = open("data/pitch_class/subtract.txt", "w")
    for (inp1, inp2) in pc_pairs:
        pc1 = abjad.NamedPitchClass(inp1)
        pc2 = abjad.NamedPitchClass(inp2)
        ic = pc1 - pc2
        f.write(":".join([
            inp1,
            inp2,
            ic.name
        ]))
        f.write("\n")
    f.close()


# def write_pc_complement_data():
#     print("Generating data for PitchClass.complement")
#     f = open("data/pitch_class/complement.txt", "w")
#     for inp in pitch_classes():
#         pc = abjad.NamedPitchClass(inp)
#         f.write(":".join([
#             inp,
#             pc.name,
#             str(pc.number),
#             accidental_name(pc.accidental.name),
#             pc._get_diatonic_pc_name()
#         ]))
#         f.write("\n")
#     f.close()



def accidental_name(name):
    if name == "natural":
        return ""
    else:
        return acc_name(name)


def generate_data():
    os.makedirs("data/pitch_class", exist_ok=True)
    write_pc_new_data()
    write_pc_alteration_data()
    write_pc_add_data()
    write_pc_subtract_data()
    # write_pc_complement_data()
