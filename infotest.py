# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 08:07:26 2025

@author: mirud
"""

import pandas as pd
from edgartools import edgar_conn

# Set your identity (as required by the SEC's programmatic access policy)
# More info: https://www.sec.gov/os/accessing-edgar-data
edgar_conn.set_identity("Your Name", "miruddfan@gmail.com")

# Download and parse the latest 10-Q filing for Apple (AAPL)
try:
    filing = edgar_conn.get_latest_filing("DOW", "10-Q")

    # Access numerical financial data as a pandas DataFrame
    # This will contain the structured XBRL facts
    financial_data = filing.xbrl.facts
    print(financial_data.head())
    print("Main branch: EDGAR connection test successful.")
    print ("Testing branching")


    # You can save this to a CSV or Excel file if needed
    # financial_data.to_csv("AAPL_latest_10Q_data.csv")

except Exception as e:
    print(f"An error occurred: {e}")