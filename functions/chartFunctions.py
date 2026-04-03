from models import chart_types, time_series
from functions.utilFunctions import compareDates, filterDataByDate, parseStockEntryKeys
from functions.httpFunctions import makeAlphaVantageRequest
import pygal
import json
import os

functions = os.path.dirname(os.path.abspath(__file__))
repoRoot = os.path.dirname(functions)
testPath = os.path.join(repoRoot, "test.json")

def generateChart(symbol: str, chart_type: chart_types.ChartTypes, time_series: time_series.TimeSeries, beginning_date: str, end_date: str) -> None:
    date_verified = compareDates(beginning_date, end_date)
    if date_verified == 1:
        print("Error: Beginning date must be earlier than end date.")
        return
    
    request = makeAlphaVantageRequest(function=time_series.value, symbol=symbol)
    if not request:
        print("Error: Failed to retrieve data from AlphaVantage.")
        return
        
    key = list(request.keys())[-1] # this is required since the value of the time series key changes based on the type of time series requested
    
    # with open(testPath, "r") as f: # delete after testing w/json
    
    raw_data = request.get(key, {}) # raw_data = json.load(f) 
    if not raw_data or not isinstance(raw_data, dict):
        print("Error: Invalid stock symbol or no data found for the specified time series.")
        return
        
    filtered_data = filterDataByDate(raw_data, beginning_date, end_date)
    if not filtered_data:
        print("Error: No data found for the specified date range.")
        return
    

    
    
    if chart_type == chart_types.ChartTypes.LINE:
        chart_class = pygal.Line
    elif chart_type == chart_types.ChartTypes.BAR:
        chart_class = pygal.Bar
    else:
        print("Error: Invalid chart type specified.")
        return
        
    chart = chart_class(title=f"{symbol} {time_series.value} from {beginning_date} to {end_date}")
    data = parseStockEntryKeys(filtered_data)
    
    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    
    for entry in data:
        dates.append(entry.get("date"))
        opens.append(entry.get("open"))
        highs.append(entry.get("high"))
        lows.append(entry.get("low"))
        closes.append(entry.get("close"))

    chart.x_labels = dates
    chart.add("Open", opens)
    chart.add("High", highs)
    chart.add("Low", lows)
    chart.add("Close", closes)
    
    try:
        chart.render_in_browser()
    except Exception as e:
        print(f"An error occurred while rendering the chart in the browser: {e}")
    
