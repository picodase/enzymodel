from molecule import Molecule, Catalyst

class ChemicalReaction():
    def __init__(self, reactants:list, products:list, scheme, catalysts:list=None, temperature:float=298.0, K:float=1, dG:float=0.0, pH:float=7.0) -> None:
        self.reactants = reactants
        self.products = products
        self.scheme = scheme
        self.catalysts = catalysts
        self.temperature = temperature
        self.K = K
        self.dG = dG
        self.pH = pH
    
    def _binding_graph(self):
        return

    def _reaction_graph(self):
        return

    def __isequal__():
        pass

    def __isequalcorereaction__():
        pass

    def _reverse_reaction():
        pass

class ElementaryReaction(ChemicalReaction):

    def __init__() -> None:
        super().__init__()
        pass

class OverallReaction(ChemicalReaction):

    def __init__(self, elementary_reactions:list):
        super().__init__()
        self.elementary_reactions = elementary_reactions
        self._overall_reaction = None
    
    def _overall_reaction(self):
        """
        Sum of all elementary reactions
        """
        if self._overall_reaction == None:
            self._overall_reaction = sum(self.elementary_reactions)
        return self._overall_reaction

    def _reaction_graph(self):
        if self._reaction_graph == None:
            self._reaction_graph = sum(self._overall_reaction._reaction_graph)
        return self._reaction_graph

    def _binding_graph(self):
        if self._binding_graph == None:
            self._binding_graph = sum(self._overall_reaction._binding_graph)
        return self._binding_graph