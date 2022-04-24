# (C) Rodrigo Dinis, 2022
import os
text = []
def shitpad():
    while True:
        writtenText = input("")
        if writtenText == "shitpadexit()":
            def saveProcess():
                filename = input("Please type the name of the file (extension included).\n")
                if filename != "":
                    file = open(filename, "w")
                    for element in text:
                        file.write(element)
                    file.close()
                    os.startfile(filename)
                    os._exit(0)
                else:
                    print("Please specify a filename.")
                    saveProcess()
            saveProcess()    
        elif writtenText == "shitpadedit()":
            try:
                textIndex = int(input("Please input the number of the line you want to edit. "))
                newText = input("Write the new text: ")
                arrIndex = textIndex - 1
                text[arrIndex] = newText + "\n"
                print("Line overwritten sucessfully. \n")
                shitpad()
            except:
                print("An invalid line number was given. Please try using the function again. \n")
        elif writtenText == "shitpaddelete()":
            try:
                textIndex = int(input("Please input the number of the line you want to remove. "))
                text.pop(textIndex - 1)
                print("Line deleted sucessfully. \n")
                shitpad()
            except:
                print("An invalid line number was given. Please try using the function again. \n")
        else:
            text.append(writtenText + "\n") #if the input isn't a command, write the line
shitpad() #run