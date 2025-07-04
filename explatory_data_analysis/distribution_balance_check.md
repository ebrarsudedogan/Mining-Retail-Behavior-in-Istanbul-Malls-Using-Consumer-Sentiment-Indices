# Distribution and Balance Check


```python
import pandas as pd

df = pd.read_csv('../datasets/customer_shopping_data_v14.csv')
```

gender


```python
col = "gender"

# Calculate proportions
counts = df[col].value_counts(normalize=True)
counts_percent = counts * 100

# Determine balanced/imbalanced
threshold = 80  # Percent
max_ratio = counts_percent.max()
if max_ratio > threshold:
    balance_label = "Imbalanced distribution"
else:
    balance_label = "Balanced distribution"

# Print results
print(f"===== {col.upper()} =====")
for category, pct in counts_percent.items():
    print(f"{category}: {pct:.2f}%")
print(f"Max class ratio: {max_ratio:.2f}% (Threshold: {threshold}%)")
print(f"Result: {balance_label}")

```

    ===== GENDER =====
    Female: 59.81%
    Male: 40.19%
    Max class ratio: 59.81% (Threshold: 80%)
    Result: Balanced distribution


age


```python
import pandas as pd
from scipy.stats import skew

col = "age"

# Descriptive stats
desc = df[col].describe()
skewness_value = skew(df[col])

# Skewness interpretation
if abs(skewness_value) < 0.5:
    skew_label = "Approximately symmetric distribution"
elif abs(skewness_value) < 1:
    skew_label = "Moderate skewness"
else:
    skew_label = "High skewness"

# Print results
print(f"===== {col.upper()} =====")
print(f"Count: {desc['count']}")
print(f"Min: {desc['min']:.2f}")
print(f"Max: {desc['max']:.2f}")
print(f"Mean: {desc['mean']:.2f}")
print(f"Std: {desc['std']:.2f}")
print(f"Skewness: {skewness_value:.2f}")
print(f"Interpretation: {skew_label}")

```

    ===== AGE =====
    Count: 99457.0
    Min: 18.00
    Max: 69.00
    Mean: 43.43
    Std: 14.99
    Skewness: 0.01
    Interpretation: Approximately symmetric distribution


category


```python
col = "category"

# Calculate proportions
counts = df[col].value_counts(normalize=True)
counts_percent = counts * 100

# Determine balanced/imbalanced
threshold = 80
max_ratio = counts_percent.max()
if max_ratio > threshold:
    balance_label = "Imbalanced distribution"
else:
    balance_label = "Balanced distribution"

# Print results
print(f"===== {col.upper()} =====")
for category, pct in counts_percent.items():
    print(f"{category}: {pct:.2f}%")
print(f"Max class ratio: {max_ratio:.2f}% (Threshold: {threshold}%)")
print(f"Result: {balance_label}")

```

    ===== CATEGORY =====
    Clothing: 34.68%
    Cosmetics: 15.18%
    Food & Beverage: 14.86%
    Toys: 10.14%
    Shoes: 10.09%
    Souvenir: 5.03%
    Technology: 5.02%
    Books: 5.01%
    Max class ratio: 34.68% (Threshold: 80%)
    Result: Balanced distribution


quantity


```python
col = "quantity"

# Descriptive stats
desc = df[col].describe()
skewness_value = skew(df[col])

# Skewness interpretation
if abs(skewness_value) < 0.5:
    skew_label = "Approximately symmetric distribution"
elif abs(skewness_value) < 1:
    skew_label = "Moderate skewness"
else:
    skew_label = "High skewness"

# Print results
print(f"===== {col.upper()} =====")
print(f"Count: {desc['count']}")
print(f"Min: {desc['min']:.2f}")
print(f"Max: {desc['max']:.2f}")
print(f"Mean: {desc['mean']:.2f}")
print(f"Std: {desc['std']:.2f}")
print(f"Skewness: {skewness_value:.2f}")
print(f"Interpretation: {skew_label}")

```

    ===== QUANTITY =====
    Count: 99457.0
    Min: 1.00
    Max: 5.00
    Mean: 3.00
    Std: 1.41
    Skewness: -0.00
    Interpretation: Approximately symmetric distribution


price


```python
col = "price"

desc = df[col].describe()
skewness_value = skew(df[col])

if abs(skewness_value) < 0.5:
    skew_label = "Approximately symmetric distribution"
elif abs(skewness_value) < 1:
    skew_label = "Moderate skewness"
else:
    skew_label = "High skewness"

print(f"===== {col.upper()} =====")
print(f"Count: {desc['count']}")
print(f"Min: {desc['min']:.2f}")
print(f"Max: {desc['max']:.2f}")
print(f"Mean: {desc['mean']:.2f}")
print(f"Std: {desc['std']:.2f}")
print(f"Skewness: {skewness_value:.2f}")
print(f"Interpretation: {skew_label}")

```

    ===== PRICE =====
    Count: 99457.0
    Min: 5.23
    Max: 5250.00
    Mean: 689.26
    Std: 941.18
    Skewness: 2.25
    Interpretation: High skewness


payment_method


```python
col = "payment_method"

counts = df[col].value_counts(normalize=True)
counts_percent = counts * 100

threshold = 80
max_ratio = counts_percent.max()
if max_ratio > threshold:
    balance_label = "Imbalanced distribution"
else:
    balance_label = "Balanced distribution"

print(f"===== {col.upper()} =====")
for cat, pct in counts_percent.items():
    print(f"{cat}: {pct:.2f}%")
print(f"Max class ratio: {max_ratio:.2f}% (Threshold: {threshold}%)")
print(f"Result: {balance_label}")

```

    ===== PAYMENT_METHOD =====
    Cash: 44.69%
    Credit Card: 35.12%
    Debit Card: 20.19%
    Max class ratio: 44.69% (Threshold: 80%)
    Result: Balanced distribution


shopping_mall


```python
col = "shopping_mall"

counts = df[col].value_counts(normalize=True)
counts_percent = counts * 100

max_ratio = counts_percent.max()
if max_ratio > threshold:
    balance_label = "Imbalanced distribution"
else:
    balance_label = "Balanced distribution"

print(f"===== {col.upper()} =====")
for cat, pct in counts_percent.items():
    print(f"{cat}: {pct:.2f}%")
print(f"Max class ratio: {max_ratio:.2f}%")
print(f"Result: {balance_label}")

```

    ===== SHOPPING_MALL =====
    Mall of Istanbul: 20.05%
    Kanyon: 19.93%
    Metrocity: 15.09%
    Metropol AVM: 10.22%
    Istinye Park: 9.83%
    Zorlu Center: 5.10%
    Cevahir AVM: 5.02%
    Forum Istanbul: 4.97%
    Viaport Outlet: 4.94%
    Emaar Square Mall: 4.84%
    Max class ratio: 20.05%
    Result: Balanced distribution


season


```python
col = "season"

counts = df[col].value_counts(normalize=True)
counts_percent = counts * 100

max_ratio = counts_percent.max()
if max_ratio > threshold:
    balance_label = "Imbalanced distribution"
else:
    balance_label = "Balanced distribution"

print(f"===== {col.upper()} =====")
for cat, pct in counts_percent.items():
    print(f"{cat}: {pct:.2f}%")
print(f"Max class ratio: {max_ratio:.2f}%")
print(f"Result: {balance_label}")

```

    ===== SEASON =====
    Winter: 29.93%
    Spring: 24.04%
    Summer: 23.22%
    Fall: 22.80%
    Max class ratio: 29.93%
    Result: Balanced distribution


is_weekday


```python
col = "is_weekday"

counts = df[col].value_counts(normalize=True)
counts_percent = counts * 100

max_ratio = counts_percent.max()
if max_ratio > threshold:
    balance_label = "Imbalanced distribution"
else:
    balance_label = "Balanced distribution"

print(f"===== {col.upper()} =====")
for cat, pct in counts_percent.items():
    print(f"{cat}: {pct:.2f}%")
print(f"Max class ratio: {max_ratio:.2f}%")
print(f"Result: {balance_label}")

```

    ===== IS_WEEKDAY =====
    1: 71.58%
    0: 28.42%
    Max class ratio: 71.58%
    Result: Balanced distribution


is_holiday


```python
col = "is_holiday"

counts = df[col].value_counts(normalize=True)
counts_percent = counts * 100

max_ratio = counts_percent.max()
if max_ratio > threshold:
    balance_label = "Imbalanced distribution"
else:
    balance_label = "Balanced distribution"

print(f"===== {col.upper()} =====")
for cat, pct in counts_percent.items():
    print(f"{cat}: {pct:.2f}%")
print(f"Max class ratio: {max_ratio:.2f}%")
print(f"Result: {balance_label}")

```

    ===== IS_HOLIDAY =====
    0: 69.04%
    1: 30.96%
    Max class ratio: 69.04%
    Result: Balanced distribution


indexes


```python
numeric_cols_df = [
    "Econ_Conf",
    "Cons_Conf",
    "RealSec_Conf",
    "total_price",
    "bloomberg_confidence",
    "oecd_confidence",
    "ipsos_confidence"
]

for col in numeric_cols_df:
    desc = df[col].describe()
    skewness_value = skew(df[col])

    if abs(skewness_value) < 0.5:
        skew_label = "Approximately symmetric distribution"
    elif abs(skewness_value) < 1:
        skew_label = "Moderate skewness"
    else:
        skew_label = "High skewness"

    print(f"===== {col.upper()} =====")
    print(f"Count: {desc['count']}")
    print(f"Min: {desc['min']:.2f}")
    print(f"Max: {desc['max']:.2f}")
    print(f"Mean: {desc['mean']:.2f}")
    print(f"Std: {desc['std']:.2f}")
    print(f"Skewness: {skewness_value:.2f}")
    print(f"Interpretation: {skew_label}\n")

numeric_cols_extra = [
    "Serv_Conf",
    "Retail_Conf",
    "Constr_Conf"
]

df_extra = pd.read_csv("../datasets/customer_shopping_data_v6.csv")
for col in numeric_cols_extra:
    desc = df_extra[col].describe()
    skewness_value = skew(df_extra[col])

    if abs(skewness_value) < 0.5:
        skew_label = "Approximately symmetric distribution"
    elif abs(skewness_value) < 1:
        skew_label = "Moderate skewness"
    else:
        skew_label = "High skewness"

    print(f"===== {col.upper()} =====")
    print(f"Count: {desc['count']}")
    print(f"Min: {desc['min']:.2f}")
    print(f"Max: {desc['max']:.2f}")
    print(f"Mean: {desc['mean']:.2f}")
    print(f"Std: {desc['std']:.2f}")
    print(f"Skewness: {skewness_value:.2f}")
    print(f"Interpretation: {skew_label}\n")

```

    ===== ECON_CONF =====
    Count: 99457.0
    Min: 92.97
    Max: 104.35
    Mean: 98.29
    Std: 3.02
    Skewness: 0.19
    Interpretation: Approximately symmetric distribution
    
    ===== CONS_CONF =====
    Count: 99457.0
    Min: 63.36
    Max: 86.65
    Mean: 75.59
    Std: 5.81
    Skewness: -0.13
    Interpretation: Approximately symmetric distribution
    
    ===== REALSEC_CONF =====
    Count: 99457.0
    Min: 100.20
    Max: 113.30
    Mean: 107.17
    Std: 4.05
    Skewness: -0.26
    Interpretation: Approximately symmetric distribution
    
    ===== TOTAL_PRICE =====
    Count: 99457.0
    Min: 5.23
    Max: 26250.00
    Mean: 2528.79
    Std: 4222.48
    Skewness: 2.87
    Interpretation: High skewness
    
    ===== BLOOMBERG_CONFIDENCE =====
    Count: 99457.0
    Min: 45.32
    Max: 77.81
    Mean: 59.41
    Std: 9.05
    Skewness: 0.09
    Interpretation: Approximately symmetric distribution
    
    ===== OECD_CONFIDENCE =====
    Count: 99457.0
    Min: 93.29
    Max: 98.87
    Mean: 96.22
    Std: 1.68
    Skewness: -0.11
    Interpretation: Approximately symmetric distribution
    
    ===== IPSOS_CONFIDENCE =====
    Count: 99457.0
    Min: 27.00
    Max: 34.40
    Mean: 30.52
    Std: 2.29
    Skewness: 0.42
    Interpretation: Approximately symmetric distribution
    
    ===== SERV_CONF =====
    Count: 99457.0
    Min: 100.40
    Max: 121.66
    Mean: 114.63
    Std: 6.39
    Skewness: -1.10
    Interpretation: High skewness
    
    ===== RETAIL_CONF =====
    Count: 99457.0
    Min: 100.88
    Max: 127.47
    Mean: 116.04
    Std: 7.05
    Skewness: -0.42
    Interpretation: Approximately symmetric distribution
    
    ===== CONSTR_CONF =====
    Count: 99457.0
    Min: 77.30
    Max: 93.63
    Mean: 86.48
    Std: 4.81
    Skewness: -0.04
    Interpretation: Approximately symmetric distribution
    

