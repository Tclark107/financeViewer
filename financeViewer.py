import csv
import math

global net

def csvToList():
    with open('./2021novtoDec.csv', newline='') as f:
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

#def parseByWord(transactions):
#   unknown = list()
#   for transaction in transactions:
#      for word in transaction[4]:
#         if(word == 'SAVE'):
#              savings += float(transaction[1])
#         elif(word == 'TROY'):
#              nonNecessaryFood += float(transaction[1])
#         elif(word == 'UBER'):
#              uber += float(transaction[1])
#         elif(word == 'ONLYFANS.COM'):
#              hdog += float(transaction[1])
#         elif(word == 'MDW'):
#              nonNecessaryFood += float(transaction[1])
#         elif(word == 'CIAO'):
#              nonNecessaryFood += float(transaction[1])
#         elif(word == 'CARLS'):
#              nonNecessaryFood += float(transaction[1])
#         elif(word == 'LOCKHEED'):
#              salary += float(transaction[1])
#         elif(word == 'CVS/PHARM'):
#              medical += float(transaction[1])
#         elif(word == 'CHICAGONEWSST1725'):
#              nonNecessaryFood += float(transaction[1])
#         # maybe travel should be seperated out more
#         # maybe fore some kinds of transactions where
#         # we have multiple kinds of transactions we should
#         # make another category
#         # like food

#I am going to overload this
def checkThatWeKeepTrackOfAllTransactions():
    incomeTotal = calculateNet(income)
    expenseTotal = calculateNet(expense)
    total = incomeTotal + expenseTotal
    delta = net - total
    delta = math.sqrt(delta * delta)
    if(delta >= 0.001):
        print("total != net")

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
    necessarySpending = list()
    entertainment     = list()
    savings           = list()
    unknown           = list() 
    # I may want another called food because seperating
    # it between necessity and entertainment is tough

    # I think that I want to rework this where
    # I will have a couple different dictionaries and
    # if word is in any of the dictionaries then put it into a list
    # that way rather than updating this, I can update the dictionary
    # plus looking up in a dictionary is going to be faster
    for expense in expenses:
        for word in expense[4]:
            if(word == 'SAVE'):
                savings.append(expense)
                del expense # issue here is if I start deleting something
                            # with save in it that is also something else
                            #maybe I put another if check here? 
#           elif word == 'TROY':
#               entertainment.append(expense)
#               del expense
#           elif(word == 'UBER'):
#               entertainment.append(expense)
#               del expense
#           elif(word == 'SPIRITS'):
#               unknown.append(expense)
#               del expense
#           elif(word == 'CIAO'):
#               entertainment.append(expense)
#               del expense
#           elif(word == 'CARLS'):
#               entertainment.append(expense)
#               del expense
#           elif(word == 'WAWA'):
#               entertainment.append(expense)
#               del expense
#           elif(word == 'CVS/PHARM'):
#               necessarySpending.append(expense)
#               del expense
#           elif(word == 'CHICAGONEWSST1725'):
#               entertainment.append(expense)
#               del expense
#           elif(word == 'HLLFRSH'):
#               necessarySpending.append(expense)
#               del expense
#           elif(word == 'ONLYFANS'):
#               entertainment.append(expense)
#               del expense
#           elif(word == 'MARTHA'):
#               entertainment.append(expense)
#               del expense
#           elif(word == 'TALW'):
#               unknown.append(expense)
#               del expense
#           elif(word == 'PlaystationNetwork'):
#               entertainment.append(expense)
#               del expense
#           elif(word == 'WEGMANS'):
#               entertainment.append(expense)
#               del expense
            else:
                unknown.append(expense)
                del expense
            break

    ukTotal = calculateNet(unknown)
    entTotal = calculateNet(entertainment)
    nSTotal = calculateNet(necessarySpending)
    sTotal = calculateNet(savings)
    total = nSTotal + sTotal + entTotal + ukTotal
    return total

def calculateFinancials(transactions):
    income, expense = seperateIntoIncomeAndExpenses(transactions)
    incomeTotal = calculateNet(income)
    print(incomeTotal)
    
    total = seperateExpensesIntoCategories(expense)
    print(incomeTotal + total)

#def initializeTotals():
#    savings, nonNecessaryFood, necessaryFood, alcohol,
#    bars, uber, hdog, salary, medical = 0

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
