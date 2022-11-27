from CGRtools.containers import *

class Molecule():
    def __init__(self, molecule_container:MoleculeContainer=None):
        self._container = molecule_container

    def __repr__(self):
        print(self._container)

class Catalyst(Molecule):
    def __init__(self):
        super().__init__()
