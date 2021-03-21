
#A function with inputs s and a and b and c and d
def process(s, a, b, c, d):

    #a,b,c,d must be integers so we set the type
    a,b,c,d = int(a),int(b),int(c),int(d)

    #An empty string which we will add values later
    result=''

    #A loop that repeats as long as the numbers of letters between index s[a] to s[b]
    for i in range(b-a+1):
        
        #Includes a letter to result string each time
        result += s[a+i]

    #Add space
    result += " "

    #A loop that repeats as long as the numbers of letters between index s[c] to s[d]
    for i in range(d-c+1):

        result += s[c+i]
        
    #Set output
    return result

#Get inputs from client
s=input("Enter the string text: ")
a=input("Number a: ")
b=input("Number b: ")
c=input("Number c: ")
d=input("Number d: ")
#Find the answer by calling the function
answer=process(s,a,b,c,d)
#Print the answer
print(answer)

"""

This a very simplfied code, u can improve it in a way u want. for example : use arrays and loops and get more than four numbers

"""

