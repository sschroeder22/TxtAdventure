import VarC
import AdvQD

# C choices
#A1B1C
def qA1B1C():
    a=input(VarC.qA1B1C)
    if a=="1":
       AdvQD.qA1B1C1D()
    elif a=="2":
       AdvQD.qA1B1C2D()
    else:
        print("\n ...could you repeat? \n")
        qA1B1C()

#A1B2C
def qA1B2C():
    a=input(VarC.qA1B2C)
    if a=="1":
       AdvQD.qA1B2C1D()
    elif a=="2":
       AdvQD.qA1B2C2D()
    else:
        print("\n ...could you repeat? \n")
        qA1B2C()

#A2B1C
def qA2B1C():
    a=input(VarC.qA2B1C)
    if a=="1":
      AdvQD.qA2B1C1D()
    elif a=="2":
       AdvQD.qA2B1C2D()
    else:
        print("\n ...could you repeat? \n")
        qA2B1C()

#A2B2C
def qA2B2C():
    a=input(VarC.qA2B2C)
    if a=="1":
       AdvQD.qA2B2C1D()
    elif a=="2":
       AdvQD.qA2B2C2D()
    else:
        print("\n ...could you repeat? \n")
        qA2B2C()
