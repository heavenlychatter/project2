from functions.chartFunctions import generateChart
from models.chart_types import ChartTypes
from models.time_series import TimeSeries

def main():
    try:
        generateChart(symbol="IBM", chart_type=ChartTypes.LINE, time_series=TimeSeries.TIME_SERIES_MONTHLY, beginning_date="2023-01-01", end_date="2024-04-02")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()    
    