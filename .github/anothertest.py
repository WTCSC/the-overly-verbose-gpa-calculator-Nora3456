print ("Welcome to the GPA calculator!")

# Validates the user input on how many classes they have.
while True:
    try:
        num_of_classes = int(input(f"How many classes do you have?: "))
        if 1 <= num_of_classes <= 10:
            break

        elif num_of_classes >= 10:
            print(f"{num_of_classes} classes...? Let's be more realistic.")
        elif num_of_classes != 1 <= num_of_classes <= 10:
            print(f"Only input the number of classes you have, no letters or extra characters.")
        elif num_of_classes == 0:
            print (f"You have {num_of_classes} classes...? What are you doing here than?")

    except ValueError:
        print ("Only input the number of classes you have, no letters or extra characters.")

      

grades = [] #stores the list for grades


# returns the question of grades in classes, based on the number of classes the user input, as well as validates the answers to the grade in classes question.
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


# how the GPA is calculated based on the average grades between classes. 
def GPA():
    sum_of_grades = sum(grades) / len(grades)
    rounded_sum = (round(sum_of_grades, 2))
    return rounded_sum


    
print (f"cal..cu..la...ting... still... calculating... alright, done! Based on {num_of_classes} classes, your GPA is currently: {GPA()}")
    

# (Trying to show what your GPA means (good, bad, etc.))

if 3.5 <= GPA() <= 4 :
    print (f"Result: you have a great GPA ({GPA()})!")
if 3 <= GPA() <= 3.5:
    print (f"Result: You have a sufficient GPA ({GPA()})!")

if 2 <= GPA() <= 3:
    print (f"Result: you have an ok GPA ({GPA()}).")
if 0 <= GPA() <= 2:
    print (f"Result: you have a poor GPA ({GPA()}).")

# function for slicing semester 1, and its average GPA.
def semester_1_GPA():
    grading_semester = len(grades) // 2
    final = grades[:grading_semester]

    sum_of_grades = sum(final) / len(final)
    rounded_sum = (round(sum_of_grades, 2))

    return rounded_sum
    
# function for slicing semester 2, and its average GPA.
def semester_2_GPA():
    grading_semester = len(grades) // 2
    final = grades[grading_semester:]

    sum_of_grades = sum(final) / len(final)
    rounded_sum = (round(sum_of_grades, 2))

    return rounded_sum

#Asking user what semester they want to focus on, and see GPA for.
if num_of_classes > 1:
    semester_analysis = input(f"Do you want to analyze 1; your first semester GPA, or 2: your second semester GPA?: ")
    if semester_analysis == '1':
        semester_1 = print (f"Your first semester GPA was: {semester_1_GPA()}")

    if semester_analysis == '2':
        semester_2 = print (f"Your second semester GPA was: {semester_2_GPA()}")
        if semester_2_GPA() > GPA():
            print("Yay! Your second semester GPA is higher than your overall GPA, keep up the good work!")



# Validates the users input for what their goal GPA is. 
while True:
        try:
            GPA_goal = float(input(f"What is your GPA goal?: "))
            if 0 <= GPA_goal <= 4:
                break
            elif GPA_goal < GPA():
                print(f"Your GPA goal should be higher than your current GPA, set your standards higher.")
            elif GPA_goal != (float):
                    print(f"Your input should be only numbers, no extra characters or letters. Try again. ")
        except ValueError:
                print ("Your GPA goal must be between 0.0 and 4.0. Make sure to use only numbers, no extra characters or letters. Try again.")
            


if GPA_goal == GPA():
    print(f"Congratulations, you are already at your GPA goal ({GPA()})!")
    

if GPA_goal != GPA():

    goal_calculated = min(grades)


    # What your new GPA would become if one grade in a class was improved to a 4.0
    def GPA_goal_calculated():
        old_sum = grades[0]
        new_sum = 4.0

        index = grades.index(old_sum)
        grades[index] = new_sum

        sum_of_grades = sum(grades) / len(grades)
        rounded_sum = round(sum_of_grades, 2)
        return rounded_sum


    print(f"The following lines will tell you what your GPA would become if a grade in a class was raised to a 4.0, (only one classes grade is raised to a 4.0 each line).")


# What the new GPA would become if only 1 grade was improved to a 4.0
    for i in range(num_of_classes):
        while True:
            try:
                if GPA_goal:
                    grades.append(i)
                    print (f"If your grade in class {i + 1} ({grades[i]}) was raised to a 4.0, your new GPA would be:{GPA_goal_calculated()}.")
                break

            except ValueError:
                print ("Try again.")

    if GPA_goal_calculated() >= GPA_goal:
        print(f"By changing just one of your classes grades to a 4.0, your goal GPA would be achieved!")
    if GPA_goal_calculated() <= GPA_goal:
        print(f"You will need to improve your grades in multiple classes in order to achieve your goal GPA.")



