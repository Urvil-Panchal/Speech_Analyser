import pandas as pd
# import csv
# from tkinter import *
# from tkinter import filedialog


class DataSet:
    """
    root = Tk()
    root.withdraw()
    file_type = dict(defaultextension=".csv", filetypes=[("csv file", "*.csv")])
    file_path = filedialog.askopenfilename(**file_type)

    print(file_path)
    """
    def __init__(self):
        self.df = pd.read_csv(r"Employee Sample Data.csv")
        self.col = []
    
    def check(self):
        for i in self.df.columns:
            self.col.append(i)
        print(self.col)
    
    def index(self, value):
        for j in self.col:
            for k in value:
                if j.lower() == k:
                    return self.col.index(j)

    def working(self):
        while True:
            choice = input("Enter choice:")

            try:
                if choice == 2:
                    print(self.df['Department'].unique())
                elif choice == 3:
                    print(self.df["City"].value_counts())
                elif choice == 4:
                    print(self.df.dropna())
                elif choice == 5:
                    print(self.df.fillna())

                elif 'rename' in choice:
                    for i in self.df.columns:
                        if i in choice:
                            print(self.df.rename(columns={i: choice.split()[-1]}))

                # Summarize Data
                # sum of column_name
                elif 'sum' in choice:
                    print(self.df[choice[7:]].sum())

                # maximum from column_name
                elif 'maximum' in choice:
                    print(self.df[choice[13:]].max())

                # minimum from column_name
                elif 'minimum' in choice:
                    print(self.df[choice[13:]].min())

                # mean of column_name
                elif 'mean' in choice:
                    print(self.df[choice[8:]].mean())

                # median of column_name
                elif ('median' and 'Median') in choice:
                    print(self.df[choice[10:]].median())

                # variance of column_name
                elif 'variance' in choice:
                    print(self.df[choice[12:]].var())

                # standard deviation of column_name
                elif 'standard deviation' in choice:
                    print(self.df[choice[22:]].std())

                # count column_name
                elif 'count' in choice:
                    print(self.df[choice[6:]].count())

                # describe
                elif 'describe' in choice:
                    print(self.df.describe())

                # shape
                elif 'shape' in choice:
                    print(self.df.shape())

                # Subset Row Observation
                elif choice == 16:
                    print(self.df.query("Age > 50 and Country == 'China'"))
                    # print(self.df[(self.df['Age'] > 50) & (self.df['Country'] == 'China') & (self.df['Job Title'] == 'Analyst')])

                # drop duplicates
                elif choice == "drop duplicates":
                    print(self.df.drop_duplicates())

                # sort by column_name
                elif 'sort' in choice:
                    print(self.df.sort_values('Full Name'))

                # n samples
                elif 'samples' in choice:
                    print(self.df.sample(int(choice[0])))

                # n heads or head
                elif ('heads' and 'head') in choice:
                    if choice[0].isdigit():
                        print(self.df.head(int(choice[0])))
                    else:
                        print(self.df.head())

                # n tails or tail
                elif ('tails' and 'tail') in choice:
                    if choice[0].isdigit():
                        print(self.df.tail(int(choice[0])))
                    else:
                        print(self.df.tail())

                elif choice == 21:
                    print(self.df.sort_values.Country)

                else:
                    break

            except Exception as e:
                print('Incorrect Command!! Error generated:', e)


if __name__ == '__main__':
    App = DataSet()
    App.check()
    App.working()
