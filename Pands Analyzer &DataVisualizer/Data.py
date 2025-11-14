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

    def __del__(self):
        print("Cleaning up resources...")

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")

    def explore_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\n--- First 5 Rows ---")
        print(self.data.head())
        print("\n--- Data Info ---")
        print(self.data.info())
        print("\n--- Descriptive Statistics ---")
        print(self.data.describe())

    def mathematical_operations(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        if 'Sales' in self.data.columns and 'Profit' in self.data.columns:
            self.data['Profit Margin %'] = (self.data['Profit'] / self.data['Sales']) * 100
            print("\nAdded new column: 'Profit Margin %'")
        else:
            print("Columns 'Sales' or 'Profit' not found in dataset.")

    def clean_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\nMissing values before cleaning:")
        print(self.data.isnull().sum())
        self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
        print("\nMissing values after cleaning:")
        print(self.data.isnull().sum())

    def descriptive_statistics(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        print("\n--- Aggregation Examples ---")
        print("Total Sales by Region:")
        print(self.data.groupby('Region')['Sales'].sum())
        print("\nAverage Profit by Product:")
        print(self.data.groupby('Product')['Profit'].mean())

        print("\n--- Statistical Summary ---")
        print(self.data.describe())
        print("\nStandard Deviation:\n", self.data.std(numeric_only=True))
        print("\nVariance:\n", self.data.var(numeric_only=True))

    def visualize_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        print("\nSelect Visualization Type:")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Heatmap")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            sns.barplot(data=self.data, x='Region', y='Sales')
        elif choice == 2:
            if 'Date' in self.data.columns:
                sns.lineplot(data=self.data, x='Date', y='Sales')
            else:
                print("No 'Date' column found.")
                return
        elif choice == 3:
            sns.scatterplot(data=self.data, x='Sales', y='Profit')
        elif choice == 4:
            self.data.groupby('Region')['Sales'].sum().plot.pie(autopct='%1.1f%%')
        elif choice == 5:
            plt.hist(self.data['Sales'], bins=10)
        elif choice == 6:
            sns.heatmap(self.data.corr(numeric_only=True), annot=True, cmap='coolwarm')
        else:
            print("Invalid choice.")
            return

        plt.title("Data Visualization")
        plt.show(block=False)
        self.last_plot = plt.gcf()

    def save_visualization(self):
        if self.last_plot is None:
            print("No plot available to save. Please create a plot first.")
            return
        filename = input("Enter file name to save the plot (e.g., sales_plot.png): ")
        if self.last_plot:
            self.last_plot.savefig(filename)
        print(f"Visualization saved as {filename} successfully!")


def main():
    print("***** Data Analysis & Visualization Program *****")
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========= MAIN MENU =========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations (Mathematical)")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            path = input("Enter dataset path (CSV file): ")
            analyzer.load_data(path)
        elif choice == '2':
            analyzer.explore_data()
        elif choice == '3':
            analyzer.mathematical_operations()
        elif choice == '4':
            analyzer.clean_data()
        elif choice == '5':
            analyzer.descriptive_statistics()
        elif choice == '6':
            analyzer.visualize_data()
        elif choice == '7':
            analyzer.save_visualization()
        elif choice == '8':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()