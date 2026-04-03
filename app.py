from functions.utilFunctions import compareDates, filterDataByDate, parseStockEntryKeys, validateDate
from functions.httpFunctions import makeAlphaVantageRequest
from functions.chartFunctions import generateChart
from models.chart_types import ChartTypes
from models.time_series import TimeSeries
import pygal
import requests
from lxml import etree
import webbrowser
import os

def displayPrompts():

    print('Stock Data Visualizer\n---------------------------')
    stock = input('\nEnter the stock symbol you are looking for: ').strip().upper()
    
    while True:
        print('\nChart Types\n--------------\n1. Bar\n2. Line\n')
        chart = input('Enter the chart type you want (1, 2): ').strip()

        if chart == "1":
            chart_type = ChartTypes.BAR
            break
        elif chart == "2":
            chart_type = ChartTypes.LINE
            break
        else:
            print("Invalid chart selection. Please enter 1 or 2.")

    while True:
        print('\nSelect the time series of the chart you want to generate\n----------------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n')
        series = input('Enter time series option(1, 2, 3, 4): ').strip()

        if series == "1":
            time_series=TimeSeries.TIME_SERIES_INTRADAY
            break
        elif series == "2":
            time_series = TimeSeries.TIME_SERIES_DAILY
            break
        elif series == "3":
            time_series = TimeSeries.TIME_SERIES_WEEKLY
            break
        elif series == "4":
            time_series = TimeSeries.TIME_SERIES_MONTHLY
            break
        else:
            print("Invalid time series selection. Please enter 1, 2, 3, or 4.")

    while True:
        start = input('\nEnter start date(YYYY-MM-DD): ').strip()
        end = input('Enter end date(YYYY-MM-DD): ').strip()
        
        if not validateDate(start) or not validateDate(end):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue

        if compareDates(start,end) == 1:
            print("Start date must be earlier than end date.")
            continue

        break

    generateChart(symbol=stock, chart_type=chart_type, time_series=time_series, beginning_date=start, end_date=end)

def main():
    while True:
        displayPrompts()
        choice = input("Would you like to continue viewing stock data? Enter 'y' to continue: ").strip().lower()
        if choice == "y":
            continue
        else:
            print("Thank you and goodbye!")
            break

main()