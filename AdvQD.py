import VarD
import AdvQE

# D choices
#qA1B1C1D
def qA1B1C1D():
    a=input(VarD.qA1B1C1D)
    if a=="1":
        AdvQE.qA1B1C1D1E()
    elif a=="2":
        AdvQE.qA1B1C1D2E()
    else:
        print("\n ...could you repeat? \n")
        qA1B1C1D()
#qA1B1C2D
def qA1B1C2D():
    a=input(VarD.qA1B1C2D)
    if a=="1":
        AdvQE.qA1B1C2D1E()
    elif a=="2":
        AdvQE.qA1B1C2D2E()
    else:
        print("\n ...could you repeat? \n")
        qA1B1C2D()

#A1B2C1D
# this is an end path
def qA1B2C1D():
    print(VarD.qA1B2C1D)

#A1B2C2D
#end path
def qA1B2C2D():
    print(VarD.qA1B2C2D)

#A2B1C1D
def qA2B1C1D():
    a=input(VarD.qA2B1C1D)
    if a=="1":
        AdvQE.qA2B1C1D1E()
    elif a=="2":
        AdvQE.qA2B1C1D2E()
    else:
        print("\n ...could you repeat? \n")
        qA2B1C1D()
#A2B1C2D
def qA2B1C2D():
    a=input(VarD.qA2B1C2D)
    if a=="1":
        AdvQE.qA2B1C2D1E()
    elif a=="2":
        AdvQE.qA2B1C2D2E()
    else:
        print("\n ...could you repeat? \n")
        qA2B1C2D()


#A2B2C1D
def qA2B2C1D():
    a=input(VarD.qA2B2C1D)
    if a=="1":
        AdvQE.qA2B2C1D1E()
    elif a=="2":
        AdvQE.qA2B2C1D2E()
    else:
        print("\n ...could you repeat? \n")
        qA2B2C1D()
#A2B2C2D
def qA2B2C2D():
    a=input(VarD.qA2B2C2D)
    if a=="1":
        AdvQE.qA2B2C2D1E()
    elif a=="2":
        AdvQE.qA2B2C2D2E()
    else:
        print("\n ...could you repeat? \n")
        qA2B2C2D()
