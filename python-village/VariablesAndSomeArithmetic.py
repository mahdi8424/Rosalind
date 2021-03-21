
# A function that gets a and b as input

def process(a,b):

    #Setting a and b type to integer
    a,b=int(a),int(b)
    
    # a_p is equal to: a to the power of 2 (a * a)
    a_p=pow(a, 2)

    #b_p is equal to: b to the power of 2 (b * b)
    b_p=pow(b, 2)

    #calculate the result 
    result=a_p + b_p

    #Set the function's output
    return result

#Get values from client
a=input("Enter a number: ")
b=input("Enter b number: ")

#Set a variable value to the result after calculation by process function
answer=process(a,b)
#print the answer
print("The answer is :" + str(answer))
