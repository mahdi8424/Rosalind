#Proccess function
def process(dna):

    #Use replace() method to change all T nucleotides to U
    rna=dna.replace("T","U")

    #Return generated rna code
    return rna

#Get DNA code from client
dna=input("Write the DNA code: ")
#Call the process function
answer=process(dna)
#Print answer
print(answer)
