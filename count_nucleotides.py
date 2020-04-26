from Bio import SeqIO
import pprint
from typing import List, Dict
pp = pprint.PrettyPrinter(indent=4)
p=pp.pprint
letters = ["A","C","G","T"]
    
def count_nucleotides(genomes:Dict(str)):

    counts ={
        genome_name:{letter:genomes[genome_name].count(letter) for letter in letters}
        for genome_name in genomes.keys()} 
    return counts


hsapiens = next(SeqIO.parse("genomes/human-PrR1jPIaAG.fasta", "fasta")).seq
pfalciparum = next(SeqIO.parse("genomes/mosquito-AK2jNK0ahq.fasta", "fasta")).seq
agambiaeas = next(SeqIO.parse("genomes/plasmodium-RkREaPiyih.fasta", "fasta")).seq
genomes = {"hsapiens":hsapiens, "pfalciparum":pfalciparum, "agambiaeas":agambiaeas}

print("COUNTING")
counts ={
        genome_name:{letter:genomes[genome_name].count(letter) for letter in letters}
        for genome_name in genomes.keys()} 
p(counts)