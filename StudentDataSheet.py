# Title: Student data sheets
# Type: Final Project
# Date: 07/07/2023
# Names : Abdulmalik Alqahtani and Maan Almajnuni
from os import path
from os import remove as delete
from os import system
from random import randint, seed
from time import sleep

from art import text2art
from colorama import Back, Fore, Style


def myHelp():
    system("cls")
    print(f"{Back.GREEN+' Student Data Sheet '+ Style.RESET_ALL}\n")
    print(
        Fore.CYAN
        + f'# To add a new course, please write \'{Style.RESET_ALL+Fore.YELLOW+ "add Course_Department Course_ID Course_Name Credits Term Grade" +Style.RESET_ALL+Fore.CYAN}\' Inputs should be separated by space; names with spaces should be written with double spaces; and Terms are fall, spring, and summer.\n'
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + f'# To edit an existing course, please write \'{Style.RESET_ALL+Fore.YELLOW+ "edit Course_Department Course_ID Course_Name Credits Term Grade" +Style.RESET_ALL+Fore.CYAN}\'  Inputs should be separated by space; names with spaces should be written with double spaces; and Terms are fall, spring, and summer.\n'
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + f'# To edit an existing course, please write \'{Style.RESET_ALL+Fore.YELLOW+ "remove Course_Department Course_ID" +Style.RESET_ALL+Fore.CYAN}\' Inputs should be separated by spaces.\n'
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + f'# To change courses search filter, please write \'{Style.RESET_ALL+Fore.YELLOW+ "show Type" +Style.RESET_ALL+Fore.CYAN}\' Inputs should be separated by spaces, and types are all, freshmen, and by department.\n'
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + f'# To exit the student sheet, please write \'{Style.RESET_ALL+Fore.YELLOW+ "exit" +Style.RESET_ALL+Fore.CYAN}\' The file will be encrypted and saved in the same folder.\n'
        + Style.RESET_ALL
    )
    input()
    return


def colorCyan(string):
    return Fore.CYAN + string + Style.RESET_ALL


def colorYellow(string):
    return Fore.YELLOW + string + Style.RESET_ALL


def colorBlue(string):
    return Fore.BLUE + string + Style.RESET_ALL


def colorRed(string):
    return Fore.RED + string + Style.RESET_ALL


def colorGreen(string):
    return Fore.GREEN + string + Style.RESET_ALL


def colorGPA(string):
    try:
        if string == "N/A":
            return colorYellow(string)
        elif float(string) > 3.00:
            return colorGreen(string)
        elif float(string) > 2.00:
            return colorYellow(string)
        elif float(string) <= 2.00:
            return colorRed(string)
    except:
        return colorYellow("N/A")


def encrypt(fileName, ID):
    def char_to_num(char):
        return 0 if char == " " else ord(char)

    def lstToStr(lst):
        string = str()
        for i in lst:
            string += str(i) + " "
        return string

    def encrypt_stream(string, key):
        seed(key)
        code = list()
        for char in string:
            code.append(char_to_num(char) ^ randint(0, 255))
        return code

    with open("temp.ess", "r", encoding="utf-8") as input:
        with open(fileName, "w", encoding="utf-16") as output:
            for line in input:
                output.write(lstToStr(encrypt_stream(line, ID)) + "\n")


def decrypt(fileName, ID):
    def num_to_char(num):
        return " " if int(num) == 0 else chr(int(num))

    def decrypt_stream(code, key):
        seed(key)
        string = str()
        for num in code:
            if num == "\n":
                break
            string += num_to_char(int(num) ^ randint(0, 255))
        return string

    with open(fileName, "r", encoding="utf-16") as input:
        with open("temp.ess", "w", encoding="utf-8") as output:
            for line in input:
                output.write((decrypt_stream(mySplit(line), ID)))


def mySplit(string):
    splitList = []
    first = 0

    for i in range(len(string)):
        if string[i] == " " and string[i + 1] != " " and string[i - 1] != " ":
            splitList.append(string[first:i])
            first = i + 1

        elif string[i] == " " and string[i + 1] == " ":
            pass

        elif i == len(string) - 1:
            splitList.append(string[first:])

    return splitList


def oneSpace(string):
    oneSpacedString = ""
    first = 0

    for i in range(len(string)):
        if string[i] == " " and string[i + 1] == " ":
            oneSpacedString += " "

        elif string[i] != " ":
            oneSpacedString += string[i]

    return oneSpacedString


def studentData(fileName):
    with open("temp.ess", "r", encoding="utf-8") as file:
        return file.readline().split(" ")


def myFormat(string, limit):
    if len(str(string)) > limit:
        string = str(string)[:limit]
    return format(str(string), str(limit) + "s")


def GPA(filename, type, extra=None):
    if type == "all":
        grades = 0
        credits = 0
        with open("temp.ess", "r", encoding="utf-8") as file:
            for index, line in enumerate(file):
                if index == 0:
                    continue
                if "N/A" not in line:
                    line = mySplit(line.rstrip())
                    grades += float(line[6]) * int(line[3])
                    credits += int(line[3])
        return grades / credits if credits != 0 else "N/A"
    if type == "core":
        grades = 0
        credits = 0
        with open("temp.ess", "r", encoding="utf-8") as file:
            for index, line in enumerate(file):
                if index == 0:
                    continue
                if extra in line and "N/A" not in line:
                    line = mySplit(line.rstrip())
                    grades += float(line[6]) * int(line[3])
                    credits += int(line[3])
        return grades / credits if credits != 0 else "N/A"
    if type == "freshmen":
        grades = 0
        credits = 0
        terms = term(extra)
        try:
            with open("temp.ess", "r", encoding="utf-8") as file:
                for index, line in enumerate(file):
                    if index == 0:
                        continue
                    if (
                        terms[0] in line or terms[1] in line or terms[2] in line
                    ) and "N/A" not in line:
                        line = mySplit(line.rstrip())
                        grades += float(line[6]) * int(line[3])
                        credits += int(line[3])
        except:
            return "N/A"
        return grades / credits if credits != 0 else "N/A"


def term(term):
    terms = list()
    if term[:4] == "fall":
        terms.append(term)
        terms.append("spring" + str(int(term[-2:]) + 1))
        terms.append("summer" + str(int(term[-2:]) + 1))
    elif term[:6] == "spring":
        terms.append(term)
        terms.append("fall" + str(int(term[-2:])))
    return terms


def removeN(string):
    result = str()
    for char in string:
        if char != "\n":
            result += char
    return result


def newFile(chat):
    with open("temp.ess", "w", encoding="utf-8") as file:
        file.write(f"{chat[1]} {chat[2]} {chat[3]} {chat[4]} {chat[5]}")
    print(
        f"\nThe file has been successfully created. The file name is {chat[1] + chat[3][-3:]}"
    )
    sleep(5)
    myHelp()
    mainMenu(chat[1] + chat[3][-3:], chat[3])


def openFile(fileName):
    if path.isfile(fileName):
        return True
    else:
        return False


def show(fileName, type):
    system("cls")
    Data = studentData(fileName)
    print(
        f"{Back.GREEN+' Student Data Sheet '+ Style.RESET_ALL}\n\n{colorBlue('First Name')} : {colorYellow(myFormat(Data[0],12))}  {colorBlue('Last Name')} : {colorYellow(myFormat(Data[1],12))}   {colorBlue('ID')} : {colorYellow(myFormat(Data[2],10))}\n{colorBlue('Major')} : {colorYellow(myFormat(Data[3],4))}           {colorBlue('Term of Entry')} : {colorYellow(myFormat(Data[4].rstrip(),8))}   {colorBlue('Filter')} : {colorYellow(myFormat(type,8))}\n{colorBlue('GPA')} : {colorGPA(myFormat(GPA(fileName, 'all'),4))}              {colorBlue('Freshmen GPA')} : {colorGPA(myFormat(GPA(fileName, 'freshmen',removeN(Data[4]).rstrip()),4))}     {colorBlue('Core GPA')} : {colorGPA(myFormat(GPA(fileName, 'core',Data[3]),4))}\n"
    )

    print(f"╔════╤══════╤══════╤══════════════════════╤═══╤══════════╤════╤══════╗")
    print(
        f"║ {colorRed('N')}  │ {colorRed('SUBJ')} │ {colorRed('NUMB')} │     {colorRed('Course Name')}      │ {colorRed('H')} │   {colorRed('Term')}   │ {colorRed('GR')} │  {colorRed('GP')}  ║"
    )
    print(f"╟────┼──────┼──────┼──────────────────────┼───┼──────────┼────┼──────╢")
    with open("temp.ess", "r", encoding="utf-8") as file:
        for index, line in enumerate(file):
            if index == 0:
                continue
            line = mySplit(line.rstrip())
            if type == "all":
                print(
                    f"║ {myFormat(str(index),2)} │ {myFormat(line[0],4)} │ {myFormat(line[1],4)} │ {myFormat(oneSpace(line[2]), 20)} │ {myFormat(line[3],1)} │ {myFormat(line[4], 8)} │ {myFormat(line[5], 2)} │ {myFormat(line[6], 4)} ║"
                )
            elif type == "freshmen":
                terms = term(Data[4].rstrip())
                if terms[0] in line or terms[1] in line or terms[2] in line:
                    print(
                        f"║ {myFormat(str(index),2)} │ {myFormat(line[0],4)} │ {myFormat(line[1],4)} │ {myFormat(oneSpace(line[2]), 20)} │ {myFormat(line[3],1)} │ {myFormat(line[4], 8)} │ {myFormat(line[5], 2)} │ {myFormat(line[6], 4)} ║"
                    )
            else:
                if type in line:
                    print(
                        f"║ {myFormat(str(index),2)} │ {myFormat(line[0],4)} │ {myFormat(line[1],4)} │ {myFormat(oneSpace(line[2]), 20)} │ {myFormat(line[3],1)} │ {myFormat(line[4], 8)} │ {myFormat(line[5], 2)} │ {myFormat(line[6], 4)} ║"
                    )

    print(f"╚════╧══════╧══════╧══════════════════════╧═══╧══════════╧════╧══════╝\n")


def add(fileName, subject, num, name, credits, sem, grade):
    with open("temp.ess", "a", encoding="utf-8") as file:
        with open("temp2.ess", "w", encoding="utf-8") as file2:
            try:
                file2.write(
                    f"{subject} {num} {name} {credits} {sem} {grade} {gradeScale(grade)}"
                )
            except:
                delete("temp2.ess")
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("Please enter a valid add-command.")
                sleep(3)
                return
        delete("temp2.ess")
        file.write(
            f"\n{subject} {num} {name} {credits} {sem} {grade} {gradeScale(grade)}"
        )
        print(f"\n{subject} {num} was added.")
        sleep(3)


def remove(fileName, subject, num):
    with open("temp.ess", "r+", encoding="utf-8") as file:
        newFile = file.readlines()
        file.seek(0)
        with open("temp2.ess", "w", encoding="utf-8") as file2:
            try:
                for line in newFile:
                    if f"{subject} {num}" not in line:
                        file2.write(line)
                    else:
                        pass
                    file2.truncate()
            except:
                delete("temp2.ess")
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("Please enter a valid remove-command.")
                sleep(3)
                return
        delete("temp2.ess")
        found = False
        for line in newFile:
            if f"{subject} {num}" not in line:
                file.write(line)
            else:
                print(f"\n{subject} {num} was removed.")
                found = True
                sleep(2)
            file.truncate()
        if found == False:
            system("cls")
            print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
            print("Please enter a valid Course data.")
            sleep(3)
            return


def edit(fileName, subject, num, name, credits, sem, grade):
    with open("temp.ess", "r+", encoding="utf-8") as file:
        newFile = file.readlines()
        file.seek(0)
        with open("temp2.ess", "w", encoding="utf-8") as file2:
            try:
                for line in newFile:
                    if f"{subject} {num}" not in line:
                        file2.write(line)
                    else:
                        file2.write(
                            f"{subject} {num} {name} {credits} {sem} {grade} {gradeScale(grade)}\n"
                        )
                    file.truncate()
            except:
                delete("temp2.ess")
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("Please enter a valid edit-command.")
                sleep(3)
                return
        found = False
        for line in newFile:
            if f"{subject} {num}" not in line:
                file2.write(line)
            else:
                file2.write(
                    f"{subject} {num} {name} {credits} {sem} {grade} {gradeScale(grade)}\n"
                )
                print(f"\n{subject} {num} was edited.")
                found = True
                sleep(3)
            file.truncate()
        if found == False:
            system("cls")
            print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
            print("Please enter a valid Course data.")
            sleep(3)
            return


def gradeScale(grade):
    grades_dict = {
        "A": 4.00,
        "A-": 3.67,
        "B+": 3.33,
        "B": 3.00,
        "B-": 2.67,
        "C+": 2.33,
        "C": 2.00,
        "C-": 1.67,
        "D+": 1.33,
        "D": 1.00,
        "D-": 0.67,
        "F": 0.00,
        "P": "N/A",
        "FF": "N/A",
        "N/A": "N/A",
    }
    return grades_dict[grade]


def mainMenu(fileName, ID):
    type = "all"
    while True:
        try:
            show("temp.ess", type)
        except:
            system("cls")
            print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
            print(
                "There are some issues with your inputs. Going back to the main menu...."
            )
            sleep(4)
            return
        chat = mySplit(input())
        if chat[0] == "add":
            try:
                add(fileName, chat[1], chat[2], chat[3], chat[4], chat[5], chat[6])
                continue
            except:
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("Please enter a valid add-command.")
                sleep(3)
                continue

        elif chat[0] == "remove":
            try:
                remove(fileName, chat[1], chat[2])
                continue
            except:
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("Please enter a valid remove-command.")
                sleep(3)
                continue

        elif chat[0] == "edit":
            try:
                edit(fileName, chat[1], chat[2], chat[3], chat[4], chat[5], chat[6])
                continue
            except:
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("Please enter a valid edit-command.")
                sleep(3)
                continue

        elif chat[0] == "show":
            try:
                type = chat[1]
                show(fileName, type)
                continue
            except:
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("Please enter a valid show-command.")
                sleep(3)
                continue

        elif chat[0] == "help":
            myHelp()
            continue

        elif chat[0] == "exit":
            with open("temp.ess", "r", encoding="utf-8") as file:
                line = mySplit(file.readline())
                encrypt(line[0] + line[2][-3:] + ".ess", ID)
            delete("temp.ess")
            system("cls")
            print(f"{Back.GREEN+' Student Data Sheet '+ Style.RESET_ALL}\n")
            print("The file was saved successfully.")
            sleep(3)
            return

        else:
            system("cls")
            print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
            print("Please enter a valid command.")
            sleep(3)
            continue


def main():
    system("cls")
    print(colorCyan(text2art("Student Data Sheet", font="basic")))
    sleep(6)
    while True:
        system("cls")
        print(f"{Back.GREEN+' Student Data Sheet '+ Style.RESET_ALL}\n")
        print(
            Fore.CYAN
            + f'# To create a new student file, please write \'{Style.RESET_ALL+Fore.YELLOW+ "new First_Name Last_Name ID Major Term_Of_Entry" +Style.RESET_ALL+Fore.CYAN}\' Inputs should be separated by spaces, and names shouldn\'t include spaces.\n'
            + Style.RESET_ALL
        )
        print(
            Fore.CYAN
            + f'# To open an existing student file, please write \'{Style.RESET_ALL+Fore.YELLOW+ "open File_Name ID" +Style.RESET_ALL+Fore.CYAN}\' Inputs should be separated by spaces, and the file should be in the same folder.\n'
            + Style.RESET_ALL
        )

        chat = mySplit(input())
        if chat[0] == "new":
            if len(chat) == 6 and (chat[5][:4] == "fall" or chat[5][:6] == "spring"):
                newFile(chat)
            else:
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("Please enter a valid student's data.")
                sleep(3)
                continue

        elif chat[0] == "open":
            if openFile(chat[1] + ".ess"):
                try:
                    decrypt(chat[1] + ".ess", chat[2])
                    mainMenu("temp.ess", chat[2])

                except:
                    system("cls")
                    print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                    print("Please enter a valid file and a valid ID.")
                    sleep(3)
                    continue
            else:
                system("cls")
                print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
                print("The file does not exist.")
                sleep(3)
        elif chat[0] == "exit":
            return
        else:
            system("cls")
            print(f"{Back.RED+' Student Data Sheet '+ Style.RESET_ALL}\n")
            print("Please enter a valid command.")
            sleep(3)
            continue


if __name__ == "__main__":
    main()
