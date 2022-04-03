import csv

def csvToList():
    with open('./2021novtoDec.csv', newline='') as f:
        reader = csv.reader(f)
        transactions = list(reader)
    return transactions

def calculateNet(transactions):
    net = 0
    for transaction in transactions:
        net = net + float(transaction[1])
    return net

def parseDescription(transactions):
    descriptionSplit = list()
    for description in transactions:
        word = description[4].split()
        descriptionSplit.append(word)
    return descriptionSplit


def main():
    transactions = csvToList()
    net = calculateNet(transactions)
    print(net)
    
    descriptionList = parseDescription(transactions)

    savings = list()
    for description in descriptionList:
        for word in description: 
            if(word == 'SAVE'):
                print(transactions[1])

    savings = list()
    

if __name__ == "__main__":
    main()
