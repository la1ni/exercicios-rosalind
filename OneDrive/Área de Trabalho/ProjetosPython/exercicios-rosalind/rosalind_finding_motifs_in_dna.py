import re
from funções_rosalind import dividing_strings_in_sequences
string_as_rosalind = """
GTCTCGAGTCTCGATGGTGTCTCGAGTCTCGAGTCTCGAGGTCTCGAGTCTCGACCAGTCTCGAGTCTCGAAAGGTCTCGAGTCTCGAAGGTCTCGACGGTCTCGAGTCTCGAAGGTCTCGACTGGTGTCTCGAGGCGAAGTCTCGAGAGGTCTCGAGTAACTTCTCGTCTCGAAGCTTTGCGTCTCGACATGTCTCGAAGGATGTCTCGACCTTGTCTCGATCGCGTCTAGTCTCGATGTGTGTCTCGAGTCGTCTCGAGTCTCGATGTCTCGAAGTCTCGACAATGAGGTCGTCTCGACGTAAAGTCTCGAACGTCTCGAGGGCGACTTAGTCACCGTCTCGACCCGTCTCGAGTCTCGAGTCTCGAGGTCTCGAAGTCTCGAGCAGTCTCGATCTCGTCTCGAGGGCTGCGTCTCGACGCTAGAAGCCCGTGTCTCGAAGTCTCGAGGTCTCGAACTGTCTCGAGTCTCGAGGTCTCGAGTCTCGAGGTCTCGAGTCTCGAGTCTCGAAGTCTCGATTAGGCGTCTCGAGGTCTCGATTCGTCTCGAACGTGACTAGTCTCGAAGTCTCGACGTGTCTCGAAAGTCTCGAGTCTCGAGTCTCGAGTCTCGAACGTCTCGAGAGTGATTAGTCTCGAGTCTCGAGTGTCTCGATGTCCTGTCTCGATCACGTCTCGAGTCTCGAGTCTCGAGTCTCGATACGTCTCGAGGTCTCGAGTCTCGATCCGTCTCGAAGGTCTCGATCTCTAGTCTCGATGTGGCGTCTCGAAGGTGTCTCGAGCGGTTGTCTCGAGTCTCGAGTCTCGAGTCTCGATCGCCAGTCTCGAGTCTCGATGTCTCGAAGTCTCGAGTCTCGACTGCGTCTCGAGCTAAGTCTCGA
GTCTCGAGT
"""
sequence_and_motif = dividing_strings_in_sequences(string_as_rosalind)
sequence = sequence_and_motif[0]
ranges_de_leitura = []
tamanho_da_seq_busca = len(sequence_and_motif[1])
quadra =''

for item in sequence_and_motif[0]:
    if len(sequence) == len(sequence_and_motif[0]):
        for indice, valor in enumerate(sequence):
            if indice < tamanho_da_seq_busca:
                quadra = quadra + valor
        ranges_de_leitura.append(quadra)
        quadra = ''
    if len(sequence) > tamanho_da_seq_busca:
        sequence = sequence.removeprefix(sequence[0])
        for indice_, valor_ in enumerate(sequence):
            if indice_ < tamanho_da_seq_busca:
                quadra = quadra + valor_
        ranges_de_leitura.append(quadra)
        quadra = ''

for i, divisao in enumerate (ranges_de_leitura):
    if divisao == sequence_and_motif[1]:
        print(i+1, end=' ')

