import VarE
import AdvQAB
import AdvQF

# E choices
#qA1B1C1D1E
#end path
def qA1B1C1D1E():
    print(VarE.qA1B1C1D1E)

#qA1B1C1D2E
def qA1B1C1D2E():
    a=input(VarE.qA1B1C1D2E)
    if a=="1":
        print("1")
        AdvQF.qA1B1C1D2E1F()
    elif a=="2":
        print("2")
        AdvQF.qA1B1C1D2E2F()
    else:
        print("\n ...could you repeat? \n")
        qA1B1C1D2E()


#qA1B1C2D1E
def qA1B1C2D1E():
    a=input(VarE.qA1B1C2D1E)
    if a=="1":
        print("1")
        AdvQF.qA1B1C2D1E1F()
    elif a=="2":
        print("2")
        AdvQF.qA1B1C2D1E2F()
    else:
        print("\n ...could you repeat? \n")
        qA1B1C2D1E()
#qA1B1C2D2E
def qA1B1C2D2E():
    print(VarE.qA1B1C2D2E)


#A2B1C1D1E
# sends back to beginning
def qA2B1C1D1E():
    print(VarE.qA2B1C1D1E)
    AdvQAB.qA1B()

#A2B1C1D2E
def qA2B1C1D2E():
    a=input(VarE.qA2B1C1D2E)
    if a=="1":
        print("1")
        AdvQF.qA2B1C1D2E1F()
    elif a=="2":
        print("2")
        AdvQF.qA2B1C1D2E2F()
    else:
        print("\n ...could you repeat? \n")
        qA2B1C1D2E()

#A2B1C2D1E
#end path
def qA2B1C2D1E():
    print(VarE.qA2B1C2D1E)

#A2B1C2D2E
def qA2B1C2D2E():
    a=input(VarE.qA2B1C2D2E)
    if a=="1":
        print("1")
        AdvQF.qA2B1C2D2E1F()
    elif a=="2":
        print("2")
        AdvQF.qA2B1C2D2E2F()
    else:
        print("\n ...could you repeat? \n")
        qA2B1C2D2E()

#A2B2C1D1E
def qA2B2C1D1E():
    a=input(VarE.qA2B2C1D1E)
    if a=="1":
        print("1")
        AdvQF.qA2B2C1D1E1F()
    elif a=="2":
        print("2")
        AdvQF.qA2B2C1D1E2F()
    else:
        print("\n ...could you repeat? \n")
        qA2B2C1D1E()

#A2B2C1D2E
#end path
def qA2B2C1D2E():
    print(VarE.qA2B2C1D2E)

#A2B2C2D1E
#end path
def qA2B2C2D1E():
    print(VarE.qA2B2C2D1E)

#A2B2C2D2E
def qA2B2C2D2E():
    a=input(VarE.qA2B2C2D2E)
    if a=="1":
        print("1")
        AdvQF.qA2B2C2D2E1F()
    elif a=="2":
        print("2")
        AdvQF.qA2B2C2D2E2F()
    else:
        print("\n ...could you repeat? \n")
        qA2B2C2D2E()
