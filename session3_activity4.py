# Activity 4
day = int(input("Enter the day: ")) #in this line prompts the user to enter the day.
month = int(input("Enter the month: ")) #in this line prompts the user to enter the month.
year = int(input("Enter the last two digits of the year: ")) #in this line prompts the user to enter the last two digits of the year.
                    #also, for all of them im using input function because it read as a string and int function is converting to an integer
if day * month == year: #in this line this condition checks if the product of the day and month is equal to year.
    print("The date is a magic date.") #if the condition shown is true, it will print as 'the date is a magic date.'
else: #in this line, shows if the condition given isn't true.
    print("The date is not a magic date.") #in this line, it prints the condition that is false, so it will print as 'The date is not a magic date.'
