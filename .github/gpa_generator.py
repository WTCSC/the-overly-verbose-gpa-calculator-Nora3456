print ("Welcome to the GPA calculator!")

num_of_classes = int(input(f"How  many classes do you have?:"))


grades =[(0.0, 4.0)]


if num_of_classes == 5:

    class_1 = float(input("What is your grade in your 1st class?:"))
    class_2 = float(input("What is your grade in your 2nd class?:"))
    class_3 = float(input("What is your grade in your 3rd class?:"))
    class_4 = float(input("What is your grade in your 4th class?:"))
    class_5 = float(input("What is your grade in your 5th class?:"))

if num_of_classes == 6:

    class_1 = float(input("What is your grade in your 1st class?:"))
    class_2 = float(input("What is your grade in your 2nd class?:"))
    class_3 = float(input("What is your grade in your 3rd class?:"))
    class_4 = float(input("What is your grade in your 4th class?:"))
    class_5 = float(input("What is your grade in your 5th class?:"))
    class_6 = float(input("What is your grade in your 6th class?:"))

print ("cal..cu..la...ting... still... calculating... alright, done! Based on {num_of_classes} classes, your GPA is currently: #input GPA#")