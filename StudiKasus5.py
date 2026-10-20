import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=== 1. PERSIAPAN DATA DASHBOARD KPI (USER PERSONA: BUDI) ===")
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", periods=30, freq="D")

data = {
    'Date': dates,
    'Daily_Transactions': np.random.randint(1200, 3500, size=30),
    'System_Response_Time_Sec': np.random.uniform(0.5, 3.5, size=30),
    'User_Satisfaction_Score': np.random.uniform(3.5, 5.0, size=30)
}

df_kpi = pd.DataFrame(data)
df_kpi['Is_Anomaly'] = df_kpi['System_Response_Time_Sec'] > 2.8

print("5 Baris Pertama Data KPI:")
print(df_kpi.head(), "\n")

print("=== 2. RINGKASAN STATISTIK KPI ===")
print(f"Rata-rata Transaksi Harian : {df_kpi['Daily_Transactions'].mean():.2f}")
print(f"Rata-rata Response Time    : {df_kpi['System_Response_Time_Sec'].mean():.2f} detik")
print(f"Jumlah Hari dengan Anomali : {df_kpi['Is_Anomaly'].sum()} hari\n")

print("=== 3. MEMBUAT VISUALISASI INTERAKTIF DASHBOARD ===")
plt.figure(figsize=(12, 6))

plt.plot(df_kpi['Date'], df_kpi['Daily_Transactions'], label='Daily Transactions', color='blue', marker='o', linewidth=2)

anomalies = df_kpi[df_kpi['Is_Anomaly']]
plt.scatter(anomalies['Date'], anomalies['Daily_Transactions'], color='red', s=100, zorder=5, label='Performance Anomaly (>2.8s)')

plt.title("Dashboard KPI Interaktif - Tren Transaksi & Anomali Sistem", fontsize=14, fontweight='bold')
plt.xlabel("Tanggal", fontsize=12)
plt.ylabel("Jumlah Transaksi", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("kpi_dashboard_visualization.png")
print("Visualisasi berhasil disimpan sebagai 'kpi_dashboard_visualization.png'")

df_kpi.to_csv("kpi_dashboard_data.csv", index=False)
print("Data KPI berhasil diexport ke 'kpi_dashboard_data.csv'")