
import pandas as pd

def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df['occupancy_rate'] = df['room_booked'] / df['room_available']
    prophet_df = df[['date', 'occupancy_rate']].rename(columns={'date': 'ds', 'occupancy_rate': 'y'})
    return df, prophet_df
