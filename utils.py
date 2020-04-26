def complement_dna(input_sequence:str):
    """Returns complementary nucleotide sequence for dna string

    Arguments:
        input_sequence {str} -- dna string to complement

    Returns:
        str -- dna complement
    """    
    dna_complementary_mappings = {"T":"A", "C":"G", "G":"C","A":"T"}
    complement_list = [dna_complementary_mappings[x] for x in input_sequence]
    return "".join(complement_list)
