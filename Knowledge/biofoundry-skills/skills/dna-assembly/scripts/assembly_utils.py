from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq

def calculate_tm(sequence_str):
    """Calculates melting temperature using Nearest-Neighbor method."""
    seq = Seq(sequence_str)
    return mt.Tm_NN(seq)

def find_restriction_sites(sequence_str, enzyme_name):
    """Finds restriction sites for a given enzyme."""
    from Bio import Restriction
    enzyme = getattr(Restriction, enzyme_name)
    seq = Seq(sequence_str)
    return enzyme.search(seq)
