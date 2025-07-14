#written for create the csv file with bloomberg data

import pandas as pd


bloomberg_data = pd.DataFrame({
    "year": [
        2020,2020,2020,2020,
        2021,2021,2021,2021,2021,2021,2021,2021,2021,
        2022,2022,
        2023,2023,2023,2023,2023,2023,2023,2023,2023,2023
    ],
    "month": [
        9,10,11,12,
        1,2,3,4,5,6,7,8,9,
        11,12,
        1,2,3,4,5,6,7,8,9,10
    ],
    "bloomberg_confidence":[
        71.27,66.10,61.52,67.44,
        72.55,69.03,65.10,57.35,55.20,62.99,65.07,60.06,61.49,
        62.74,72.39,
        74.42,70.27,77.81,78.90,75.13,75.90,58.84,65.32,64.98,72.08
    ]
})

bloomberg_data["month_str"] = (
    bloomberg_data["year"].astype(str) + "-" + bloomberg_data["month"].astype(str).str.zfill(2)
)

bloomberg_data.to_csv("../datasets/bloomberg_cons_conf_index.csv", index=False, encoding="utf-8-sig")

print("CSV dosyası başarıyla kaydedildi: bloomberg_cons_conf_index.csv")
