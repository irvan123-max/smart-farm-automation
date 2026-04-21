import pandas as pd
import matplotlib.pyplot as plt
import datetime
from config import TARGET

class SmartFarm:
    def __init__(self, file_name, nama_farm):
        self.file_name = file_name
        self.nama_farm = nama_farm
        self.df = None

    # ===== LOAD DATA =====
    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_name)
            self.df["Telur"] = pd.to_numeric(self.df["Telur"], errors="coerce")
            self.df = self.df.dropna()
        except FileNotFoundError:
            print("X File tidak ditemukan!")
            exit()

    # ===== ANALISIS =====
    def analyze(self):
        self.total = self.df["Telur"].sum()
        self.rata = self.df["Telur"].mean()
        self.max_val = self.df["Telur"].max()
        self.min_val = self.df["Telur"].min()

        self.best_day = self.df.loc[self.df["Telur"].idxmax()]
        self.worst_day = self.df.loc[self.df["Telur"].idxmin()]

    # ===== GRAFIK =====
    def create_chart(self):
        plt.figure()

        plt.plot(self.df["Hari"], self.df["Telur"], marker='o')

        plt.title(f"Produksi Telur - {self.nama_farm}")
        plt.xlabel("Hari")
        plt.ylabel("Jumlah Telur")

        plt.axhline(y=TARGET)
        plt.grid()

        self.chart_file = f"grafik_{datetime.date.today()}.png"
        plt.savefig(self.chart_file)
        plt.close()

    # ===== REPORT =====
    def generate_report(self):
        now = datetime.datetime.now()
        file_name = f"report_{now.date()}.txt"

        with open(file_name, "w") as file:
            file.write("=== LAPORAN PRODUKSI ===\n")
            file.write(f"Farm: {self.nama_farm}\n")
            file.write(f"Tanggal : {now}\n\n")

            file.write(f"Total Produksi : {self.total}\n")
            file.write(f"Rata-rata      : {self.rata:.2f}\n")
            file.write(f"Tertinggi      : {self.max_val}\n")
            file.write(f"Terendah       : {self.min_val}\n\n")

            file.write("=== ANALISIS ===\n")
            file.write(f"Hari terbaik   : {self.best_day['Hari']} ({self.best_day['Telur']})\n")
            file.write(f"Hari terburuk  : {self.worst_day['Hari']} ({self.worst_day['Telur']})\n")

            if self.rata < 70:
                file.write("\n PRODUKSI BURUK\n")

        print(f"Report dibuat: {file_name}")

    # ===== RUN SYSTEM =====
    def run(self):
        self.load_data()
        self.analyze()
        self.create_chart()
        self.generate_report()