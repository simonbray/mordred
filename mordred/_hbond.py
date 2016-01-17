from ._base import Descriptor
from rdkit.Chem import rdMolDescriptors


class HBondBase(Descriptor):
    explicit_hydrogens = False
    require_connected =False


class HBondAcceptor(HBondBase):
    r'''
    hydrogen bond acceptor descriptor

    Returns:
        int: hydrogen bond acceptor count
    '''

    def __str__(self):
        return 'nHBAcc'

    def calculate(self, mol):
        return rdMolDescriptors.CalcNumHBA(mol)


class HBondDonor(HBondBase):
    r'''
    hydrogen bond donor descriptor

    Returns:
        int: hydrogen bond donor count
    '''

    def __str__(self):
        return 'nHBDon'

    def calculate(self, mol):
        return rdMolDescriptors.CalcNumHBD(mol)
