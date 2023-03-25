#I  declare that my work contains no examples of misconduct ,such as plagarism ,or collusion.
#Any code taken from other sources is referenced within my code sollution.
#Student ID-20221168  UOW ID-W1953846
#Author:Dumindu Gamage
#Date-01/12/2022
#PART-2(Extended)
#CODE                                                                                            #EXPLANATION
def validity_number(progression_level=" pass "):                                                 #create a function (validity_number) which accepts one parameter(default=pass)
    while True:                                                                                  # create an infinite loop(Run forever until return user_answer to main_1() function
        try:                                                                                     #start a try block because we have to handle exceptions when user enter a invalid value.
            user_answer=int(input(f"Enter your total{progression_level} credits:"))              #In this line i get user_answer ,convert it to int and store it in user answer
            if(user_answer>=0 and user_answer<=120 and (user_answer%20)==0):                     #If user's input is the correct value range.
               return user_answer                                                                #If user's entered value is incorrect range then return the value to the main_1() function
            else:                                                                                #if user entered out of range then
                print("Out of Range.")                                                           #print the message out of range.
        except ValueError:                                                                       #if valueError occured in the line which we take user's input then 
            print("Integer Required")                                                            #print need an integer.

progression_data=[]                                                                             #create a empty list.because we have to save all progression data.      
def insert_to_the_list(progress_level,pass_pl,defer_pl,fail_pl):                                #create a function named insert_to_the_list.This function will save the all prrogression data.
    progression_data.append([progress_level,pass_pl,defer_pl,fail_pl])                          #In this line ,I hope to append the data we get from user.According to that ,progression_data is a nested list. 

def show_progression_data():                                                           # create a function named show_progression_data.The purpose of creating this function is to print all the progression data in the progression_data list.
    for data_set in progression_data:                                                  # get element(also a list) by element(also a list) from progression_data using enhanced for loop.
        print(data_set[0],"-", data_set[1],",", data_set[2],",", data_set[3])          # this function will simply print all the progression data in the progression_data list.
                                                                                                                              

def validity_total(tot_1):                                                                 #this function will check whether total=120,takes one parameter tot_1.
    if (tot_1==120):                                                                       #if pass+defer+fail is equal to 120 then
        progression_level=sort_progression_level(pass_pl,fail_pl)                          #call sort_progression_outcome function to get the progresssion 
        insert_to_the_list(progression_level, pass_pl, defer_pl, fail_pl)                  #call the function insert_to_the_list which accepts three parameters progression_level,pass_pl,defer_pl,fail_pl.
        print(progression_level)                                                           #print progression_level
    else:                                                                                  #if pass+defer+fail is not equal to 120 then
        print("Total incorrect")                                                           #we display to user "Total is incorrect".
        main_1()                                                                           #takes user to begin the program again.
                                                                            
def sort_progression_level(Pass,fail):                                                    #create a function which accepts three parameters Pass,Defer and Fail..This will sort out the progression level.
    pro_1="Progress"                                                                      #set pro_1 to "Progress"
    pro_2="Progress(module trailer)"                                                      #set pro_2 to "Progress(module trailer)"
    pro_3="Module Retriever"                                                              #set pro_3 to "Module Retriever"
    pro_4="Exclude"                                                                       #set pro_4 to "Exclude" 
    if(Pass==120):                                                                        #if pass==120 then.
        add_progress()                                                                    #call add_progress() function to increment number of students for progress category by 1
        return pro_1                                                                      #return "Progress" to where the function called
    elif(Pass==100):                                                                      #if pass==100 then.
        add_trailer()                                                                     # call add_trailer() function to increment number of students for progress(module trailer) category by 1.
        return pro_2                                                                      #return "Progresss(module trailer)" to where the function called.
    elif(fail>=80):                                                                       #if fail value>=80 then
        add_exclude()                                                                     #call add_Exclude() function to increment number of students for exclude category by 1.
        return pro_4                                                                      #return "Module Retriver" to where the function called
    else:                                                                                 #else it should be definetly "Do not Progress-module retriever."
        add_retriever()                                                                   #call add_retriever() function to increment number of students for "Do not progress -module retriver" category by 1.
        return pro_3                                                                      #return "Do not progress -module retriever." to where the function called.
        
def  main_1():                                                                           #In here i create a function named main_1().Creating this type of function, i hope to handle main tasks in this program.
     global pass_pl,fail_pl,defer_pl                                                     #I make those variables in global scope.because we want to access this variables in validity_total function. 
     pass_pl=validity_number(" PASS")                                                    #call the validity_number function with argument "pass" and store the returned value in pass_pl
     defer_pl=validity_number(" DEFER")                                                  #call the validity_number function with argument "defer" and store the returned value in defer_pl
     fail_pl=validity_number(" FAIL")                                                    #call the validity_number function with argument "fail" and store the returned value in fail_pl
     
     total=pass_pl+defer_pl+fail_pl                                                     #calculate the total of  what user entered.
     validity_total(total)                                                              #call the validity_total function with argument total(we calculated total in previous line.)

def add_progress():                                                                    #create a function to increment progress by 1.
    global progress_cr                                                                 # We use global keyword to read and write progress global variable inside the add_progress() function.
    progress_cr+=1                                                                     # Increment progress_cr by 1.(Inside a function we can only ,access global variables,but can't modify global variables without global keyword.)
def add_trailer():                                                                     #create a function to increment trailer by 1.
    global trailer_cr                                                                  #We use global keyword to read and write trailer_cr global variable inside the add_trailer() function.
    trailer_cr+=1                                                                      #Increment trailer by 1.( Inside a function we can only ,access global variables,but can't modify global variables without global keyword.)
def add_exclude():                                                                     #create a function to increment exclude_cr by 1.
    global exclude_cr                                                                  #we use global keyword to read and write exclude_cr global variable inside the add_exclude() function.
    exclude_cr+=1                                                                      #Increment exclude_cr by 1.
def add_retriever():                                                                   #create a function to increment  retriever_cr by 1.
    global retriever_cr                                                                #We use global keyword to read and write retriever_cr global variable inside the add_retriever() function.
    retriever_cr+=1                                                                    #Increment retriever_cr by 1.                                                                               
    

def prompt_Histogram():                                                                                                                          #create a function to display histogram on the screen.
    print("-----------------------------------------------------------------------------\nHistogram")                                            #print heading named Histogram.
    print(f"Progress : "+ "*" *progress_cr)                                                                                          #print progress_cr category student's count.
    print(f"Trailer : " + "*" *trailer_cr)                                                                                            #print trailer_cr category student's count.
    print(f"Retriever : " + "*" *exclude_cr)                                                                                          #print exclude_cr category student's count.
    print(f"Exclude : " + "*" *retriever_cr)                                                                                        #print retriever_cr  category student's count.
    print(f"\n{sum([progress_cr,trailer_cr,exclude_cr,retriever_cr])} outcomes in total\n------------------------------------------------------------------------------") #print total no of students.

    show_progression_data()                                                                                                                   #call the function show_progression_data.because,we have to print progression data.So,calling this function here able to print all progression data separately.

progress_cr=trailer_cr=exclude_cr=retriever_cr=0                                                                                              # make progress_cr,trailer_cr,retriever_cr,excluded_cr variables with value 0 in global scope.

print("Staff version with histogram\n")                                                                                   #print introduction
while True:                                                                                                                 #infinite while loop to handle entire looping process.
    main_1()                                                                                                                  #call main function.
    user_choice=input("\nWould you like to enter another set of data?\nEnter 'y for yes or 'q' to quit and view results:")#get user option  as his like and store it in user_choice    
    if(user_choice.lower()=='y'):                                                                                           #check the lower case of user's input is equal to "y"
        print("")                                                                                                           #if yes then print blank line to separate it from previous line.
        continue                                                                                                            #go to the begining of the loop to continue normal process again.
    elif(user_choice.lower()=='q'):                                                                                         #check the lower case of user's input is equal to 'q'
        prompt_Histogram()                                                                                                  #if yes then call prompt_histogram  function to dispaly histogram.
        break                                                                                                               #break the loop and stop the program after displaying histogram.
    else:                                                                                                                   #if user's input anything other than 'y' and 'q'
        print("Invalid Option.")                                                                                            #print "Invaid Option."
        break                                                                                                               #break the while loop.

