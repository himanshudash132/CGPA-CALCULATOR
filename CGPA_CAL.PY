def grade(x):
    if x >= 90:
        return 10
    elif 80 <= x <= 89:
        return 9
    elif 70 <= x <= 79:
        return 8
    elif 60 <= x <= 69:
        return 7
    elif 50 <= x <= 59:
        return 6
    elif 40 <= x <= 49:
        return 5
    else:
        return 2

def calculate_sgpa(credits, total_weight):
    total_score = sum(credits)
    sgpa = total_score / total_weight
    return sgpa

def get_marks_and_credits(subjects):
    credits = []
    for subject, weight in subjects:
        try:
            marks = int(input(f"\n{subject}\t\t: "))
            credits.append(grade(marks) * weight)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return None
    return credits

def First_Semester():
    subjects = [
        ("Mathematics - I", 4),
        ("Chemistry", 3),
        ("Professional Communication", 2),
        ("Biology", 2),
        ("Chemistry Lab", 1.5),
        ("Computer Programming", 4),
        ("Language Lab", 1),
        ("Engineering Graphics", 2)
    ]
    credits = get_marks_and_credits(subjects)
    if credits is None:
        return
    sgpa = calculate_sgpa(credits, 19.5)
    print("\n\n\tYour SGPA Calculated: {:.3f}".format(sgpa))

def Second_Semester():
    subjects = [
        ("Mathematics - II", 4),
        ("Physics", 4),
        ("Basic Electrical Engineering", 3),
        ("Analog Electronic Circuits", 3),
        ("Physics Lab", 1.5),
        ("Basic Electrical Engineering Lab", 1),
        ("Analog Electronic Circuits Lab", 1),
        ("Basic Manufacturing Systems", 2),
        ("Environmental Science", 1)
    ]
    credits = get_marks_and_credits(subjects)
    if credits is None:
        return
    sgpa = calculate_sgpa(credits, 20.5)
    print("\n\tYour SGPA Calculated: {:.3f}".format(sgpa))

def Third_Semester():
    subjects = [
        ("Data Structures and Algorithms", 4),
        ("Engineering Economics", 3),
        ("Principles of Digital Communication", 4),
        ("Discrete Mathematics", 3),
        ("Object-Oriented Programming", 3),
        ("Probability & Statistics", 3),
        ("Data Structures Lab", 1),
        ("Object-Oriented Programming Lab", 1)
    ]
    credits = get_marks_and_credits(subjects)
    if credits is None:
        return
    sgpa = calculate_sgpa(credits, 22)
    print("\n\tYour SGPA Calculated: {:.3f}".format(sgpa))

def Fourth_Semester():
    subjects = [
        ("Operating Systems", 3),
        ("Automata and Formal Languages", 4),
        ("Web Technology", 3),
        ("Database Management System", 4),
        ("Computer Architecture", 4),
        ("Digital Electronics", 3),
        ("Database Management System Lab", 1),
        ("Operating Systems Lab", 1),
        ("Web Technology Lab", 1),
        ("Business Communication", 1)
    ]
    credits = get_marks_and_credits(subjects)
    if credits is None:
        return
    sgpa = calculate_sgpa(credits, 25)
    print("\n\tYour SGPA Calculated: {:.3f}".format(sgpa))

def Fifth_Semester():
    subjects = [
        ("Software Engineering", 4),
        ("Big Data", 3),
        ("Design and Analysis of Algorithms", 3),
        ("Computer Networks", 3),
        ("Data Mining and Data Warehousing", 3),
        ("Internet of Things", 3),
        ("Algorithms Laboratory", 1),
        ("Networks Laboratory", 1)
    ]
    credits = get_marks_and_credits(subjects)
    if credits is None:
        return
    sgpa = calculate_sgpa(credits, 21)
    print("\n\tYour SGPA Calculated: {:.3f}".format(sgpa))

def Sixth_Semester():
    subjects = [
        ("Data Analytics", 3),
        ("Artificial Intelligence", 3),
        ("Department Elective-III", 3),
        ("Department Elective-IV", 3),
        ("Department Elective-V", 3),
        ("Open Elective-I / Minor-1", 3),
        ("Tools and Techniques Lab", 2),
        ("Data Analytics Lab", 1),
        ("Minor Project", 2)
    ]
    credits = get_marks_and_credits(subjects)
    if credits is None:
        return
    sgpa = calculate_sgpa(credits, 23)
    print("\n\tYour SGPA Calculated: {:.3f}".format(sgpa))

# The functions for 7th and 8th semesters remain as they are.
def Seventh_Semester():
    print("\n\t   Semester selected: 7th\n\n\tEnter marks of each subject (out of 100)")
    subjects = [
        ("HS Elective-II", 3),
        ("Professional Practice, Law & Ethics", 2),
        ("Open Elective-II / Minor-2", 3),
        ("Project-I/Internship", 3),
        ("Practical Training", 2)
    ]
    credits = get_marks_and_credits(subjects)
    if credits is None:
        return
    sgpa = calculate_sgpa(credits, 13)
    print("\n\tYour SGPA Calculated: {:.3f}".format(sgpa))

def Eighth_Semester():
    print("\n\t   Semester selected: 8th\n\n\tEnter marks of each subject (out of 100)")
    try:
        PI2 = int(input("\nProject-II/Internship\t\t: "))
        sgpa = grade(PI2) * 10 / 10
        print("\n\tYour SGPA Calculated: {:.3f}".format(sgpa))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print("\t\t   SGPA Calculator\n")
print("Note - SGPA/CGPA Calculator only for 'Computer Science Engineering' Branch Student \n")
try:
    n = int(input("Enter your Semester: "))
    if n == 1:
        First_Semester()
    elif n == 2:
        Second_Semester()
    elif n == 3:
        Third_Semester()
    elif n == 4:
        Fourth_Semester()
    elif n == 5:
        Fifth_Semester()
    elif n == 6:
        Sixth_Semester()
    elif n == 7:
        Seventh_Semester()
    elif n == 8:
        Eighth_Semester()
    else:
        print("Invalid semester number.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

