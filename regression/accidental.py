import abjad
import os

extended_quarters = []
for i in range(1, 5):
    extended_quarters += [
        "s" * i + "qs",
        "f" * i + "qf"
    ]


def fix_name(name):
    if name == "sharp":
        return "s"
    elif name == "flat":
        return "f"
    elif name == "+":
        return "qs"
    elif name == "~":
        return "qf"
    if name == "quarter sharp":
        return "qs"
    elif name == "quarter flat":
        return "qf"
    elif name == "three-quarters sharp":
        return "tqs"
    elif name == "three-quarters flat":
        return "tqf"
    elif name == "double sharp":
        return "ss"
    elif name == "double flat":
        return "ff"
    else:
        return name


def accidentals():
    return ["", "+", "~", "qs", "qf",
            "tqs", "tqf", "s", "ss",
            "sss", "ssss", "f", "ff",
            "fff", "ffff"] + extended_quarters


def write_accidentals_new_data():
    print("Generating data for Accidental.new(string)")
    f = open("data/accidental/new.txt", "w")
    for inp in accidentals():
        acc = abjad.Accidental(inp)
        name = fix_name(acc.name)

        f.write(",".join([inp, name, str(acc.semitones)]))
        f.write("\n")
    f.close()


def write_accidentals_new_from_number_data():
    print("Generating data for Accidental.new(number)")
    f = open("data/accidental/new_from_number.txt", "w")
    for inp in range(-10, 11):
        inp = inp/2
        acc = abjad.Accidental(inp)
        name = fix_name(acc.name)

        f.write(",".join([str(inp), name, str(acc.semitones)]))
        if not inp % 1:
            f.write("\n")
            f.write(",".join([str(int(inp)), name, str(acc.semitones)]))
        f.write("\n")
    f.close()


def generate_data():
    os.makedirs("data/accidental/", exist_ok=True)
    write_accidentals_new_data()
    write_accidentals_new_from_number_data()
