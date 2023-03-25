#I  declare that my work contains no examples of misconduct ,such as plagarism ,or collusion.
#Any code taken from other sources is referenced within my code sollution.
#Student ID-20221168  UOW ID-W1953846
#Date-18/11/2022
def validity_number(progression_level="Pass"):                                                     #create a function (validity_number) which accepts one parameter(default=pass)
    while True:                                                                                    #create an infinite loop(Run forever until return user_answer to main_1() function
        try:                                                                                       #start a try block because we have to handle exceptions when user enter a invalid value
            user_answer=int(input(f"Please enter your credits at pass {progression_level} : "))    #get user_answer ,convert it to int,store it in user_answer
            if(user_answer>=0 and user_answer<=120 and (user_answer%20)==0):                       #check whether user's input is the correct value range.
                return user_answer                                                                 #If user's entered value is incorrect range then return the value to the main_1() function
            else:                                                                                  #if user entered out of range then
                print("Out of Range.")                                                             #print the message out of range.
        except ValueError:                                                                         #if valueError occured in the line which we take user's input then 
         print("Integer Required")                                                                 #print need an integer 

def validity_total(tot_1):                                                                         #this function will check whether total=120,takes one parameter-total.
    if (tot_1==120):                                                                               #if pass+defer+fail is equal to 120 then
        progression_level=sort_progression_level(pass_pl,fail_pl)                                  #call sort_progression_outcome function to get the progresssion 
        print(progression_level)                                                                   #print total is incorrect
    else:                                                                                          #print the progress level
        print("Total incorrect")                                                                   #if total is not equal to 120 
        main_1()                                                                                   #takes user to begin the program.

def sort_progression_level(Pass,fail):                         
    pro_1="Progress"                                                                              #set pro_1 to "Progress"
    pro_2="Progress(module trailer)"                                                              #set pro_2 to "Progress(module trailer(module trailer)"
    pro_3="Module Retriever"                                                                      #set pro_3 to "Module Retriever"
    pro_4="Exclude"                                                                               #set pro_4 to "Exclude"
    if(Pass==120):                                                                                #if pass=120 then
        return pro_1                                                                              #return "Progress(module trailer)" to where the function called 
    elif(Pass==100):                                                                              #if pass=100 then
        return pro_2                                                                              #return "Progress(module Retriever") to where the function callled 
    elif(fail>=80):                                                                               #if fail value>=80 then 
        return pro_4                                                                              #return "Exclude"to where the function called.
    else:                                                                                         #else it should be definetly "Do not Progress-module retriever."
        return pro_3                                                                              #return "Do not Progress-module retriever."

def main_1():                                                                                     #In here, I create a main_1() function to handle main tasks in the program.
    global pass_pl,fail_pl                                                                        #I make those variables in global scope because I want to access these variables in check validity_total function. 
    pass_pl=validity_number("pass")                                                               #call the validity_number function with argument "pass" and store the returned value in pass_pl
    defer_pl=validity_number("defer")                                                             #call the validity_number function with argument "defer" and store the returned value in  defer_pl
    fail_pl=validity_number("fail")                                                               #call the validity_number function with argument "fail" and store the returned value in fail_pl

    total=pass_pl+defer_pl+fail_pl                                                                # calculate the total of  what user eneterd  
    validity_total(total)                                                                         #call the validity_total function with the argument total(This is calculated in previous line.)

main_1()                                                                                          #call the main function(This is the starting point of program.)

