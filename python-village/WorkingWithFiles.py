#Define a function with the input file name 
def process(fname):

    #Open a file named result to write the result text in it(this file will be created in the app's directory)
    result=open("result.txt","w")
    #Define a varible and increase it in loop each round, this shows the line's number
    x=0
    #This loop reads the file (fname) and store each line in (file) variable
    for file in open(fname,'r'):

        #Check if the line's number (x) is odd 
        if x%2==1:

            #Write the line in  reslt.txt file
            write=result.write(file)
        #Increase the (x) which shows the line's number, we are going to next line...
        x=x+1

    #Now let's close the files we opened...
    result.close()
    #Return 1 ot true to tell that our function did it's job!
    return 1

#Get input file's name
fname=input("Write file's name (with extention included): ")
#Call the function
answer=process(fname)
#Check if the function returns true or 1
if answer:
    print("check the result.txt file in the app's directory...")
    
