import sys
from normadresse import abrev
import json

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("""Usage:  normjson.py
        cat test.json | python normjson.py name afnor""")
    else:
        for j in sys.stdin.readlines():
            t = json.loads(j)
            if sys.argv[1] in t and t['type'] != 'municipality':
                t[sys.argv[2]] = abrev(t[sys.argv[1]][0]).upper()
            print(json.dumps(t))
