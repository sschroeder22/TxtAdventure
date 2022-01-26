organization explained = """
VarC stands for the Variables C
AdvQC stands for Adventure Questions C

The first question asked is A, the second B, the third C, etc

So how I specify which C question is something like "qA1B2C."

qA1B2C is when option 1 was chosen for A and option 2 for B.

Each letter has all the code for those questions on one file,
and the text that belongs to them in a seperate file. The question
functions import the variables with the text from the
corresponding variable files.
"""



Section= "What a Variable file looks like:"
#the only thing on the variable files is a lot of text
#it sets a question variable equal to the question text, and prompts the user to input "1" or "2"
qA1B1C = """
    The giant squid tosses and turns the Seeker, but
finally the creature growstired of its new game and
jets off with an enormous squirt of water [...]
    Just as the platform begins to move, the giant
squid suddenly returns as if from nowhere. It is
headed directly at you.

If you decide to fight the squid
with yourspear gun, hoping to scare
it off, press 1.

If you decide to signal Maray to pull
you up at top speed, knowing you will
get the bends, press 2.
 """



Section= "What a question looks like:""
#imports Variables from VarC so that they can be used in this file
import VarC
#imports AdvQD so that the question here can send the user to the next one after
import AdvQD
#defines the function of given question. In this case A1B1C
def qA1B1C():
    #prints the question from VarC.py and sets the input equal to a
    a=input(VarC.qA1B1C)
    #if variable a is 1, that means option 1 was chosen and it runs the next question, in this case qA1B1C1D
    #if an option were to take someone back to a previous question, it would be imported at the top and ran instead
    if a=="1":
       AdvQD.qA1B1C1D()
    #same as above but for a=2
    elif a=="2":
       AdvQD.qA1B1C2D()
    #if an option other than 1 or 2 was entered, then it repeats the question
    else:
        print("\n ...could you repeat? \n")
        qA1B1C()



Section= "What an ending looks like"
#defines the question, same as above
def qA1B2C1D():
    #instead of promting an input, just prints it and is stopped.
    print(VarD.qA1B2C1D)

Section = "Launcher File"
#TxtAdv imports and runs the first question, I have a seperate launcher because I had it more complicated originally
import AdvQAB
AdvQAB.qA()
