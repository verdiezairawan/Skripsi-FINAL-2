#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import numpy as np

def test_coingecko_direct():
    """Test langsung ke CoinGecko API untuk melihat data mentah"""
    print("Testing CoinGecko API directly...")
    
    try:
        # Test OHLC API
        print("\n=== Testing OHLC API ===")
        ohlc_url = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=7"
        response = requests.get(ohlc_url, timeout=10)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Data length: {len(data)}")
            print(f"First 3 records:")
            for i, record in enumerate(data[:3]):
                print(f"  {i}: {record}")
            
            # Parse data
            ohlc_df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close'])
            ohlc_df['Date'] = pd.to_datetime(ohlc_df['timestamp'], unit='ms')
            ohlc_df = ohlc_df.set_index('Date')
            ohlc_df = ohlc_df.drop('timestamp', axis=1)
            
            print(f"\nParsed DataFrame shape: {ohlc_df.shape}")
            print(f"Columns: {ohlc_df.columns.tolist()}")
            print(f"Data types: {ohlc_df.dtypes}")
            print(f"First few rows:")
            print(ohlc_df.head())
            
            # Check if values are different
            print(f"\nValue ranges:")
            print(f"Open range: {ohlc_df['open'].min():.2f} - {ohlc_df['open'].max():.2f}")
            print(f"High range: {ohlc_df['high'].min():.2f} - {ohlc_df['high'].max():.2f}")
            print(f"Low range: {ohlc_df['low'].min():.2f} - {ohlc_df['low'].max():.2f}")
            print(f"Close range: {ohlc_df['close'].min():.2f} - {ohlc_df['close'].max():.2f}")
            
            # Check if values are the same
            if ohlc_df['open'].equals(ohlc_df['high']) and ohlc_df['high'].equals(ohlc_df['low']) and ohlc_df['low'].equals(ohlc_df['close']):
                print("\n❌ PROBLEM: All OHLC values are the same!")
            else:
                print("\n✅ SUCCESS: OHLC values are different (as expected)")
            
            # Test resampling
            print(f"\n=== Testing Resampling ===")
            if len(ohlc_df) > 1:
                df_daily = ohlc_df.resample('D').agg({
                    'open': 'first',
                    'high': 'max',
                    'low': 'min',
                    'close': 'last'
                })
                print(f"After daily resampling: {df_daily.shape}")
                print(f"Daily data:")
                print(df_daily)
                
                # Check if daily values are different
                if df_daily['open'].equals(df_daily['high']) and df_daily['high'].equals(df_daily['low']) and df_daily['low'].equals(df_daily['close']):
                    print("\n❌ PROBLEM: Daily OHLC values are the same!")
                else:
                    print("\n✅ SUCCESS: Daily OHLC values are different")
            else:
                print("Not enough data for resampling")
                
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Exception: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_coingecko_direct() 