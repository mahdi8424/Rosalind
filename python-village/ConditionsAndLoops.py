#Function to process input data
def process(a,b):

    #a and b must be integers
    a,b = int(a),int(b)
    
    #Loop that repeats from a to b and each time  increases +1
    #This variable stores sumed numbers
    number=0
    while a<=b:

        #Check if the number is odd
        if a%2==1:
            number = number + a
        #Increase (a) variable +1 each time, otherwise the loop will never end!
        a=a+1
    
    return number


#Get data from client
a=input("Enter a integer: ")
b=input("Enter b integer: ")
#Call the process function with given numbers and store return value in  result variable
result=process(a,b)
#Print result
print(result)
