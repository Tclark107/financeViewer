import csv
import math

global net
global expenseTotal
global outputFile

def csvToList():
    #with open('./2021novtoDec.csv', newline='') as f:
    #with open('./202201to04.csv', newline='') as f:
    with open('./41022.csv', newline='') as f:
        reader = csv.reader(f)
        transactions = list(reader)
    return transactions

def calculateNet(transactions):
    total = 0
    for transaction in transactions:
        total = total + float(transaction[1])
    return total

def parseDescription(transactions):
    for description in transactions:
        descriptionSplit = description[4].split()
        description.pop(4);
        description.append(descriptionSplit)
    return transactions

#I am going to overload this
#def checkThatWeKeepTrackOfAllTransactions():
#   incomeTotal = calculateNet(income)
#   expenseTotal = calculateNet(expense)
#   total = incomeTotal + expenseTotal
#   delta = net - total
#   delta = math.sqrt(delta * delta)
#   if(delta >= 0.001):
#       print("total != net")

def seperateIntoIncomeAndExpenses(transactions):
    global net
    income = list()
    expense = list()
    for transaction in transactions:
        if float(transaction[1]) > 0:
            income.append(transaction)
        else:
            expense.append(transaction)
    return income, expense
    
def seperateExpensesIntoCategories(expenses):
    necessarySet = {"CVS/PHARM","646-846-3663","PECO","TARGET","COMCAST","MTA*METROCARD","EZPASS","Rachael"}
    entertainmentSet     = {"UBER","CARLS","WAWA","WINE","SPIRITS","MARTHA","FIRSTLEAF","WHELIHAN","TROY","YOSH","WEGMANS","PlaystationNetwork","CheU","TRESTLE","BAR-LY","BREW","PANERA","DUNKIN","DOORDASH","SOUTHWES","TGI","AKI","PARKMOBILE","BAKESHOP","CAVANAUGHS","OLDCITYCOFFEE"}
    savingsSet           = {"SAVE","MONEYLINE"}

    necessaryList = list()
    entertainmentList     = list()
    savingsList           = list()
    unknownList           = list()

    # I need to find a way to make this more robustso that I don't
    # end up in a situation where I append something to a list where
    # it shouldn't be
    # maybe write tests around this
    count =0
    processMemo = list()
    expenseHandledFlag = 0
    for expense in expenses:
        count += 1
        for word in expense[4]: 
            if word in necessarySet:
                necessaryList.append(expense)
                expenseHandledFlag = 1
                break
            elif word in entertainmentSet:
                entertainmentList.append(expense)
                expenseHandledFlag = 1
                break
            elif word in savingsSet:
                savingsList.append(expense)
                expenseHandledFlag = 1
                break
        if(not expenseHandledFlag):
            unknownList.append(expense)
        expenseHandledFlag = 0

    print(count)
    print (len(expenses))
    return necessaryList, entertainmentList, savingsList, unknownList
    #if count does not = amount of expenses throw an error

def calculatePercentage(money):
    global expenseTotal
    percent = money/expenseTotal
    percent = int(percent*100)
    return percent

def calculateFinancials(transactions):
    global expenseTotal
    income, expense = seperateIntoIncomeAndExpenses(transactions)
    incomeTotal = calculateNet(income)
    expenseTotal = calculateNet(expense)
    print(expenseTotal)
    print(incomeTotal)
    Total = incomeTotal + expenseTotal
    print(Total)
    
    necessaryList, entertainmentList, savingsList, unknownList = seperateExpensesIntoCategories(expense)

    necessaryTotal = calculateNet(necessaryList)
    entertainmentTotal= calculateNet(entertainmentList)
    savingsTotal = calculateNet(savingsList)
    unknownTotal = calculateNet(unknownList)

    necessaryPercent     = calculatePercentage(necessaryTotal)
    entertainmentPercent = calculatePercentage(entertainmentTotal)
    savingsPercent       = calculatePercentage(savingsTotal)
    unknownPercent       = calculatePercentage(unknownTotal)

    # print everything to screenout
    print("You spent " , necessaryTotal, " on necessary things")
    print("You spent " , entertainmentTotal ," on entertainment things")
    print("You spent " , savingsTotal , " on savingsthings")
    print("You spent " , unknownTotal , " on unknown things")
    print("Here is your unknown list of things")
    for element in unknownList:
        print(element)
    print("necpercentage is ", necessaryPercent, "%\n")
    print("entpercentage is ", entertainmentPercent, "%\n")
    print("savpercentage is ", savingsPercent, "%\n")
    print("unkpercentage is ", unknownPercent, "%\n")
    print("You made" , incomeTotal) 
    print("You spent" , expenseTotal) 
    print("Your net is" , Total) 

    # write everyting to a file
    outputFile = open("041022.txt","w")
    outputFile.write("You spent " + str(calculateNet(necessaryList))+ " on necessary things\n")
    outputFile.write("You spent " + str(calculateNet(entertainmentList))+" on entertainment things\n")
    outputFile.write("You spent " + str(calculateNet(savingsList)) + " on savingsthings\n")
    outputFile.write("You spent " + str(calculateNet(unknownList)) + " on unknown things\n")
    outputFile.write("Here is your unknown list of things\n")
    for element in unknownList:
        outputFile.write(str(element)+"\n")
    outputFile.write("necpercentage is "+ str(necessaryPercent)+"\n")
    outputFile.write("entpercentage is "+ str(entertainmentPercent)+"\n")
    outputFile.write("savpercentage is "+ str(savingsPercent)+"\n")
    outputFile.write("unkpercentage is "+ str(unknownPercent)+"\n")
    outputFile.write("You made" + str(incomeTotal)+"\n")
    outputFile.write("You spent" + str(expenseTotal)+"\n") 
    outputFile.write("Your net is" + str(Total))

    outputFile.close()

def main():
    global net
#    initializeTotals()
    transactions = csvToList()
    net = calculateNet(transactions)
    print(net)
    
    parseDescription(transactions)
    calculateFinancials(transactions)

net = 0
if __name__ == "__main__":
    main()
