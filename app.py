import pygal
import requests
from lxml import etree
from datetime import datetime
import webbrowser
import os

def display_prompts():
    print('Stock Data Visualizer\n---------------------------')
    stock = input('\nEnter the stock symbol you are looking for: ')
    print('Chart Types\n--------------\n1. Bar\n2. Line\n')
    chart = input('Enter the chart type you want (1, 2): ')
    print('Select the time series of the chart you want to generate\n----------------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n')
    series = input('Enter time series option(1, 2, 3, 4): ')
    start = input('Enter start date(YYYY-MM-DD): ')
    end = input('Enter end date(YYYY-MM-DD): ')

def main():
    while (True):
        display_prompts()
        choice = input("Would you like to continue viewing stock data? Enter 'y' to continue: ")
        if choice == "y":
            continue
        else:
            print("Exiting application...")
            break

main()