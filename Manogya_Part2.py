"""
Name: Manogya Aryal
Class: DSC 200
Lab 6 part 2

"""

import pandas as pd


# This is the class that will clean the dataset  and create a new csv file with the clean dataset.
class Lab6:
    # constructor for class that accepts the csv and column name files
    def __init__(self, csvFile, column_file):
        self.csvFile = csvFile
        self.column_file = column_file

    def CleanData(self):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(self.csvFile)

        # Display information about the DataFrame
        print(df.info())
        # print the number of observations(rows) and features (columns) in the dataset before cleaning it
        observations_before_cleaning = len(df)
        features_before_cleaning = len(df.columns)
        print(
            f"The number of features and observations before cleaning the csv file are: {features_before_cleaning}, "
            f"{observations_before_cleaning} ")

        # Remove rows with missing values
        df = df.dropna()

        #  Rename columns to match the specified names from the column name file
        df = df.rename(columns={'educ_num': 'education-num'})
        df = df.rename(columns={'marital_status': 'marital-status'})

        # the correct columns we need
        columns = [
            "age", "workclass", "fnlwgt", "education", "education-num",
            "marital-status", "occupation", "relationship", "race",
            "sex", "capital-gain", "capital-loss", "hours-per-week",
            "native-country", "salary"
        ]

        # write the new cleaned column names in the csv file
        df = df[columns]

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Replace "?" with pd.NA throughout the dataset
        df = df.map(lambda x: pd.NA if str(x).strip() == "?" else x)

        # Remove rows with missing values
        df = df.dropna()

        # Identify categorical columns to check for incosistent values
        categorical_columns = df.select_dtypes(exclude=['number']).columns

        # Print unique values for each categorical column
        for column in categorical_columns:
            unique_values = df[column].unique()
            print(f"Unique values in '{column}':")
            for value in unique_values:
                print(value)

        # Define a mapping dictionary for education column that has inconsistent data
        mapping_dict_education = {
            'bachelors': 'Bachelors',
            'hs-grad': 'HS-grad',
            'some-college': 'Some-college',
            'assoc-acdm': 'Assoc-acdm',
            '7th-8th': '7th-8th',
            '10th': '10th',
            '1st-4th': '1st-4th',
            'preschool': 'Preschool',
            '12th': '12th',
            'masters': 'Masters',
            '9th': '9th',
            'doctorate': 'Doctorate',
            'prof-school': 'Prof-school',
            'assoc-voc': 'Assoc-voc',
            '5th-6th': '5th-6th',
        }

        # Recode values using the mapping dictionary for the education column
        df['education'] = df['education'].replace(mapping_dict_education)

        # Save the cleaned data to a new CSV file
        new_csv_file = self.csvFile.replace('.csv', '_cleaned.csv')
        df.to_csv(new_csv_file, index=False)

        #  Print the final number of features and observations after cleaning the dataset
        observations_after_cleaning = len(df)
        features_after_cleaning = len(df.columns)
        print(
            f"The number of features and observations after cleaning the CSV file are: {features_after_cleaning}, {observations_after_cleaning}")

    # this function merges the three datasets we've chosen in Lab 5 and saves the merged dataset into a csv file.
    def Part1(self):

        # first dataset, has hourly rates of pay by classification of jobs for year 2018
        hourly_rates_df = pd.read_csv(
            '../../Desktop/Group2_Lab6/data/Hourly_Rates_of_Pay_by_Classification_and_Step.csv')

        # second dataset, has employee demographics of Arlington, VA
        employee_demo_df = pd.read_csv('../../Desktop/Group2_Lab6/data/Employee+Demographics.csv')

        # third dataset, has the average weekly hours worked nationally from 2013 to 2022.
        average_weekly_hours = pd.read_csv('../../Desktop/Group2_Lab6/data/Average_weekly_hours_of_all_employees.csv', index_col=0)

        # merge the first and second dataset on the job title. Perform inner join
        merged_df = pd.merge(hourly_rates_df, employee_demo_df, right_on='JobTitle', left_on='Title', how='inner')

        # add an average_weekly_hours column and fill it with the average_weekly_hours from 2018
        average_weekly_hours = average_weekly_hours.T
        merged_df['Avg_Weekly_Hours'] = average_weekly_hours[2018].mean()

        merged_df.to_csv('./data/employee_data.csv')


# this is the main that provides path to csv file and colunm name file and creates an instance of class Lab6 and passes
# the values for csvFile and columnNameFile
def main():
    csv = './data/Lab6Data.csv'
    column_file = '../../Desktop/Group2_Lab6/data/Lab6DataColumn .names'
    lab6 = Lab6(csv, column_file)

    choice = int(input('Choose part 1 or part 2: '))
    if choice == 1:
        lab6.CleanData()
    elif choice == 2:
        lab6.Part1()
    else:
        print('Incorrect input. Run script again and input either 1 or 2.')


main()
