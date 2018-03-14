import sys
import csv
from normadresse import abrev

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("""Usage:  normstream.py
        cat test.csv | python normstream.py nom nom_afnor""")  # noqa
    else:
        input = csv.DictReader(sys.stdin)
        output = csv.DictWriter(sys.stdout, input.fieldnames)
        output.writeheader()
        for t in input:
            t[sys.argv[2]] = abrev(t[sys.argv[1]]).upper()
            output.writerow(t)
