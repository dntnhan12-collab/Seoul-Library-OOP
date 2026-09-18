import pandas as pd

file_path = "data/서울시 공공도서관 현황정보.csv"

data = pd.read_csv(
    file_path,
    encoding="utf-8-sig"
)

print(data.head())
print(data.columns)
print(data.shape)