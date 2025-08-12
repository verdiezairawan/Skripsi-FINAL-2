#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit_app

def test_data_retrieval():
    print("Testing data retrieval from CoinGecko...")
    
    try:
        # Test dengan 7 hari
        print("\n=== Testing 7 days data ===")
        data, error = streamlit_app.get_coingecko_data(days=7)
        
        if error:
            print(f"Error: {error}")
            return
        
        if data is not None:
            print(f"Data shape: {data.shape}")
            print(f"Columns: {data.columns.tolist()}")
            print(f"First few rows:")
            print(data.head())
            print(f"\nData types:")
            print(data.dtypes)
            
            # Check if values are different
            print(f"\nValue ranges:")
            print(f"Open range: {data['Open'].min():.2f} - {data['Open'].max():.2f}")
            print(f"High range: {data['High'].min():.2f} - {data['High'].max():.2f}")
            print(f"Low range: {data['Low'].min():.2f} - {data['Low'].max():.2f}")
            print(f"Close range: {data['Close'].min():.2f} - {data['Close'].max():.2f}")
            
            # Check if values are the same (this should not happen)
            if data['Open'].equals(data['High']) and data['High'].equals(data['Low']) and data['Low'].equals(data['Close']):
                print("\n❌ PROBLEM: All OHLC values are the same!")
            else:
                print("\n✅ SUCCESS: OHLC values are different (as expected)")
                
        else:
            print("No data returned")
            
    except Exception as e:
        print(f"Exception occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_data_retrieval() 