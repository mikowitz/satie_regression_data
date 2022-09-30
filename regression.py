import sys

import regression.interval_class as interval_class
import regression.interval as interval
import regression.pitch_class as pc
import regression.accidental as accidental
import regression.pitch as pitch


def should_generate(name):
    return name in sys.argv or "everything" in sys.argv


if __name__ == "__main__":

    if should_generate("interval-class"):
        print("Generating data for IntervalClass")
        interval_class.generate_data()

    if should_generate("interval"):
        print("Generating data for Interval")
        interval.generate_data()

    if should_generate("accidental"):
        print("Generating data for Accidental")
        accidental.generate_data()

    if should_generate("pitch-class"):
        print("Generating data for PitchClass")
        pc.generate_data()

    if should_generate("pitch"):
        print("Generating data for Pitch")
        pitch.generate_data()
