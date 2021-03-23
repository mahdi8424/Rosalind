"""

Two things must be done, first: Reverse the string
second: Replace the nucleotides with their complements

"""

#Function
def process(dna):

    #Reversing
    reversed_dna = dna[::-1]

    #Replacing loop
    
    #Complements array
    complements={"A":"T","T":"A","G":"C","C":"G"}

    #Emmpty string to store Complemented DNA
    complemented_dna=""
    for i in reversed_dna:

        #Replace each nucleotide with its complement
        complemented_dna += complements[i]

    #Return Complemented DNA
    return complemented_dna

s = input("DNA Code: ")
answer = process(s)
print(answer)
    
    
