import streamlit_app

print("Testing get_coingecko_data...")
data, error = streamlit_app.get_coingecko_data(days=7)

if error:
    print(f"Error: {error}")
else:
    print(f"Success! Data shape: {data.shape}")
    print(f"Columns: {data.columns.tolist()}")
    if len(data) > 0:
        print(f"First row:")
        print(data.iloc[0])
        print(f"Open: {data.iloc[0]['Open']}")
        print(f"High: {data.iloc[0]['High']}")
        print(f"Low: {data.iloc[0]['Low']}")
        print(f"Close: {data.iloc[0]['Close']}")
    else:
        print("Data is empty!") 