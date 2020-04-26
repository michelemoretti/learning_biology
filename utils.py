def complement_dna(input_sequence: str):
    """Returns complementary nucleotide sequence for dna string

    Arguments:
        input_sequence {str} -- dna string to complement

    Returns:
        str -- dna complement
    """
    dna_complementary_mappings = {"T": "A", "C": "G", "G": "C", "A": "T"}
    complement_list = [dna_complementary_mappings[x] for x in input_sequence]
    return "".join(complement_list)


def reverse_complement_dna(input_sequence):
    complement = complement_dna(input_sequence)
    reverse_complement = complement[::-1]
    return reverse_complement


codon_to_AA = {
    "AUG": "M",
    "GCG": "A",
    "UCA": "S",
    "GAA": "E",
    "GGG": "G",
    "GGU": "G",
    "AAA": "K",
    "GAG": "E",
    "AAU": "N",
    "CUA": "L",
    "CAU": "H",
    "UCG": "S",
    "UAG": "STOP",
    "GUG": "V",
    "UAU": "Y",
    "CCU": "P",
    "ACU": "T",
    "UCC": "s",
    "CAG": "Q",
    "CCA": "P",
    "UAA": "STOP",
    "AGA": "R",
    "ACG": "T",
    "CAA": "Q",
    "UGU": "C",
    "GCU": "A",
    "UUC": "F",
    "AGU": "S",
    "AUA": "I",
    "UUA": "L",
    "CCG": "P",
    "AUC": "I",
    "UUU": "F",
    "CGU": "R",
    "UGA": "STOP",
    "GUA": "V",
    "UCU": "S",
    "CAC": "H",
    "GUU": "V",
    "GAU": "D",
    "CGA": "R",
    "GGA": "G",
    "GUC": "V",
    "GGC": "G",
    "UGC": "C",
    "CUG": "L",
    "CUC": "L",
    "CGC": "R",
    "CGG": "R",
    "AAC": "N",
    "GCC": "A",
    "AUU": "I",
    "AGG": "R",
    "GAC": "D",
    "ACC": "T",
    "AGC": "S",
    "UAC": "Y",
    "ACA": "T",
    "AAG": "K",
    "GCA": "A",
    "UUG": "L",
    "CCC": "P",
    "CUU": "L",
    "UGG": "W",
}