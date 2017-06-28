# normadresse

Module python pour abréger des libellés d'adresses en suivant la norme NF Z10-011.

## Installation

git clone
pip install -r requirements.txt

## Utilisation

### En ligne de commande:

python normadresse.py 'BOULEVARD DU MARECHAL JEAN MARIE DE LATTRE DE TASSIGNY'
echo 'BOULEVARD DU MARECHAL JEAN MARIE DE LATTRE DE TASSIGNY' | python normadresse.py
cat libelles.txt | python normadresse.py

### Comme module python:

import normadresse

print(abrev('BOULEVARD DU MARECHAL JEAN MARIE DE LATTRE DE TASSIGNY'))
