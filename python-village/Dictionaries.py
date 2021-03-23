#Define a function which get (s) value as string
def process(s):

    #Change the string to an array which includes the string(s) words separately
    s_array = s.split(" ")
    result={}
    #This loops reads the array, each word per round and stores that word in i variable
    for i in s_array:

        #Count the number of (i) word in the array
        count=s_array.count(i)
        #Add the word(i) as key and word's repeated times(count) as value to result dictionary
        result[i]=count

    #Return the result dictionary
    return result

#Get text from client
s=input("Enter the text:([!] There is a new line at the end of the file, do not copy that!) ")
#Call the function which return dictionary and store it in (answer)
answer=process(s)
#Open a file named result.txt to store the answer
file=open("result.txt","w")
#Use a loop to print the returned dictionary
for key,value in answer.items():

    #Set value type to string because we can't connect a string to integer
    string = key + ' ' + str(value)
    #Write the string in file
    file.write(string + "\n")
print("Added to file result.txt")
#Close the file we opened
file.close()
"""

You can change this in other ways to make it better

"""
