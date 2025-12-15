import CGRtools

### A module for the definition of reactive and nonreactive graphs in a chemical reaction, specifically in the context of an enzyme active site

class MolecularGraph():
    def __init__(self, atoms:list, bonds:list, energies:list):
        self.atoms = atoms
        self.bonds = bonds
        self.energies = energies
        return

class ReactiveGraph(MolecularGraph):
    def __init__(self):
        pass

class BindingGraph(MolecularGraph):
    def __init__(self):
        pass

class SplitSite():
    def __init__(self, rg:ReactiveGraph, nrg:BindingGraph) -> tuple:
        self.rg = rg
        self.nrg = nrg

        self._compute_sites()
        return (self.reactive_sites, self.binding_sites)

    def _split_sitedness(self):
        # Computes interactions between the reactive and nonreactive graphs and their overlap
        pass

    def _compute_sites(self):
        # Assigns atoms to both the reactive and nonreactive graphs, AKA reactive or binding sites

        self.r_sub = None
        self.b_sub = None
        self.r_enz = None
        self.b_enz = None

        self.reactive_sites = (self.r_sub, self.r_enz)
        self.binding_sites = (self.b_sub, self.b_enz)
        return
