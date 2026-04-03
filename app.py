from functions.utilFunctions import compareDates, filterDataByDate, parseStockEntryKeys
from functions.httpFunctions import makeAlphaVantageRequest
import pygal
import requests
from lxml import etree
from datetime import datetime
import webbrowser
import os

def displayPrompts():

    chartInvalid = True
    timeSeriesInvalid = True
    datesInvalid = True

    print('Stock Data Visualizer\n---------------------------')
    stock = input('\nEnter the stock symbol you are looking for: ')
    
    while chartInvalid:
        print('Chart Types\n--------------\n1. Bar\n2. Line\n')
        chart = input('Enter the chart type you want (1, 2): ')
        # verify_input(series, "int", 2)
        break
    while timeSeriesInvalid:
        print('Select the time series of the chart you want to generate\n----------------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n')
        series = input('Enter time series option(1, 2, 3, 4): ')
        # verify_input(series, "int", 4)
        break
    while datesInvalid:
        start = input('Enter start date(YYYY-MM-DD): ')
        end = input('Enter end date(YYYY-MM-DD): ')
        compareDates(start, end)
        break

def main():
    while (True):
        displayPrompts()
        choice = input("Would you like to continue viewing stock data? Enter 'y' to continue: ").trim().lower()
        if choice == "y":
            continue
        else:
            print("Thank you and goodbye!")
            break

main()