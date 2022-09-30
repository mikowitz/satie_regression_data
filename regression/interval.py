import abjad
import os
from .helpers import (
    qualities_for,
    polarities,
    quartertones
)


def intervals(max_size=50):
    return [p + qual + q + str(size)
            for size in range(1, max_size)
            for qual in qualities_for(size)
            for p in polarities for q in quartertones]


def write_interval_new_data():
    print("Generating data for Interval.new")
    f = open("data/interval/new.txt", "w")
    for inp in intervals(15):
        i = abjad.NamedInterval(inp)
        f.write(" ".join([
            inp,
            i.interval_class.name,
            i.name,
            str(i.number),
            str(i.octaves),
            i.quality,
            str(i.direction_number),
            str(i.semitones),
            str(i.staff_spaces)
        ]))
        f.write("\n")
    f.close()


def generate_data():
    os.makedirs("data/interval", exist_ok=True)
    write_interval_new_data()
