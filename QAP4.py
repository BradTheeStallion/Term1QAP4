#QAP4:  A  program  to  enter  and  calculate  new  insurance  policy information for the One  Stop  Insurance  Company's customers.
#By Brad Ayers
#March 14 - 22, 2024

#Imports
import datetime
import CoolStuffQAP4 as QAP4 #Most functions used in this program are here

#Functions
#A version of this function exists in CoolStuff, but in order to work it needs to be copy-pasted and tailored to the program.
def DataFile(Filename):
    #This function automates the data file saving process, including a loading bar. Specify the name of the file as an arugment when calling the function.
    #DataFile("filename.dat")
    import types
    import time
    import random
    PHRASE_1 = "Saving: Please Stand By"
    PHRASE_2 = "Data Saved Successfully."
    DataList = []
    Frames1 = []
    Frames2 = []
    Frames3 = []
    def FrameLoop(Phrase, FrameList):
        #Just avoiding repetition within the outer function.
        Counter1 = 0
        Counter2 = 1
        while Counter1 <= len(Phrase):
            FrameList.append(Phrase[0:Counter2])
            Counter1 += 1
            Counter2 += 1
    AllVars = dict(globals())
    for Name, Var in AllVars.items():
        if type(Var) not in [types.ModuleType, types.FunctionType] and not Name.startswith("_"):
            DataList.append(Var)
    f = open(Filename, "a")
    f.write("Date:       Policy #:  Name:              Address:                Tel #:          Email:                 # Cars:  Premium:\n")
    f.write("--------------------------------------------------------------------------------------------------------------------------\n")
    f.write(f"{DataList[0]:<10s}  {DataList[3]:<4d}       {DataList[10][0]:<1s}. {DataList[11]:<15s} {DataList[12]:<20s}    {DataList[16]:<14s}  {DataList[17]:<25s} {DataList[18]:<2d}  {QAP4.Hst(DataList[22])[2]:>10s}\n")
    f.write(f"                                          {DataList[13]} {DataList[14]}\n")
    f.write(f"                                          {DataList[15]}\n")
    f.close()
    FrameLoop(PHRASE_1, Frames1)
    for i in range(0,3):
        for j in range(0,4):
            Frames1.append(PHRASE_1 + (j * " ."))    
    for i in range(0,41):
        Frames2.append(i * "|")
    FrameLoop(PHRASE_2, Frames3)
    for frame in Frames1:
        print("\r" + frame, end="")
        time.sleep(0.03)
    print("\r" + " " * len(Frames1[-1]), end="")
    LoadingDelay = random.randint(20,34)
    for frame in Frames2:
        if frame == Frames2[LoadingDelay]:
            print("\r" + frame, end="")
            time.sleep(random.uniform(0.6, 0.9))
        else:
            print("\r" + frame, end="")
            time.sleep(0.05)
    print("\r" + " " * len(Frames2[-1]), end="")
    for frame in Frames3:
        if frame != Frames3[-1]:
            print("\r" + frame, end="")
            time.sleep(0.03)
        else:
            print("\r" + frame, end="")
            time.sleep(0.5)
    print("\r" + " " * len(Frames3[-1]), end="")

while True:

    #Constants
    TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
    MONTHS = 8 #Number of months in the payment plan

    #The 7 constants below are saved in the file Defaults.dat
    #I didn't include HST since it's baked into my Hst() function

    f = open("Defaults.dat", "r")
    NEXT_POL_NUM = int(f.readline()) #Next  policy  number
    BAS_PREM = float(f.readline()) #Basic  premium
    DISC_ADD_CAR = float(f.readline()) #Discount  for additional  cars
    LIABILITY = float(f.readline()) #Cost  of  extra  liability  coverage
    GLASS = float(f.readline()) #Cost  of  glass  coverage
    LOANER = float(f.readline()) #Cost  for  loaner  car coverage
    MONTHLY_PROC_FEE = float(f.readline()) #Processing fee for monthly payments
    f.close()

    #Inputs 1
    #I chose to divide the inputs and processing into two sections so I could validate the downpayment against the total.
    print()
    if not QAP4.Whoops("Welcome to One Stop Insurance's Policy Detail Form. Press any key to continue.\nIf you are here by mistake, type END: "):
        print("Thank you for using the QAP4 claim processing program!")
        print()
        break
    CustFrstName = QAP4.ValidNameAdd("Please enter the customer's first name: ")[1]
    print()
    CustLstName = QAP4.ValidNameAdd("Please enter the customer's last name: ")[1]
    print()
    StAdd = QAP4.ValidNameAdd("Please enter the customer's street address: ")[1]
    print()
    City = QAP4.ValidNameAdd("Please enter the customer's city of residence: ")[0]
    print()
    Prov = QAP4.ValidProv("Please enter the customer's province of residence (XX): ")
    print()
    PstCode = QAP4.ValidPost("Please enter the customer's postal code (X#X#X#): ")[1]
    print()
    PhoNum = QAP4.ValidPhone("Please enter the customer's phone number (##########): ")[1]
    print()
    Email = QAP4.ValidEmail("Please enter the customer's email address: ")
    print()
    NumCars = QAP4.IntMoreZero("Please enter the number of cars to be insured: ")
    print()
    ExtLiab = QAP4.ValidYN("Will the customer opt for extra liability up to $1,000,000? (Y or N): ")  
    print()
    Glass = QAP4.ValidYN("Will the customer opt for glass coverage? (Y or N): ")
    print()
    Loaner = QAP4.ValidYN("Will the customer opt for a loaner car? (Y or N): ")
    print()
    
    #Processing 1
    Premium = BAS_PREM
    for i in range(NumCars):
        if i != 0:
            Premium += (BAS_PREM * DISC_ADD_CAR)

    TotExCost = 0
    if ExtLiab == "Y":
        TotExCost += (NumCars * LIABILITY)
    if Glass == "Y":
        TotExCost += (NumCars * GLASS)
    if Loaner == "Y":
        TotExCost += (NumCars * LOANER)
    
    TotPrem = QAP4.Hst(Premium + TotExCost)
    
    #Inputs 2
    PayType = QAP4.ValidYN("Will the customer opt for full or monthly payment? (F or M)?: ", "F", "M")
    if PayType == 'M':
        DPStatus = QAP4.ValidYN("Will the customer opt to make a down payment? (Y or N): ")
        if DPStatus == 'Y':
            while True:
                DownPay = QAP4.MFMoreZero("Please enter the amount of the downpayment: ")
                if DownPay > TotPrem[1]:
                    QAP4.Padding("Error: Downpayment cannot be more than total.")
                    continue
                else:
                    break
        else:
            DownPay = 0
    else:
        DownPay = 0
    print()
        
    ClaimList = []
    while True:
        if not QAP4.Whoops("Press return to enter the customer's previous claims.\nIf there are no previous claims, type END: "):
            break
        Listy = []
        Listy.append(QAP4.ValidInt("Please enter previous claim number: "))
        Listy.append(QAP4.ValiDate("Press return to enter previous claim date: ")[1])
        Listy.append(QAP4.MoneyFloat("Please enter previous claim amount: ")[1])
        ClaimList.append(Listy)
        print()
        
    #Processing 2
    AmtDue = (TotPrem[1] - DownPay)
    MthlyPay = ((TotPrem[1] + MONTHLY_PROC_FEE - DownPay)/MONTHS)
         
    #Output
    print()
    print("          One Stop Insurance Company")
    print("           Insurance Claim Invoice:")
    print("______________________________________________")
    print()
    print(f"  Invoice Date: {TODAY:<10s}   Policy No: {NEXT_POL_NUM:>4d}")
    print()
    print(f"  Customer:")
    print()
    print(f"    {CustFrstName:<{len(CustFrstName)}s} {CustLstName:<{27 - len(CustFrstName)}s}")
    print(f"    {StAdd:<29s}")
    print(f"    {City:<{len(City)}s} {Prov:<2s} {PstCode:<7s}")
    print(f"    {PhoNum:<14s}")
    print(f"    {Email:<20s}")
    print()
    print("----------------------------------------------")
    print()
    print(f"    Number of Cars: {NumCars:<2d}")
    print()
    print(f"       Premium:              {QAP4.Hst(Premium)[2]:>10s}")
    if ExtLiab == "Y":
        print(f"       Extra Liability:         {QAP4.Hst(NumCars * LIABILITY)[2]:>7s}")
    if Glass == "Y":
        print(f"       Glass Coverage:          {QAP4.Hst(NumCars * GLASS)[2]:>7s}")
    if Loaner == "Y":    
        print(f"       Loaner Car:              {QAP4.Hst(NumCars * LOANER)[2]:>7s}")
    print(f"       Total Extras:         {QAP4.Hst(TotExCost)[2]:>10s} ")
    print(f"       Subtotal:             {TotPrem[2]:>10s}")
    print(f"       HST:                  {TotPrem[3]:>10s}")
    if PayType == 'M':
        print("                             ----------")
        print(f"       Total:                {TotPrem[4]:>10s}")
        print(f"       Downpayment:          {QAP4.Hst(DownPay)[2]:>10s}")
        print("                             ----------")
        print(f"       Total Due:            {QAP4.Hst(AmtDue)[2]:>10s}")
        print()
        print("----------------------------------------------")
        print()
        print(f"  Processing Fee:    {QAP4.Hst(MONTHLY_PROC_FEE)[2]:<6s}  (one time only)")
        print(f"  Monthly Payment:   {QAP4.Hst(MthlyPay)[2]:<8s} (for {MONTHS} months)")
        print()
        print(f"  First Payment Due: {QAP4.FrstNxtMnth()[1]:<10s}")
        print()
    else:
        print("                             ----------")
        print(f"       Total Due:            {TotPrem[4]:>10s}")
        print()
    print("----------------------------------------------")
    print()
    print("               Previous Claims")
    print("               ---------------")
    print("   Claim #          Date            Amount")
    print("  -----------------------------------------")

    if ClaimList:
        for item in ClaimList:
            print(f"   {item[0]:<6d}        {item[1]:^10s}    {item[2]:>11s}")
    else:
        print("              No Previous Claims.")

    print("  -----------------------------------------")
    print()
    print("          One Stop: Look No Further!")
    print()
    print("----------------------------------------------")
    print()
    
    DataFile("Claims.dat")
    f = open("Claims.dat", "a")
    if ClaimList:
        for item in ClaimList:
            f.write("{}\n".format(f"Previous Claim #: {item[0]}, Date: {item[1]}, Amt: {item[2]}"))
            f.write("\n")
    else:
        f.write("No Previous Claims.\n")
        f.write("\n")
        f.write("\n")
    f.close()
    
    NEXT_POL_NUM += 1
    QAP4.UpdateFrstLn("Defaults.dat", (str(NEXT_POL_NUM)))

    #Housekeeping
    if not QAP4.Whoops("\nPress return to enter another customer, or type END and press return to exit the program: "):
        print("Thank you for using the QAP4 claim processing program!")
        print()
        break
