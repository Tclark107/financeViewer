import csv

def csvToList():
    with open('./2021novtoDec.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def main():
    data = csvToList()
    total = 0
    for transaction in data:
        total = total + float(transaction[1])
    print(total)

if __name__ == "__main__":
    main()
