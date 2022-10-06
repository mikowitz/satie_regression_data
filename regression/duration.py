import abjad
import os

durations = [(n, d)
             for n in range(-100, 100)
             for d in range(-100, 100)]


def write_duration_new_data():
    print("Generating data for Duration.new")
    f = open("data/duration/new.txt", "w")
    for (n, d) in durations:
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


def generate_data():
    os.makedirs("data/duration", exist_ok=True)
    write_duration_new_data()
