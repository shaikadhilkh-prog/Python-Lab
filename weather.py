import json
import pandas as pd

# 1. Sample Nested JSON Dataset (Simulating a Weather API Response)
weather_json_data = """
[
    {
        "location": {"city": "New York", "country": "US", "coordinates": {"lat": 40.71, "lon": -74.00}},
        "current": {"temp_c": 18.5, "humidity": 64, "condition": "Clear"},
        "forecast": {"high_c": 22.0, "low_c": 14.0}
    },
    {
        "location": {"city": "London", "country": "UK", "coordinates": {"lat": 51.50, "lon": -0.12}},
        "current": {"temp_c": 12.0, "humidity": 82, "condition": "Rainy"},
        "forecast": {"high_c": 14.5, "low_c": 9.0}
    },
    {
        "location": {"city": "Tokyo", "country": "JP", "coordinates": {"lat": 35.67, "lon": 139.65}},
        "current": {"temp_c": 21.0, "humidity": 55, "condition": "Cloudy"},
        "forecast": {"high_c": 24.0, "low_c": 17.5}
    }
]
"""

def process_weather_data():
    # Load the JSON string into a Python list of dictionaries
    raw_data = json.loads(weather_json_data)
    
    # 2. Flatten the nested JSON structure into a tabular DataFrame
    # pd.json_normalize automatically breaks down nested structures using a separator (default is '.')
    df = pd.json_normalize(raw_data)
    
    print("--- Full Tabular Weather DataFrame ---")
    print(df.to_string(index=False))
    print("\n" + "="*50 + "\n")
    
    # 3. Extract and Rename Specific Columns for the Summary Report
    summary_df = df[[
        'location.city', 
        'location.country', 
        'current.temp_c', 
        'current.humidity', 
        'current.condition'
    ]].copy()
    
    summary_df.columns = ['City', 'Country', 'Temperature (°C)', 'Humidity (%)', 'Condition']
    
    # 4. Display Summarized Weather Report
    print("--- Summarized Weather Report ---")
    print(summary_df.to_string(index=False))
    
    # Optional: Calculate basic summary metrics across cities
    avg_temp = summary_df['Temperature (°C)'].mean()
    print("\n--- Quick Insights ---")
    print(f"Average Temperature across cities: {avg_temp:.1f}°C")

if __name__ == "__main__":
    process_weather_data()
