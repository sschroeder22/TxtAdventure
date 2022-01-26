import VarAB
import VarC
import AdvQC

def qA():
      #texting asking for an option choice
    a=input(VarAB.qA)
    #starts function opA1 (explained above) when option 1 chosen
    if a=="1":
        qA1B()
    #starts function opA2 (explained above) when option 2 chosen
    elif a=="2":
        qA2B()
# if the input isnt for either option, it reads a text and repeats the question till there is a proper answer
    else:
        print("\n ...could you repeat? \n")
        qA()

#the same as above is repeated, one for each possability of A. there were 2 possabilities for A, will be 4 for B, and it will get exponentially bigger each time

#B QUESTIONS

#question B when option 1 was chosen on qA
def qA1B():
    a=input(VarAB.qA1B)
    if a=="1":
        AdvQC.qA1B1C()
    elif a=="2":
        AdvQC.qA1B2C()
    else:
        print("\n ...could you repeat? \n")
        qA1B()

#question B when option 2 was chosen on qA
def qA2B():

    a=input(VarAB.qA2B)
    if a=="1":
       AdvQC.qA2B1C()
    elif a=="2":
       AdvQC.qA2B2C()
    else:
        print("\n ...could you repeat? \n")
        qA2B()
