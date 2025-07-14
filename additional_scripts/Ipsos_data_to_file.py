#written for create the csv file with ipsos data

import csv

data = [
    ("2021-01", 31.7),
    ("2021-02", 32.0),
    ("2021-03", 33.6),
    ("2021-04", 32.0),
    ("2021-05", 30.0),
    ("2021-06", 28.5),
    ("2021-07", 30.0),
    ("2021-08", 28.7),
    ("2021-09", 29.4),
    ("2021-10", 28.9),
    ("2021-11", 30.3),
    ("2021-12", 28.7),
    ("2022-01", 29.3),
    ("2022-02", 29.2),
    ("2022-03", 30.2),
    ("2022-04", 28.5),
    ("2022-05", 29.3),
    ("2022-06", 28.0),
    ("2022-07", 27.0),
    ("2022-08", 27.0),
    ("2022-09", 30.6),
    ("2022-10", 33.9),
    ("2022-11", 34.1),
    ("2022-12", 34.4),
    ("2023-01", 34.0),
    ("2023-02", 34.4),
    ("2023-03", 31.6)
]

with open('../datasets/ipsos_cons_conf_index.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "PCSI"])
    writer.writerows(data)

print("CSV dosyası oluşturuldu: ipsos_cons_conf_index.csv")
