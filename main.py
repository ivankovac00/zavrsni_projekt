from subject import Subject
from student import Student
from studentGrade import StudentGrade
from blockchain import Blockchain
from block import Block
from time import sleep

LIST_OF_SUBJECTS = [Subject("Hrvatski"), Subject("Povijest"), Subject("Matematika"), Subject("Zemljopis"), Subject("Biologija")]
LIST_OF_STUDENTS = [Student("Anić Ana", 1), Student("Bebek Toni", 2),Student("Milić Goran", 16), Student("Vučić Zoran", 24)]
list_of_student_grades = []
blockchain = Blockchain()

#metoda koja provjerava da li je uneseni znak integer
def inputTypeCheckerService(input):
    try:
        int(input)
    except ValueError:
        return False
    return True
    
#metoda provjerava da li je input u dozvoljenom rasponu
def inputRangeCheckerService(start, end, userInput):
    if userInput < start or userInput > end:
        return False
    return True

#metoda koja kombinira prethodne 2 metode i ispisuje zadanu poruku
def inputCheckerService(msg, start, end):
    isInputComplete = False
    while not isInputComplete:
        print(msg)
        userInput = input()
        if not inputTypeCheckerService(userInput):
            print("Neispravan unos!")
            continue
        userInput = int(userInput)
        if not inputRangeCheckerService(start, end, userInput):
            print("Neispravan unos!")
            continue
        return userInput

#metoda koja ispisuje blokove
def printBlockchain():
    if not blockchain.blocks:
        print("Nema zapisa!")
    else:
        for block in blockchain.blocks:
            print("\n")
            print(f"block: {block.index}")
            print(f"hash: {block.hash}")
            print(f"previous hash: {block.prevHash}")
            print(f"timestamp: {block.timestamp}")
            print(f"data: {block.data}")
            sleep(1.0)
    return ""

#metoda koja kreira blokove
def createBlock(data):
    try:
        lastBlock = blockchain.blocks[-1]
    except IndexError:
        lastBlock = False
    if not lastBlock:
        return Block(1, data,"Ovo je prvi hash!")
    else:
        return Block(lastBlock.index + 1, data, lastBlock.hash)

# metoda koja provjerava odabir korinika, provjerava imamo li dosada unešenih ocjena, te dodaje novu ocjenu u listu ocjena
# također poziva metodu za kreiranje blokova
def addGrade(subject, student):
    isInputComplete = False
    grade = inputCheckerService("Unesite ocjenu:", 1, 5)

    studentGradeList = list(filter(lambda x: x.student.name == student.name and x.subject.name == subject.name, list_of_student_grades))
    if not studentGradeList:
        studentGrade = StudentGrade(student, subject)
        studentGradeList = [studentGrade]
        list_of_student_grades.append(studentGradeList[0])
    studentGradeList[0].grades.append(grade)
    data = f"Učeniku {studentGradeList[0].student.name} je upisana ocjena {grade} iz predmeta {studentGradeList[0].subject.name}."
    blockchain.blocks.append(createBlock(data))
    return ""

# metoda koja provjerava korisnikov odabir predmeta i učenika te poziva metodu za upis ocjena
def subjectProcedure():
    index = 1
    for subject in LIST_OF_SUBJECTS:
        print(f"{str(index)}. {subject.name}")
        index += 1
    subjectIndex = inputCheckerService("Odaberi predmet:", 1, index)

    subject = LIST_OF_SUBJECTS[subjectIndex-1]

    index = 1
    for student in LIST_OF_STUDENTS:
        print(f"{str(index)}. {student.name}")
        index += 1
    studentIndex = inputCheckerService("Odaberi učenika:", 1, index)
    selectedStudent = LIST_OF_STUDENTS[studentIndex-1]
    addGrade(subject, selectedStudent)
    return ""

# metoda koja provjerava korisnikov odabir učenika te ispisuje njegove postojeće ocjene ako ih ima
def studentProcedure():
    print("Odaberi učenika: ")
    index = 1
    for student in LIST_OF_STUDENTS:
        print(f"{str(index)}. {student.name}")
        index += 1
    studentIndex = inputCheckerService("Odaberi učenika:", 1, index)

    selectedStudent = LIST_OF_STUDENTS[studentIndex-1]
    studentGradeList = list(filter(lambda x: x.student.name == selectedStudent.name, list_of_student_grades))
    if not studentGradeList:
        print("Nema unesenih ocjena! ")
    else:
        print(f"Ocjene učenika {selectedStudent.name} su:")
        for grade in studentGradeList:
            print(grade.subject.name)
            print(', '.join(map(str, grade.grades)))
    return ""

# switch case metoda koja poziva prethodno navedene metode te izvršava moguće opcije 
def switch(choice):
    if choice == 1:
        subjectProcedure()
    elif choice == 2:
        studentProcedure()
    elif choice == 3:
        printBlockchain()
    return ""

choice = 0

# metoda koja provjerava korisnikov unos te poziva switch case metodu 
# također završava program ako je korisnik unio broj 9
while(choice!=9):
    print("1) Upis ocjene\n2) Prikaz ocjena\n3) Ispiši podatke o blockchainu\n9) Izlaz")
    print("Unesite opciju: ")
    choice = input()
    if not inputTypeCheckerService(choice):
        print("Neispravan unos!")
        continue
    choice = int(choice)
    if choice == 9:
        continue
    if not inputRangeCheckerService(1, 3, choice):
        print("Neispravan unos!")
        continue
    print(switch(choice))

print("------Kraj programa------")