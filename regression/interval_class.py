import abjad
import os
from .helpers import (
    qualities_for,
    polarities,
    quartertones
)


def interval_classes(max_size=50):
    return [p + qual + q + str(size)
            for size in range(1, max_size)
            for qual in qualities_for(size)
            for p in polarities for q in quartertones]


def ic_pairs(max_size=50):
    return [(ic, ic2)
            for ic in interval_classes(max_size)
            for ic2 in interval_classes(max_size)]


def write_interval_class_new_data():
    print("Generating data for IntervalClass.new")
    f = open("data/interval_class/new.txt", "w")
    for inp in interval_classes(20):
        ic = abjad.NamedIntervalClass(inp)
        f.write(" ".join([inp, ic.name, str(ic.number),
                ic.quality, str(ic.direction_number)]))
        f.write("\n")
    f.close()


def write_interval_class_add_data():
    print("Generating data for IntervalClass.add")
    f = open("data/interval_class/add.txt", "w")
    pairs = ic_pairs(11)
    pairs_len = len(pairs)
    for (idx, (in1, in2)) in enumerate(pairs):
        ic = abjad.NamedIntervalClass(in1) + abjad.NamedIntervalClass(in2)
        f.write(" ".join([in1, in2, ic.name, str(ic.number),
                ic.quality, str(ic.direction_number)]))
        f.write("\n")
        if idx > 0 and (idx % 10000 == 0 or idx == pairs_len):
            print("  {}/{}".format(idx, pairs_len))
    f.close()


def write_interval_class_subtract_data():
    print("Generating data for IntervalClass.subtract")
    f = open("data/interval_class/subtract.txt", "w")
    pairs = ic_pairs(11)
    pairs_len = len(pairs)
    for (idx, (in1, in2)) in enumerate(pairs):
        ic = abjad.NamedIntervalClass(in1) - abjad.NamedIntervalClass(in2)
        f.write(" ".join([in1, in2, ic.name, str(ic.number),
                ic.quality, str(ic.direction_number)]))
        f.write("\n")
        if idx > 0 and (idx % 10000 == 0 or idx == pairs_len):
            print("  {}/{}".format(idx, pairs_len))
    f.close()


def generate_data():
    os.makedirs("data/interval_class/", exist_ok=True)
    write_interval_class_new_data()
    write_interval_class_add_data()
    write_interval_class_subtract_data()
