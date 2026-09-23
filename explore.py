import pandas as pd
from scipy import stats

df = pd.read_csv('onca_sample_200_classified.csv')

# Group citing_cases_count by case_type
groups = [df[df['case_type'] == t]['citing_cases_count'].dropna() for t in df['case_type'].unique()]

f_stat, p_value = stats.f_oneway(*groups)
print(f"F-statistic: {f_stat:.3f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Result: statistically significant difference between case types")
else:
    print("Result: no statistically significant difference between case types")
    