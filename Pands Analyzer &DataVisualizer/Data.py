import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:
    def __init__(self, file_path=None):
        self.data = None
        self.last_plot = None
        if file_path:
            self.load_data(file_path)

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")


# EXPLORE DATA

    def explore_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== Explore Data ==")
            print("1. Display first 5 rows")
            print("2. Display last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                print(self.data.head())
            elif choice == '2':
                print(self.data.tail())
            elif choice == '3':
                print(self.data.columns)
            elif choice == '4':
                print(self.data.dtypes)
            elif choice == '5':
                print(self.data.info())
            elif choice == '6':
                break
            else:
                print("Invalid choice!")


# MATHEMATICAL OPERATIONS

    def mathematical_operations(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        if 'Sales' in self.data.columns and 'Profit' in self.data.columns:
            self.data['Profit Margin %'] = (self.data['Profit'] / self.data['Sales']) * 100
            print("Added new column 'Profit Margin %'")
        else:
            print("Columns 'Sales' or 'Profit' not found")


#  HANDLE MISSING DATA

    def clean_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display missing value rows")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing with a specific value")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                missing = self.data[self.data.isnull().any(axis=1)]
                if missing.empty:
                    print("No missing values!")
                else:
                    print(missing)

            elif choice == '2':
                self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
                print("Missing values filled with mean.")

            elif choice == '3':
                self.data.dropna(inplace=True)
                print("Rows with missing values dropped.")

            elif choice == '4':
                value = input("Enter replacement value: ")
                self.data.fillna(value, inplace=True)
                print("Missing values replaced.")

            elif choice == '5':
                break
            else:
                print("Invalid choice!")


# DESCRIPTIVE STATISTICS

    def descriptive_statistics(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        print("\n--- Descriptive Statistics ---")
        print(self.data.describe())


# DATA VISUALIZATION

    def visualize_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                x = input("Enter X column: ")
                y = input("Enter Y column: ")
                sns.barplot(data=self.data, x=x, y=y)

            elif choice == '2':
                x = input("Enter X column: ")
                y = input("Enter Y column: ")
                sns.lineplot(data=self.data, x=x, y=y)

            elif choice == '3':
                x = input("Enter X column: ")
                y = input("Enter Y column: ")
                sns.scatterplot(data=self.data, x=x, y=y)

            elif choice == '4':
                column = input("Enter column for pie chart grouping: ")
                self.data[column].value_counts().plot.pie(autopct="%1.1f%%")

            elif choice == '5':
                column = input("Enter column for histogram: ")
                plt.hist(self.data[column], bins=10)

            elif choice == '6':
                break
            else:
                print("Invalid choice!")
                continue

            plt.title("Visualization")
            plt.show(block=False)
            self.last_plot = plt.gcf()


# SAVE VISUALIZATION

    def save_visualization(self):
        if self.last_plot is None:
            print("No plot to save!")
            return

        filename = input("Enter filename (e.g. plot.png): ")
        self.last_plot.savefig(filename)
        print(f"Visualization saved as {filename}")


# MAIN PROGRAM


def main():
    print("=========== Data Analysis & Visualization Program ============")
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========= MAIN MENU =========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("====================================================")

        choice = input("Enter your choice: ")

        if choice == 1:
            path = input("Enter dataset path (CSV file): ")
            analyzer.load_data(path)
        elif choice == 2:
            analyzer.explore_data()
        elif choice == 3:
            analyzer.mathematical_operations()
        elif choice == 4:
            analyzer.clean_data()
        elif choice == 5:
            analyzer.descriptive_statistics()
        elif choice == 6:
            analyzer.visualize_data()
        elif choice == 7:
            analyzer.save_visualization()
        elif choice == 8:
            print("Exiting program. goodbye👋🏻")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
