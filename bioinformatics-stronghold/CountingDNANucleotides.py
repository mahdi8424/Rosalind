#Define a function to count nucleotids
def process(s):

    #Use count() function to get the number of each nucleotid and store them in a dictionary
    result={}
    result["A"]=s.count("A")
    result["C"]=s.count("C")
    result["G"]=s.count("G")
    result["T"]=s.count("T")

    #Return the values
    return result

#Get string from clinet
s=input("What is the string? :")

#Call the written function and store output in a variable
answer=process(s)

#Print the answer in a format that question asks ([!] space is a string, for connecting we need to set type of the integers to string)
print(str(answer["A"]) + ' ' + str(answer["C"]) + " " + str(answer["G"]) + ' ' + str(answer["T"]))
