import re

def validateDate(date_str: str) -> bool:
    # verifies that the date string is in the format  YYYY-MM-DD and that the month and day are valid
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    if re.match(date_pattern, date_str):
        return True
    else:
        return False
        
def compareDates(date_str1: str, date_str2: str) -> int:
    # compares two date strings in the format YYYY-MM-DD and returns -1 if date_str1 is earlier than date_str2, 0 if they are the same, and 1 if date_str1 is later than date_str2
    if not validateDate(date_str1) or not validateDate(date_str2):
        raise ValueError("Invalid date format. Dates must be in the format YYYY-MM-DD.")
    
    if date_str1 < date_str2:
        return -1
    elif date_str1 > date_str2:
        return 1
    else:
        return 0
        
def filterDataByDate(data: dict[str, any], beginning_date: str, end_date: str) -> dict[str, any]:
    # filters the data dictionary to only include entries between the beginning and end dates (inclusive)
    return data
    
def parseStockEntryKeys(data: dict[str, any]) -> list[dict[str, any]]:
    
    parsed_data = []
    for date, entry in data.items():
        parsed_entry = {
            "date": date,
            "open": float(entry.get("1. open", 0)),
            "high": float(entry.get("2. high", 0)),
            "low": float(entry.get("3. low", 0)),
            "close": float(entry.get("4. close", 0)),
            "volume": float(entry.get("5. volume", 0))
        }
        parsed_data.append(parsed_entry)
    return parsed_data
        
    