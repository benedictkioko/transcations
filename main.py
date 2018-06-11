import csv
from operator import itemgetter
from datetime import datetime


def find(transactions_csv_file_path, n = 0):
  consecutive_days = {}
  previous_day = {}
  with open(transactions_csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for customer_id, _, date_str in reader:
        date = datetime.strptime(date_str[:10], "%Y-%M-%d")
        if customer_id not in consecutive_days:
            consecutive_days[customer_id] = [1]
        if customer_id not in previous_day:
            previous_day[customer_id] = date
        else:
            td = date - previous_day[customer_id]
            previous_day[customer_id] = date
            if td.days == 1:
                consecutive_days[customer_id][0] += 1
            else:
                consecutive_days[customer_id].insert(0, 1)

    longest_consecutive_days = []
    for cust_id, vals in consecutive_days.items():
        longest_consecutive_days.append((cust_id, max(vals)))

         
    sorted_consecutive_days = sorted(longest_consecutive_days, key=itemgetter(1), reverse=True)
    return list(map(lambda x : x[0], sorted_consecutive_days))[:n]


def main():
    file_path = input('file > ')
    n = int(input('num > '))
    print(find(file_path, n))

if __name__ == '__main__':
    main()