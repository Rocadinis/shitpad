# (C) Rodrigo Dinis, 2022
import os
os.system("color a")
os.system("title Shitpad")
text = []
def shitpad():
    while True:
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
        elif writtenText == "shitpadopen()": #IMPERFECT BUT IT WORKS, I'LL HAVE TO FIX IT LATER
            try:
                filename = input("Open which file? ")
                if filename != "":
                    with open(filename, "r+") as f:
                        for openline in f.readlines():
                            text.append(openline)
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
            except:
                print("The file was not found. Please try again.")
        elif writtenText == "shitpadedit()":
            try:
                textIndex = int(input("Please input the number of the line you want to edit. "))
                newText = input("Write the new text: ")
                arrIndex = textIndex - 1
                text[arrIndex] = newText + "\n"
                print("Line overwritten sucessfully. \n")
                linecounter = 1
                for line in text:
                    formatted = line[:len(line) - 1]
                    print(linecounter, formatted)
                    linecounter = linecounter + 1
                shitpad()
            except:
                print("An invalid line number was given. Please try using the function again. \n")
        elif writtenText == "shitpaddelete()":
            try:
                textIndex = int(input("Please input the number of the line you want to remove. "))
                text.pop(textIndex - 1)
                print("Line deleted sucessfully. \n")
                linecounter = 1
                for line in text:
                    formatted = line[:len(line) - 1]
                    print(linecounter, formatted)
                    linecounter = linecounter + 1
                shitpad()
            except:
                print("An invalid line number was given. Please try using the function again. \n")
        else:
            text.append(writtenText + "\n") #if the input isn't a command, write the line
shitpad() #run