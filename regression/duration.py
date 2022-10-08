import abjad
import os


def durations(range_max=100):
    return [(n, d)
            for n in range(-range_max, range_max)
            for d in range(-range_max, range_max)]


def write_duration_new_data():
    print("Generating data for Duration.new")
    f = open("data/duration/new.txt", "w")
    for (n, d) in durations():
        if d != 0:
            dur = abjad.Duration(n, d)
            f.write(":".join([
                str(n),
                str(d),
                str(dur.numerator),
                str(dur.denominator)
            ]))
            f.write("\n")
    f.close()


def write_duration_printable_data():
    print("Generating data for Duration.printable")
    f = open("data/duration/printable.txt", "w")
    for (n, d) in durations():
        if d != 0:
            dur = abjad.Duration(n, d)
            f.write(":".join([
                str(n),
                str(d),
                str(dur.is_assignable)
            ]))
            f.write("\n")
    f.close()


def write_duration_add_data():
    print("Generating data for Duration.add")
    f = open("data/duration/add.txt", "w")
    pairs = [(i1, i2) for i1 in durations(15) for i2 in durations(15)]
    pairs_len = len(pairs)
    print(pairs_len)
    for (idx, ((n, d), (n2, d2))) in enumerate(pairs):
        if d != 0 and d2 != 0:
            dur1 = abjad.Duration(n, d)
            dur2 = abjad.Duration(n2, d2)
            dur_sum = dur1 + dur2
            f.write(":".join([
                str(n),
                str(d),
                str(n2),
                str(d2),
                str(dur_sum.numerator),
                str(dur_sum.denominator)
            ]))
            f.write("\n")
        if idx > 0 and (idx % 10000 == 0 or idx == pairs_len):
            print("  {}/{}".format(idx, pairs_len))
    f.close()


def write_duration_subtract_data():
    print("Generating data for Duration.subtract")
    f = open("data/duration/subtract.txt", "w")
    pairs = [(i1, i2) for i1 in durations(15) for i2 in durations(15)]
    pairs_len = len(pairs)
    print(pairs_len)
    for (idx, ((n, d), (n2, d2))) in enumerate(pairs):
        if d != 0 and d2 != 0:
            dur1 = abjad.Duration(n, d)
            dur2 = abjad.Duration(n2, d2)
            dur_diff = dur1 - dur2
            f.write(":".join([
                str(n),
                str(d),
                str(n2),
                str(d2),
                str(dur_diff.numerator),
                str(dur_diff.denominator)
            ]))
            f.write("\n")
        if idx > 0 and (idx % 10000 == 0 or idx == pairs_len):
            print("  {}/{}".format(idx, pairs_len))
    f.close()


def generate_data():
    os.makedirs("data/duration", exist_ok=True)
    write_duration_new_data()
    write_duration_printable_data()
    write_duration_add_data()
    write_duration_subtract_data()
