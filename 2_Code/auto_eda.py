import pandas as pd
from ydata_profiling import ProfileReport
import os


def generate_eda(folder_path):
    print("Called")
    csv_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.csv')]
    if not csv_files:
        raise ValueError("No file matches in " + folder_path)

    i = 0
    for fname in csv_files[0:]:
        i += 1
        print(f"Started File {i}")
        file_path = os.path.join(folder_path, fname)
        df = pd.read_csv(file_path, low_memory=False)
        profile = ProfileReport(df, title="Auto-EDA")
        profile.to_file(os.path.join(folder_path, f"{i}_auto_eda.html"))
        print("File finished")
    print("Done All")


def combine_csvs(folder_path, output_filename="combined.csv"):
    csv_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.csv')]
    if not csv_files:
        raise ValueError("No file matches in " + folder_path)
    
    first_path = os.path.join(folder_path, csv_files[0])
    combined_df = pd.read_csv(first_path)

    for fname in csv_files[1:]:
        file_path = os.path.join(folder_path, fname)
        df = pd.read_csv(file_path, header=0)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    out_path = os.path.join(folder_path, output_filename)
    combined_df.to_csv(out_path, index=False)
    print(f"Combined {len(csv_files)} files into {out_path}")

generate_eda(r"D:\Summer Practicum\1. Data\On_Time_Marketing_Carrier_On_Time_Performance_Beginning_January_2018_2023_All_Months")
#combine_csvs(data_folder)
