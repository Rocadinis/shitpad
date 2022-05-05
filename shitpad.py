# (C) Rodrigo Dinis, 2022
import os, time
os.system("cls")
os.system("color a")
os.system("title Shitpad")
text = []
def shitpad():
    while True:
        def printLines():
            linecounter = 1
            for line in text:
                formatted = line[:len(line) - 1]
                print(linecounter, formatted)
                linecounter = linecounter + 1
        lines = len(text) + 1
        writtenText = input(str(lines) + " ")
        if writtenText == "shitpadexit()":
            def saveProcess():
                filename = input("Please type the name of the file (extension included).\n")
                if filename != "":
                    file = open(filename, "w")
                    for element in text:
                        file.write(element)
                    file.close()
                    os._exit(0)
                else:
                    print("Please specify a filename.")
                    saveProcess()
            saveProcess()    
        elif writtenText == "shitpadopen()":
            try:
                filename = input("Open which file? ")
                if filename != "":
                    with open(filename, "r+") as f:
                        if len(text) >= 0:
                            overwriteConf = input("There is already text in this file. Discard your changes and open a file? ").lower()
                            if overwriteConf == "yes" or overwriteConf == "y":
                                os.system("cls")
                                while text:
                                    text.pop()
                                for openline in f.readlines():
                                    text.append(openline)
                            else:
                                print("Process aborted.")
                                shitpad()
                    linecounter = 1
                    for line in text:
                        if linecounter == len(text):
                            print(linecounter, line)
                            textIndex = linecounter - 1
                            text[textIndex] = text[textIndex] + "\n"
                        else:
                            formatted = line[:len(line) - 1]
                            print(linecounter, formatted)
                            linecounter = linecounter + 1
                    linecounter = linecounter + 1
                    shitpad()
                else:
                    print("Please specify a filename.")
                    printLines()
            except:
                print("The file was not found. Please try again.")
        elif writtenText == "shitpadedit()":
            try:
                textIndex = int(input("Please input the number of the line you want to edit. "))
                newText = input("Write the new text: ")
                arrIndex = textIndex - 1
                text[arrIndex] = newText + "\n"
                print("Line overwritten sucessfully. \n")
                time.sleep(1.5)
                os.system("cls")
                printLines()
                shitpad()
            except:
                print("An invalid line number was given. Please try using the function again. \n")
                printLines()
        elif writtenText == "shitpaddelete()":
            try:
                textIndex = int(input("Please input the number of the line you want to remove. "))
                text.pop(textIndex - 1)
                print("Line deleted sucessfully. \n")
                time.sleep(1.5)
                os.system("cls")
                linecounter = 1
                printLines()
                shitpad()
            except:
                print("An invalid line number was given. Please try using the function again. \n")
                printLines()
        elif writtenText == "shitpadinsert()":
            try:
                line = int(input("Please input the number of the line you want to insert into. "))
                insText = input("Write the text: ")
                text.insert(line - 1, insText)
                print("Line inserted sucessfully.")
                time.sleep(1.5)
                os.system("cls")
                printLines()
                shitpad()
            except:
                print("An invalid line number was given. Please try using the function again. \n")
        elif writtenText == "shitpadfind()":
            toFind = input("Please input the text to find. ")
            linecounter = 0
            found = 0
            for line in text:
                linecounter += 1
                if toFind in line:
                    print(linecounter, line)
                    found = found + line.count(toFind)
            print("Found " + str(found) + " occurences of " + toFind + " in this file.")
            printLines()
            shitpad()
        else:
            text.append(writtenText + "\n") #if the input isn't a command, write the line
shitpad() #run