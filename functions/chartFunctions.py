from io import open_code
import json
from models import chart_types, time_series
from functions.utilFunctions import compareDates, filterDataByDate, parseStockEntryKeys
from functions.httpFunctions import makeAlphaVantageRequest
import pygal

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
    
    
    
    raw_data = request.get(key, {})
    if not raw_data:
        print("Error: No data found for the specified time series.")
        return
        
    filtered_data = filterDataByDate(raw_data, beginning_date, end_date)
    if not filtered_data:
        print("Error: No data found for the specified date range.")
        return
        
    with open(f"test.json", "w") as f:
        json.dump(filtered_data, f)
        
    chart = pygal.Line(title=f"{symbol} {chart_type.value} from {beginning_date} to {end_date}")
    data = parseStockEntryKeys(filtered_data)
    print(data[0])
    open_code = [entry.get("open") for entry in data]
    high_code = [entry.get("high") for entry in data]
    low_code = [entry.get("low") for entry in data]
    close_code = [entry.get("close") for entry in data]

    chart.add("Open", open_code)
    chart.add("High", high_code)
    chart.add("Low", low_code)
    chart.add("Close", close_code)

    chart.render_in_browser()
    



