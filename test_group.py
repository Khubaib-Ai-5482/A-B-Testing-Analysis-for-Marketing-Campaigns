import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, chi2_contingency
from statsmodels.stats.proportion import proportions_ztest

df = pd.read_csv("test_group.csv", sep=";")

df.columns = df.columns.str.strip()

df["CTR"] = df["# of Website Clicks"] / df["# of Impressions"]
df["Conversion_Rate"] = df["# of Purchase"] / df["# of Website Clicks"]
df["Cost_per_Purchase"] = df["Spend [USD]"] / df["# of Purchase"]

df.replace([np.inf, -np.inf], np.nan, inplace=True)

campaign_a = df[df["Campaign Name"] == "Campaign_A"]
campaign_b = df[df["Campaign Name"] == "Campaign_B"]

print("Campaign A rows:", len(campaign_a))
print("Campaign B rows:", len(campaign_b))

success = [
    campaign_a["# of Purchase"].sum(),
    campaign_b["# of Purchase"].sum()
]
visitors = [
    campaign_a["# of Website Clicks"].sum(),
    campaign_b["# of Website Clicks"].sum()
]

z_stat, p_ztest = proportions_ztest(success, visitors)
print("\nZ-Test")
print("Z-Stat:", z_stat)
print("P-Value:", p_ztest)

t_stat, p_ttest = ttest_ind(
    campaign_a["Cost_per_Purchase"].dropna(),
    campaign_b["Cost_per_Purchase"].dropna(),
    equal_var=False
)
print("\nT-Test")
print("T-Stat:", t_stat)
print("P-Value:", p_ttest)

contingency_table = [
    [campaign_a["# of Add to Cart"].sum(), campaign_a["# of Purchase"].sum()],
    [campaign_b["# of Add to Cart"].sum(), campaign_b["# of Purchase"].sum()]
]

chi2, p_chi, dof, expected = chi2_contingency(contingency_table)
print("\nChi-Square Test")
print("Chi2:", chi2)
print("P-Value:", p_chi)

plt.figure()
plt.bar(["Campaign A", "Campaign B"], [
    campaign_a["Conversion_Rate"].mean(),
    campaign_b["Conversion_Rate"].mean()
])
plt.title("Average Conversion Rate")
plt.ylabel("Conversion Rate")
plt.show()

plt.figure()
plt.bar(["Campaign A", "Campaign B"], [
    campaign_a["Cost_per_Purchase"].mean(),
    campaign_b["Cost_per_Purchase"].mean()
])
plt.title("Average Cost per Purchase")
plt.ylabel("USD")
plt.show()

alpha = 0.05
print("\nFINAL DECISION:")

if (p_ztest < alpha) and (p_ttest < alpha) and (p_chi < alpha):
    print("✅ LAUNCH Campaign B")
    print("Reason: Better conversion, lower cost, improved funnel")
else:
    print("❌ DO NOT LAUNCH Campaign B")
    print("Reason: No statistically significant improvement")