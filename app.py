import pygal
import requests
from lxml import etree
from datetime import datetime
import webbrowser
import os

def invalid_int_test():

    return

def invalid_string_test():

    return

def invalid_date_test():

    return

def verify_input(input, type, range):
    # use conditions to find if int or date is invalid return input if valid or display error and repeat entry
    input.trim()
    if type == "int":
        if invalid_int_test():
            return False
        else:
            return input
    elif type == "string":
        if invalid_string_test():
            return False
        else:
            return input
    else:
        if invalid_date_test():
            return False
        else:
            return input

def display_prompts():
    print('Stock Data Visualizer\n---------------------------')
    stock = input('\nEnter the stock symbol you are looking for: ')
    verify_input(chart, "int", 2)
    print('Chart Types\n--------------\n1. Bar\n2. Line\n')
    chart = input('Enter the chart type you want (1, 2): ')
    print('Select the time series of the chart you want to generate\n----------------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n')
    series = input('Enter time series option(1, 2, 3, 4): ')
    verify_input(series, "int", 4)
    start = input('Enter start date(YYYY-MM-DD): ')
    verify_input(series, "date", "")
    end = input('Enter end date(YYYY-MM-DD): ')
    verify_input(series, "date", "")

def main():
    while (True):
        display_prompts()
        choice = input("Would you like to continue viewing stock data? Enter 'y' to continue: ").trim().lower()
        if choice == "y":
            continue
        else:
            print("Thank you and goodbye!")
            break

main()