import pandas as pd

def read_data(file_path):
    df = pd.read_csv(file_path)
    # remove "source," "ISO" & "CTS" related column, since they are all identical or doesn't contribute meaningfully
    df = df.drop(columns=['ISO2','ISO3','Source','CTS Code','CTS Name','CTS Full Descriptor'])
    # remove rows that contain "Percent of GDP" since they could be disruptive when doing spreadsheet analysis
    df = df[~df.astype(str).apply(lambda x: x.str.contains('Percent of GDP')).any(axis=1)]
    return df

def main():
    file_path = 'data/Fossil_Fuel_Subsidies.csv'
    try:
        df = read_data(file_path)
        print("Data loaded successfully.")
        df.to_csv('data/clean_data.csv', index=False)
        print("Clean data saved as clean_data.csv")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
