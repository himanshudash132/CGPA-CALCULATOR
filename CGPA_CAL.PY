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
    
def First_Semester():
    print("\n\t   Semester selected: 1st\n\n\tEnter marks of each subject (out of 100)")
    Mathematics = int(input("\nMathematics - I\t\t\t: "))
    a = grade(Mathematics) * 4
    Chemistry = int(input("\nChemistry\t\t\t: "))
    b = grade(Chemistry) * 3
    Professional_Communication = int(input("\nProfessional Communication\t: "))
    c = grade(Professional_Communication) * 2
    Biology = int(input("\nBiology\t\t\t\t: "))
    d = grade(Biology) * 2
    Chemistry_Lab = int(input("\nChemistry Lab\t\t\t: "))
    e = grade(Chemistry_Lab) * 1.5
    Computer_Programming = int(input("\nComputer Programming\t\t: "))
    f = grade(Computer_Programming) * 4
    Language_Lab = int(input("\nLanguage Lab\t\t\t: "))
    g = grade(Language_Lab) * 1
    Engineering_Graphics = int(input("\nEngineering Graphics\t\t: "))
    h = grade(Engineering_Graphics) * 2
    credit_total = a + b + c + d + e + f + g + h
    credit_total /= 19.5
    print("\n\n\tYour SGPA Calculated: {:.1f}".format(credit_total))  

def Second_Semester():
    print("\n\t   Semester selected: 2nd\n\n\tEnter marks of each subject (out of 100)")
    Mathematics = int(input("\nMathematics - II\t\t\t: "))
    a = grade(Mathematics) * 4
    Physics = int(input("\nPhysics\t\t\t\t: "))
    b = grade(Physics) * 4
    Basic_Electrical_Engineering = int(input("\nBasic Electrical Engineering\t: "))
    c = grade(Basic_Electrical_Engineering) * 3
    Analog_Electronic_Circuits = int(input("\nAnalog Electronic Circuits\t: "))
    d = grade(Analog_Electronic_Circuits) * 3
    Physics_Lab = int(input("\nPhysics Lab\t\t\t: "))
    e = grade(Physics_Lab) * 1.5
    Basic_Electrical_Engineering_Lab = int(input("\nBasic Electrical Engineering Lab\t: "))
    f = grade(Basic_Electrical_Engineering_Lab) * 1
    Analog_Electronic_Circuits_Lab = int(input("\nAnalog Electronic Circuits Lab\t: "))
    g = grade(Analog_Electronic_Circuits_Lab) * 1
    Basic_Manufacturing_Systems = int(input("\nBasic Manufacturing Systems\t: "))
    h = grade(Basic_Manufacturing_Systems) * 2
    Environmental_Science = int(input("\nEnvironmental Science\t\t\t: "))
    i = grade(Environmental_Science) * 1
    credit_total = a + b + c + d + e + f + g + h + i
    credit_total /= 20.5
    print("\n\tYour SGPA Calculated: {:.1f}".format(credit_total)) 

def Third_Semester():
    print("\n\t   Semester selected: 3rd\n\n\tEnter marks of each subject (out of 100)")
    DSA = int(input("\nData Structures and Algorithms\t: "))
    a = grade(DSA) * 4
    Economics = int(input("\nEngineering Economics\t: "))
    h = grade(Economics) * 3
    DE = int(input("\nPrinciples of Digital Communication\t: "))
    b = grade(DE) * 4
    DMS = int(input("\nDiscrete Mathematics\t\t: "))
    c = grade(DMS) * 3
    OOP = int(input("\nObject-Oriented Programming\t\t: "))
    d = grade(OOP) * 3
    PS = int(input("\nProbability & Statistics\t\t: "))
    e = grade(PS) * 3
    DSA_lab = int(input("\nData Structures Lab\t\t\t: "))
    f = grade(DSA_lab) * 1
    OOP_lab = int(input("\nObject-Oriented Programming Lab\t: "))
    g = grade(OOP_lab) * 1
    credit_total = a + b + c + d + e + f + g + h
    credit_total /= 22
    print("\n\tYour SGPA Calculated: {:.1f}".format(credit_total)) 

def Fourth_Semester():
    print("\n\t   Semester selected: 4th\n\n\tEnter marks of each subject (out of 100)")
    OS = int(input("\nOperating Systems\t\t: "))
    a = grade(OS) * 3
    AFL = int(input("\nAutomata and Formal Languages\t: "))
    b = grade(AFL) * 4
    WT = int(input("\nWeb Technology\t\t\t: "))
    c = grade(WT) * 3
    DBMS = int(input("\nDatabase Management System\t: "))
    d = grade(DBMS) * 4
    CA = int(input("\nComputer Architecture\t\t: "))
    e = grade(CA) * 4
    DE = int(input("\nDigital Electronics\t\t: "))
    f = grade(DE) * 3
    DBMS_lab = int(input("\nDatabase Management System Lab\t: "))
    g = grade(DBMS_lab) * 1
    OS_lab = int(input("\nOperating Systems Lab\t\t: "))
    h = grade(OS_lab) * 1
    WT_Lab = int(input("\nWeb Technology Lab\t\t: "))
    i = grade(WT_Lab) * 1
    BC = int(input("\nBusiness Communication\t\t: "))
    j = grade(BC) * 1
    credit_total = a + b + c + d + e + f + g + h + i + j
    credit_total /= 25
    print("\n\tYour SGPA Calculated: {:.1f}".format(credit_total)) 

def Fifth_Semester():
    print("\n\t   Semester selected: 5th\n\n\tEnter marks of each subject (out of 100)")
    IoT = int(input("\nInternet of Things\t\t: "))
    a = grade(IoT) * 3
    CN = int(input("\nComputer Networks\t\t: "))
    b = grade(CN) * 3
    DAA = int(input("\nDesign and Analysis of Algorithms\t: "))
    c = grade(DAA) * 3
    SE = int(input("\nSoftware Engineering\t\t: "))
    d = grade(SE) * 4
    DE1 = int(input("\nDepartment Elective-I\t\t: "))
    e = grade(DE1) * 3
    DE2 = int(input("\nDepartment Elective-II\t\t: "))
    f = grade(DE2) * 3
    NL = int(input("\nNetworks Lab\t\t\t: "))
    g = grade(NL) * 1
    AL = int(input("\nAlgorithms Lab\t\t\t: "))
    h = grade(AL) * 1
    credit_total = a + b + c + d + e + f + g + h
    credit_total /= 21
    print("\n\tYour SGPA Calculated: {:.1f}".format(credit_total)) 

def Sixth_Semester():
    print("\n\t   Semester selected: 6th\n\n\tEnter marks of each subject (out of 100)")
    DA = int(input("\nData Analytics\t\t\t: "))
    a = grade(DA) * 3
    AI = int(input("\nArtificial Intelligence\t\t: "))
    b = grade(AI) * 3
    DE3 = int(input("\nDepartment Elective-III\t\t: "))
    c = grade(DE3) * 3
    DE4 = int(input("\nDepartment Elective-IV\t\t: "))
    d = grade(DE4) * 3
    DE5 = int(input("\nDepartment Elective-V\t\t: "))
    e = grade(DE5) * 3
    OE = int(input("\nOpen Elective-I / Minor-1\t: "))
    f = grade(OE) * 3
    TT_Lab = int(input("\nTools and Techniques Lab\t: "))
    g = grade(TT_Lab) * 2
    DA_Lab = int(input("\nData Analytics Lab\t\t: "))
    h = grade(DA_Lab) * 1
    MP = int(input("\nMinor Project\t\t\t: "))
    i = grade(MP) * 2
    credit_total = a + b + c + d + e + f + g + h + i
    credit_total /= 23
    print("\n\tYour SGPA Calculated: {:.1f}".format(credit_total))

def Seventh_Semester():
    print("\n\t   Semester selected: 7th\n\n\tEnter marks of each subject (out of 100)")
    HS2 = int(input("\nHS Elective-II\t\t\t: "))
    a = grade(HS2) * 3
    PPLE = int(input("\nProfessional Practice, Law & Ethics\t: "))
    b = grade(PPLE) * 2
    OE2 = int(input("\nOpen Elective-II / Minor-2\t: "))
    c = grade(OE2) * 3
    PI = int(input("\nProject-I/Internship\t\t: "))
    d = grade(PI) * 3
    PT = int(input("\nPractical Training\t\t: "))
    e = grade(PT) * 2
    credit_total = a + b + c + d + e
    credit_total /= 13
    print("\n\tYour SGPA Calculated: {:.1f}".format(credit_total))

def Eighth_Semester():
    print("\n\t   Semester selected: 8th\n\n\tEnter marks of each subject (out of 100)")
    PI2 = int(input("\nProject-II/Internship\t\t: "))
    a = grade(PI2) * 10
    credit_total = a / 10
    print("\n\tYour SGPA Calculated: {:.1f}".format(credit_total))
    
print("\t\t   SGPA Calculator\n")
print("Note - SGPA/CGPA Calculator only for 'Computer Science Engineering' Branch Student \n")
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
