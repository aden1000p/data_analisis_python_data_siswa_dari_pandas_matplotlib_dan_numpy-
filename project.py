import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.system('cls')
df = pd.read_excel('./book2.xlsx')

def baris(n):
    print("=" * n)

while True:
    
    list = ['Lihat Perorangan', 'lihat dari masing masing kolom', 'lihat dari keseluruhan (max/min/mean/median/std/sum/count)', 'visualisasi data', 'pencarian nilai input','keluar']
    
    for i in range(10):
        baris(30)
        
        if i == 3:
            print("data Sisswa di smk Ngawi Inteligence")
            print(df)
            baris(30)
            for index,  i in enumerate(list):
                print(index + 1, i)

    guess = input("pilih mau menilai data mana? ")
    
    if guess == "lihat perorangan":
        data_siswa = map(int, input("masukan nomor siswa: ").split(','))
        print(df.iloc[data_siswa])
    elif guess == "lihat dari masing masing kolom":
        data_siswa = map(str, input("masukan nomor kolom: ").split(','))
        print(df[data_siswa])
    elif guess == "lihat dari keseluruhan":
        data_siswa = input("mau yang mana dulu (max/min/mean/median/std/sum/count)? ")
        df = df.describe()
        
        if data_siswa == "max":
            print('seluruh siswa max: \n', df.max())
        elif data_siswa == "min":
            print('seluruh siswa min \n', df.min())
        elif data_siswa == "mean":
            print('seluruh rata-rata:  \n', df.mean())
        elif data_siswa == "median":
            print("seluruh siswa median: \n", df.median())
        elif data_siswa == "std":
            print("jumlah seluruh siswa standar deviasi: \n", df.std())
        elif data_siswa == "sum":
            print("jumlah seluruh siswa yang ada: \n", df.sum())
        elif data_siswa == "count":
            print("jumlah seluruh data siswa: \n", df.count())
        else:
            print("tidak ada pilihan lain silahkna coba lagi!!!")
    
    elif guess == "visualisasi data":
        list = ['Lingkaran', 'Bar', 'Bar horizontal', 'Garis', 'Box plot', 'Scatter', 'histogram']
        for index, i in enumerate(list):
            print(index + 1, i)

        guess = input("silahkan pilih apa yang kamu mau: ")
        
        if guess == "lingkaran".lower():
            guess = input("mau individu atau kelompok: ")
            if guess == 'individu'.lower():
                pilihan = str(input("masukan kolom yang ada di data: "))
                plt.style.use('ggplot')
                df.index = df['nama']
                df.plot(kind='pie', y=f'{pilihan}', x=df.index, autopct='%1.1f%%', title="Data siswa dengan lingkaran", layout=[10, 10])
                plt.show()
            else:
                pilihan1 = str(input("masukan kolom yang ada di data: "))
                plt.style.use('ggplot')
                df.index = df['nama']
                df.plot(kind='pie', y=f'{pilihan1}', x=df.index, autopct='%1.1f%%', title="Data siswa dengan lingkaran", layout=[10, 10])
                plt.show()
                
        elif guess == "bar".lower():
            pilihan1 = str(input("masukan kolom yang ada di data: "))
            plt.style.use('seaborn-v0_8')
            df.plot(kind='bar', y=f'{pilihan1}', x='nama')
            plt.show()
        elif guess == "bar horizontal".lower():
            plt.style.use('bmh')
            df.plot(kind='barh', y='jumlah', x='nama')
            plt.show()
        elif guess == "garis".lower():
            plt.style.use('bmh')
            df.plot(kind='line', x='jumlah', y='rata-rata', label='nama')
            plt.legend()
            plt.show()
        elif guess == "box plot":
            plt.style.use('bmh')
            df['jumlah'].plot(kind='box')
            plt.legend()
            plt.show()
        elif guess == "scatter":
            df.plot(kind='scatter', x='jumlah', y='nama', marker='o')
            plt.show()
        elif guess == "histogram":
            df.plot(kind='hist', x='jumlah', bins=20)
            plt.grid()
            plt.show()
        
    elif guess == "pencarian nilai input":
        data_siswa = int(input("masukan angka yang kamu ketik maxmimal 1-1000: "))
        angka = df['jumlah'] > data_siswa
        print(df[angka])
    
    elif guess == "keluar":
        break
    
    else:
        print("menu tidak tersedia coba lagi")
        

