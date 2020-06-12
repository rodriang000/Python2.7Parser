#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
# ConvertText, by Angel "Yaboi" Rodriguez 3/18/2018
# The purpose of this program is to allow the user to edit a list of characters they want to remove 
# from files they enter.

# TODO: Expand to be able to do using multiple cores where each function does a convertText
# using parallel programming. Could do for funsies.

# Figure out what you want to do for square and curly bracketes. Maybe have an if statement
# Similar to how you've handled smart quotes.

EDITLIST= ["~", "`", "@", "$", "%", "^", "&", "*", "\"", "|", "+", "=", "#", "{", "}", "[","]"]
def convertText(mylist, editlist=EDITLIST):
	for afile in mylist:
		filename = afile + ".txt"
		if os.path.isfile(filename) and os.stat(filename).st_size != 0:
			info = " "
			with open(filename, 'r') as origfile, open("AR " + filename, 'w') as newfile:			
				print "File is open!"
				info = origfile.read()
				# Add a print see what type info is, could add the replace method here.
				# Example:
				# for char in EDITLIST:
				#       info.replace(char, " ")
				infolist = info.split('\n')
				for line in infolist:
					newline = []
					for char in line:
						# Check for smart quotes, if it finds one replace it with "
						if char == "“" or char == "”":
							char = "\""
						# Check for the other types of characters, if it finds one, replace with empty space
						if char in editlist or char == '\t':
							if char == '{' or '[':
								char = '('
							elif char == '}' or ']':
								char = ')'
						newline.append(char)
					# Done with line, add it to write file, delete newline
					stringline = ''.join(newline)
					newfile.write(stringline)
					newfile.write('\n')
				print "Finished with: " ; print filename
				 
def changelist(choice = 2, editlist = EDITLIST):
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == 2:
        del editlist[:]
        print('''
    Type out the characters to remove from the files, seperated by a comma(,)
    Ex: 
    $,#,*,",',<
        
Your characters:''')
        editlist = list((raw_input().split(',')))
        return editlist
    
    elif choice == 3:
        print('''
    Type out the characters to add to the list, seperated by a comma(,)
    Ex: 
    z,/,\\,+,=
    List of characters: {}

Your characters:'''.format(editlist))
        newlist = editlist + list(raw_input().split(','))
        return newlist

    elif choice == 4:
        print('''
    Type out the characters tor remove from the list, seperated by a comma(,)
    Ex: 
    z,/,abc,%,ok
    List of characters: {}

Remove Characters:'''.format(editlist))
    delList = list(set((raw_input().split(','))))
    [ editlist.remove(element) for element in delList if element in editlist ]
    return editlist

def getfiles():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
    Type out the name of the files to be edited, seperated by \",\"
    Ex: 
    File1,File2,File3,Angel is cool,Goofigoober
    
    ** Make sure to match the spelling, otherwise the program won't find the file. **

Filenames:''')
    mylist = raw_input().split(',')
    return mylist

def usage():
    print("You don't have to worry about [] or {} characters, they automatically get switched to ()")
    print( '''
        Hello, give me characters you would like to remove from the file(s).
        Type '1' for the basic list 
        Type '2' to start a new list with only your characters added
        Type '3' to add to the list
        Type '4' to remove from the list
        Type '5' to stop editing the list
        ''')
    print('''
Your choice:''')

# Main
if __name__ == '__main__':
    usage()
    editlist = EDITLIST
    # Get the list of information from the user
    usrChoice = str(input())
    while usrChoice != '5':
        if usrChoice == '1':
            editlist =["~", "`", "@", "$", "%", "^", "&", "*", "\"", "|", "+", "=", "#", "{", "}", "[","]"]
        elif usrChoice == '2':
            editlist = sorted(list(set(changelist(int(usrChoice),editlist))))
        elif usrChoice == '3':
            editlist = sorted(list(set(changelist(int(usrChoice),editlist))))
        elif usrChoice == '4':
            editlist = sorted(list(set(changelist(int(usrChoice),editlist))))
        else:
            print("You need to type a number 1 through 5. Exiting program.")
            exit()
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Your list is:") ; print(editlist)
        usage()
        usrChoice = raw_input()
    # Now that both components are had, do convert Text
    myfiles = getfiles()
    print("The files are:") ; print (myfiles)
    print("The list is:") ; print (editlist)
    convertText(myfiles,editlist)
    print("Type enter to close the program")
    wait = raw_input()
