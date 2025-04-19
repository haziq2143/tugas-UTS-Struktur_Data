import pandas as pd

url = "https://docs.google.com/spreadsheets/d/17ru4XAU2NloE9Dfxr2PC1BVcsYkLLT5r7nPSsiOFlvQ/export?format=csv&gid=743838712"

df = pd.read_csv(url)

df['Judul Paper'] = df['Judul Paper'].astype(str)
df['Tahun Terbit'] = df['Tahun Terbit'].astype(str)
df['Nama Penulis'] = df['Nama Penulis'].astype(str)
df['NIM'] = df['NIM'].astype(str)
df['Nama Mahasiswa'] = df['Nama Mahasiswa'].astype(str)
df['Abstrak (langusung copas dari paper)'] = df['Abstrak (langusung copas dari paper)'].astype(str)
df['Kesimpulan (Langusung copas dari paper)'] = df['Kesimpulan (Langusung copas dari paper)'].astype(str)



def linear_search(df, key, value):
    return df[df[key].str.lower() == value.lower()]

def binary_search(df, key, value):
    df_sorted = df.sort_values(by=key, key=lambda x: x.str.lower()).reset_index(drop=True)
    low = 0
    high = len(df_sorted) - 1
    value = value.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_value = df_sorted.loc[mid, key].lower()

        if mid_value == value:
            return df_sorted.loc[[mid]]
        elif value < mid_value:
            high = mid - 1
        else:
            low = mid + 1

    return pd.DataFrame()  

def tampilkan_hasil(hasil):
    if hasil.empty:
        print("Data tidak ditemukan.")
    else:
        for index, row in hasil.iterrows():
            print(f"Judul  : {row['Judul Paper']}")
            print(f"Tahun  : {row['Tahun Terbit']}")
            print(f"Penulis: {row['Nama Penulis']}")
            print(f"NIM: {row['NIM']}")
            print(f"Nama Mahasiswa: {row['Nama Mahasiswa']}")
            print(f"Abstract: {row['Abstrak (langusung copas dari paper)']}")
            print(f"Kesimpulan: {row['Kesimpulan (Langusung copas dari paper)']}")
            print("-" * 40)
            
menu = 3
while menu != 5:
    print("Masukkan Kolom:\n1.Judul Paper\n2.Nama Penulis\n3.Tahun Terbit")
    kolomMenu = int(input("Masukkan Kolom Menu: "))

    if kolomMenu == 1:
        kolom = "Judul Paper"
        nilai =  input("Masukkan Judul Paper: ")
        break
    elif kolomMenu == 2:
        kolom = "Nama Penulis"
        nilai =  input("Masukkan Nama Penulis: ")
        break
    elif kolomMenu == 3:
        kolom = "Tahun Terbit"
        tempt =  input("Masukkan Tahun Terbit: ")
        nilai = f"{tempt}.0"
        break
    else:
        print('Pilihan Invalid, selesai')
        break

print("=== Linear Search ===")
tampilkan_hasil(linear_search(df, kolom, nilai))

print("\n=== Binary Search ===")
tampilkan_hasil(binary_search(df, kolom, nilai))