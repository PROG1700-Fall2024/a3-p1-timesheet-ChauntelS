#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     W023947
#Student Name:  Chauntel Smith
# YOUR CODE STARTS HERE, each line must be indented (one tab)
#Global Values
#weekDays = [1, 2, 3, 4, 5]   #I could not for the life of me figure out how to not have this as a global
#Users hours per day and stored as list

#Global Values
#weekDays = [1, 2, 3, 4, 5]   #I could not for the life of me figure out how to not have this as a global
#Users hours per day and stored as list
def userHours(weekDays):
    hours = []
    for i in range(len(weekDays)):
        hours.append(float(input(f"Enter hour amount on day #{weekDays[i]} : ")))
    return hours
#Making the math, math 
def calculation(hours):
    maxHours = max(hours)
    totalHours = sum(hours)
    average = totalHours / len(hours)
    indexOfMax = (hours.index(maxHours)+1)  
    return maxHours,totalHours,average,indexOfMax
#Apparently there needs to be anouther math section, because the slack math was not mathing in the first math section
def slackCalculation(hours):
    slackDays = [(i + 1, x) for i, x in enumerate(hours) if x < 7] #<<------- I spend HOURS on this line, I tried google, I tried YouTub, I cound not get it.
    allSlackDays = len(slackDays)                                            #I had to ask A.I. "how to call the values of a list that are less than 7" in order to get it to work
    return slackDays,allSlackDays
#And again another math section
def slackDayAmount(slackDays,allSlackDays):
    if allSlackDays >0:
        print("Days you slacked off (i.e. worked less than 7 hours):")
        for day, hours in slackDays:
            print(f"Day #{day}: {hours} hours")
    else:
        print("Congratulations not one of your work days was less than 7 hours, you work harder than most!")
   
#The main Program
def main():
    weekDays = [1, 2, 3, 4, 5] # NEVER MIND, I GOT IT !
    #Welcome message
    print("Welcome!\nWant to know you Max, Total, Average, or Minimum hours for the work week?\nThis Time sheet will calculate you hours for you!")
    #Loop to restart if the user imputs the wrong values
    while True:             #I was so scared to use a while loop for the first time myself.... and yes the program did get stuck in a loop not once, but twice before I figured it out
        hours = userHours(weekDays)
        maxHours,totalHours,average,indexOfMax = calculation(hours)
        slackDays, allSlackDays = slackCalculation(hours)
        slackDays,allSlackDays
        #Display of final calculations 
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"The most hours worked was on :\nDay #{indexOfMax} when you worked {maxHours} hours.")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"The total number of hours worked was : {totalHours}")
        print(f"The average number of hours worked each day was: {average}")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        print(slackDayAmount(slackDays,allSlackDays)) 
        #Confirming information inputted by user is correct while displaying the final calculations
        correct = input("Are these hours correct? (Y/N): ")     
        if correct.upper() == "Y":
            print("Come back next week!")   #Come back soon message
            break
        else:
            print("Sorry about that, lets try again!")  #Message about trying again
main()      

  
    # YOUR CODE ENDS HERE