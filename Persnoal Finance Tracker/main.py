import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ['date', 'amount', 'category', 'description']
    FORMAT = "%d-%m-%Y"
    #Initializing
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
        
    #Adding entry
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'date' : date,
            'amount' : amount,
            'category' : category,
            'description' : description
        }
        
        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")


    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask] # only the values that were true for the mask will be stored

        if filtered_df.empty:
            print("No transaction found in the given date range")
        else:
            print(f"Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={'date':lambda x: x.strftime(CSV.FORMAT)}))

        total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()
        total_expanse = filtered_df[filtered_df['category'] == 'Expanse']['amount'].sum()
        print('\nSummary')
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expanse: ${total_expanse:.2f}")
        print(f"Net Savings: ${(total_income - total_expanse):.2f}")

        return filtered_df

obj = CSV()

def add():
    obj.initialize_csv()
    date = get_date("Enter the date of the transacton (dd-mm-yyyy) oe enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    obj.add_entry(date, amount, category, description)

#Plotting the dates and income and expanses
def plot_transaction(df):
    df.set_index('date', inplace=True)

    income_df = (df[df['category'] == 'Income'].resample('D').sum().reindex(df.index, fill_value=0))
    expanse_df = (df[df['category'] == 'Expanse'].resample('D').sum().reindex(df.index, fill_value=0))


    plt.figure(figsize=(10,5))
    plt.plot(income_df.index, income_df['amount'], label='Income', color='g')
    plt.plot(expanse_df.index, expanse_df['amount'], label='Expanse', color='r')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income and Expanses Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print('2. View transaction and summary whitin a date range')
        print('3. Exit')
        choice = input('Enter your choice (1-3): ')
        if choice == '1':
            add()
        elif choice == '2':
            start = get_date("Enter the start date (dd-mm-yyyy)")
            end = get_date("Enter the end date (dd-mm-yyyy)")
            df = obj.get_transaction(start, end)
            if input('Do you want to see a plot? (y/n)').lower() == 'y':
                plot_transaction(df)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print('Not a valid choice. Enter 1, 2 or 3.')


if __name__ == '__main__':
    main()