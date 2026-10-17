import sys
import pandas as pd
import numpy as np
import os

def process_sensor_data(input_path, output_path):
    print(f"[*] Membaca data dari: {input_path}")
    if not os.path.exists(input_path):
        print(f"[!] Error: File {input_path} tidak ditemukan.")
        return

    # Memuat dataset
    df = pd.read_csv(input_path)

    # Simulasi kalibrasi data sensor PM2.5 lokal
    print("[*] Melakukan kalibrasi dan pembersihan data...")
    df['pm25_adjusted'] = df['pm25_raw'] * 0.95 + 1.8

    # Kategorisasi status kualitas udara
    conditions = [
        (df['pm25_adjusted'] <= 35),
        (df['pm25_adjusted'] > 35) & (df['pm25_adjusted'] <= 75),
        (df['pm25_adjusted'] > 75)
    ]
    choices = ['Sehat', 'Sedang', 'Berbahaya']
    df['status_udara'] = np.select(conditions, choices, default='Tidak Diketahui')

    # Menyimpan hasil ke folder outputs
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[+] Pemrosesan selesai. Hasil disimpan di: {output_path}")

if __name__ == "__main__":
    input_file = "data/sensors_raw.csv"
    output_file = "outputs/processed_pm25_output.csv"
    process_sensor_data(input_file, output_file)