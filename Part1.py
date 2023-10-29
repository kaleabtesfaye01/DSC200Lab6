import pandas as pd
import openpyxl as op


def main():
    hourly_rates_df = pd.read_csv('./data/Hourly_Rates_of_Pay_by_Classification_and_Step.csv')
    employee_demo_df = pd.read_csv('./data/Employee+Demographics.csv')
    clean_data()
    merged_df = pd.merge(hourly_rates_df, employee_demo_df, right_on='JobTitle', left_on='Title', how='inner')


def clean_data():
    with open('./data/cpsaat22.xlsx', 'r') as fptr:
        wb = op.load_workbook(fptr)

main()