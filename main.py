import pandas as pd
from core.stock_processor import process_stock

# === Load daftar saham
df = pd.read_excel('data/stocks_name.xlsx')
data_stocks_name = df['stocks_name'] + '.JK'
data_final = []

# === Proses setiap saham
for stock_name in data_stocks_name:
    result, message = process_stock(stock_name)
    print(message)
    if result:
        data_final.append(result)

# === Simpan hasil
pd.DataFrame(data_final).to_excel("Output_Trend.xlsx", index=False)
print("Data trend berhasil disimpan di Output_Trend.xlsx")
