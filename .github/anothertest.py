print ("Welcome to the GPA calculator!")

num_of_classes = int(input(f"How many classes do you have?: "))

def validate_num_of_classes():
    while num_of_classes != (int):
        if num_of_classes != (int):
            print(f"{num_of_classes} is not a valid answer.")
            return False
        else:
            break

#if num_of_classes != (int):
    #print(f"{num_of_classes} is not a valid answer.")
#else:
   # False#

   # if not isinstance(value, (int, float)):
    #    print(f'{value} is not a valid answer.')
       # return False
   # else:
   #     return True
      

grades = []


for i in range(num_of_classes):
    while True:
        try:
            grade = float(input(f"What is your grade in class {i + 1}: "))
            if 0 <= grade <= 4:
               grades.append(grade)
               print (f"You entered: {grade}")
               break
            else:
                print("Grade must be between 0.0 and 4.0. Make sure to use only numbers, no extra characters or letters. Try again.")

        except ValueError:
            print ("Grade must be between 0.0 and 4.0. Make sure to use only numbers, no extra characters or letters. Try again.")

        11
def GPA():
    sum_of_grades = sum(grades) / len(grades)
    rounded_sum = round(sum_of_grades, 2)
    return rounded_sum
    
    
print (f"cal..cu..la...ting... still... calculating... alright, done! Based on {num_of_classes} classes, your GPA is currently: {GPA()}")
    
# (Trying to show what your GPA means (good, bad, etc.))

#if GPA <= 3.5 and GPA >= 4:
 #   print (f"Result: you have a great GPA ({GPA()})!")
#if GPA <= 3 and GPA >= 3.5:
    #print (f"Result: You have a sufficient GPA ({GPA()})!")

#if 2 <= GPA <= 3:
   # print (f"Result: you have an ok GPA ({GPA()})!")
#if 0 <= GPA <= 2:
   # print (f"Result: you have a poor GPA ({GPA()})!")


# print (f"Do you want to focus on 1; the first semester, or 2: the second semester?: ")


while True:
        try:
            GPA_goal = float(input(f"What is your GPA goal?: "))
            if 0 <= GPA_goal <= 4:
               break
            else:
                print("Your GPA goal must be between 0.0 and 4.0. Make sure to use only numbers, no extra characters or letters. Try again.")

        except ValueError:
            print ("Your GPA goal must be between 0.0 and 4.0. Make sure to use only numbers, no extra characters or letters. Try again.")

if GPA_goal == GPA:
    print(f"Congratulations, you are already at your GPA goal ({GPA()})!")


goal_calculated = min(grades) 



def GPA_goal_calculated():

  #  grades.replace(min(grades), 4.0)
    old_sum = min(grades)
    new_sum = 4
    try:
        index = grades.index(old_sum)
        grades[index] = new_sum
    except ValueError:
        print(f"Try again.")

    sum_of_grades = sum(grades) / len(grades)
    rounded_sum = round(sum_of_grades, 2)
    return rounded_sum



print(f" If you changed your lowest grade ({goal_calculated})to a 4.0, your new GPA would be {GPA_goal_calculated()}")


