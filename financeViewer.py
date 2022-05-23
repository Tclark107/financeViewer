import csv
import math


class financeManager:
    net               = 0    
    expenseTotal      = 0
    incomeTotal       = 0

    necessaryPercent     = 0
    entertainmentPercent = 0
    savingsPercent       = 0
    unknownPercent       = 0
    necessaryTotal       = 0
    entertainmentTotal   = 0
    savingsTotal         = 0
    unknownTotal         = 0

    necessaryList     = list()
    entertainmentList = list()
    savingsList       = list()
    unknownList       = list()

    # maybe food and amazon should be there own category since they
    # can go either way.  ow I may just have to do a bunch of 
    # conditional checks
    necessarySet = {"CVS/PHARM","646-846-3663","PECO","TARGET","COMCAST","MTA*METROCARD","EZPASS","Rachael","*AAA","AsurionWireless","UPS"}
    entertainmentSet     = {"URBAN","UBER","CARLS","WAWA","WINE","SPIRITS","MARTHA","FIRSTLEAF","WHELIHAN","TROY","YOSH","WEGMANS","PlaystationNetwork","CheU","TRESTLE","BAR-LY","BREW","PANERA","DUNKIN","DOORDASH","SOUTHWES","TGI","AKI","PARKMOBILE","BAKESHOP","CAVANAUGHS","OLDCITYCOFFEE","EMBER","WHITE","*GRACE","PLATYPUS","GRAMOPHONE","LYFT","CANE'S","EPC*EPIC","*SEOUL","*DROELOE","*URBAN",}
    savingsSet           = {"SAVE","MONEYLINE"}

    def __init__(self, bankStatement):
        self.inputFile = bankStatement 

    def csvToList(bankCsv):
        #with open('./2021novtoDec.csv', newline='') as f:
        #with open('./202201to04.csv', newline='') as f:
        with open(bankCsv, newline='') as f:
            reader = csv.reader(f)
            transactions = list(reader)
        return transactions

    def calculateNet(transactions):
        total = 0
        for transaction in transactions:
            total = total + float(transaction[1])
        return total

    def parseDescription(expense):
       descriptionSplit = expense[4].split()
       expense.pop(4);
       expense.append(descriptionSplit)
       return expense

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
        income = list()
        expense = list()
        for transaction in transactions:
            if float(transaction[1]) > 0:
                income.append(transaction)
            else:
                expense.append(transaction)
        return income, expense
        
    def seperateExpensesIntoCategories(expenses):
        # I need to find a way to make this more robustso that I don't
        # end up in a situation where I append something to a list where
        # it shouldn't be
        # maybe write tests around this
        for expense in expenses:
            financeManager.parseDescription(expense)
            financeManager.checkEveryExpense(expense)

        financeManager.checkIfUnkownListNotEmpty()

    def checkEveryExpense(expense):
            expenseHandledFlag = 0
            for word in expense[4]:
                expenseHandledFlag = financeManager.distributeExpenseBasedOnWord(word, expense, expenseHandledFlag)
                if(expenseHandledFlag):
                    break

            if(not expenseHandledFlag):
                financeManager.unknownList.append(expense)

    def distributeExpenseBasedOnWord(word, expense, handledFlag):
        if word in financeManager.necessarySet:
            financeManager.necessaryList.append(expense)
            handledFlag = 1
        elif word in financeManager.entertainmentSet:
            financeManager.entertainmentList.append(expense)
            handledFlag = 1
        elif word in financeManager.savingsSet:
            financeManager.savingsList.append(expense)
            handledFlag = 1
        return handledFlag

    def checkIfUnkownListNotEmpty():
        while financeManager.unknownList:
            financeManager.askUserWhatExpenseThisIs(financeManager.unknownList[0])

    def askUserWhatExpenseThisIs(expense):
        while True:
            print(expense)
            userInput = input("should this go into (n)ecessary, (e)ntertainment or (s)avings: ")
            if userInput not in ("e","n","s"):
                print('you must use a "e", "n" or "s"\n')
            else:
                if userInput == 'e':
                    financeManager.entertainmentList.append(expense)
                    financeManager.unknownList.pop(0)
                if userInput == 'n':
                    financeManager.necessaryList.append(expense)
                    financeManager.unknownList.pop(0)
                if userInput == 's':
                    financeManager.savingsList.append(expense)
                    financeManager.unknownList.pop(0)
                break
            
    def calculateMainTotals(income, expense):
        financeManager.expenseTotal = financeManager.calculateNet(expense)
        financeManager.incomeTotal  = financeManager.calculateNet(income)
        financeManager.net          = financeManager.incomeTotal + financeManager.expenseTotal

    def calculateExpensePercentages():
        financeManager.necessaryPercent     = financeManager.calculatePercentage(financeManager.necessaryTotal)
        financeManager.entertainmentPercent = financeManager.calculatePercentage(financeManager.entertainmentTotal)
        financeManager.savingsPercent       = financeManager.calculatePercentage(financeManager.savingsTotal)
        financeManager.unknownPercent       = financeManager.calculatePercentage(financeManager.unknownTotal)

    def calculatePercentage(money):
        percent = money/financeManager.expenseTotal
        percent = percent*100
        return percent

    def calculateExpenseTotals():
        financeManager.necessaryTotal      = financeManager.calculateNet(financeManager.necessaryList)
        financeManager.entertainmentTotal  = financeManager.calculateNet(financeManager.entertainmentList)
        financeManager.savingsTotal        = financeManager.calculateNet(financeManager.savingsList)
        financeManager.unknownTotal        = financeManager.calculateNet(financeManager.unknownList)

    def writeToFile():
        # write everyting to a file
        #outputFile = open("results/041022.txt","w")
        outputFile = open("results/050822.txt","w")

        # eventully I'll have to get rid of the (-) signs
        outputFile.write("You spent "           + "{:.2f}".format(financeManager.necessaryTotal)       + " on necessary\n")
        outputFile.write("You spent "           + "{:.2f}".format(financeManager.entertainmentTotal)   + " on entertainment\n")
        outputFile.write("You spent "           + "{:.2f}".format(financeManager.savingsTotal)         + " on savings\n\n")

        outputFile.write("necpercentage is "    + "{:.2f}".format(financeManager.necessaryPercent)     + "%\n")
        outputFile.write("entpercentage is "    + "{:.2f}".format(financeManager.entertainmentPercent) + "%\n")
        outputFile.write("savpercentage is "    + "{:.2f}".format(financeManager.savingsPercent)       + "%\n\n")

        outputFile.write("You made "            + "{:.2f}".format(financeManager.incomeTotal)          + "\n")
        outputFile.write("You spent "           + "{:.2f}".format(financeManager.expenseTotal)         + "\n") 
        outputFile.write("Your net is "         + "{:.2f}".format(financeManager.net))

        outputFile.close()

    def calculateFinancials(bankStatement):
        transactions = financeManager.csvToList(bankStatement)
        income, expense = financeManager.seperateIntoIncomeAndExpenses(transactions)
        financeManager.calculateMainTotals(income,expense)
        financeManager.seperateExpensesIntoCategories(expense)

        financeManager.calculateExpenseTotals()
        financeManager.calculateExpensePercentages()

        financeManager.writeToFile()

        for element in financeManager.entertainmentList:
            print(element)

def main():
    bankStatement = 'bankStatements/50822.csv' 
    myFinanceManager = financeManager(bankStatement)
    financeManager.calculateFinancials(myFinanceManager.inputFile)

net = 0
if __name__ == "__main__":
    main()
