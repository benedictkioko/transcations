import csv
from operator import itemgetter
from datetime import datetime
from itertools import islice


def get_the_best(transactions_csv_file_path, n=0):
    consecutive_days = {}
    previous_day = {}
    with open(transactions_csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        # this line changed
        for customer_id, _, date_str in sorted(reader, key=itemgetter(0, 2)):
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
                elif td.days != 0:
                    consecutive_days[customer_id].insert(0, 1)

        longest_consecutive_days = map(lambda x: (
            x[0], max(x[1])), consecutive_days.items())

        sorted_consecutive_days = sorted(
            longest_consecutive_days, key=itemgetter(1), reverse=True)
        return list(islice(map(lambda x: x[0], sorted_consecutive_days), n))


def main():
    file_path = input('file > ')
    n = int(input('num > '))
    print(get_the_best(file_path, n))


if __name__ == '__main__':
    main()
