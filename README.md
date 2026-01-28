# A/B Testing Analysis for Marketing Campaigns

This project performs a **complete statistical A/B testing analysis** to compare two marketing campaigns using real performance metrics. It applies multiple hypothesis tests and ends with a clear, data-driven business decision.

---

## 📌 Project Objective

To decide whether **Campaign B** should be launched by comparing it against **Campaign A** using:

* Conversion performance
* Cost efficiency
* Funnel behavior

The decision is based on **statistical significance**, not assumptions.

---

## 🛠️ Tools & Libraries

* **Python**
* **Pandas** – data cleaning and feature engineering
* **NumPy** – numerical operations
* **Matplotlib** – visual comparison
* **SciPy** – T-test and Chi-Square test
* **Statsmodels** – Z-test for proportions

---

## 📂 Dataset

**Input File:** `test_group.csv`

**Separator:** `;`

### Required Columns

* `Campaign Name`
* `# of Impressions`
* `# of Website Clicks`
* `# of Add to Cart`
* `# of Purchase`
* `Spend [USD]`

---

## 🔄 Analysis Workflow

### 1. Data Cleaning

* Trim column names
* Handle division-by-zero cases
* Remove infinite values

---

### 2. Feature Engineering

Calculated performance metrics:

* **CTR (Click Through Rate)**
* **Conversion Rate**
* **Cost per Purchase**

---

### 3. Campaign Segmentation

* Data split into **Campaign A** and **Campaign B**
* Row counts validated before testing

---

### 4. Statistical Tests Applied

#### 🔹 Z-Test (Conversion Rate)

* Compares purchase conversion proportions
* Input: purchases vs website clicks

#### 🔹 Independent T-Test (Cost Efficiency)

* Compares average cost per purchase
* Welch’s t-test applied (unequal variance)

#### 🔹 Chi-Square Test (Funnel Behavior)

* Tests dependency between add-to-cart and purchases
* Measures funnel improvement

---

### 5. Visual Comparison

* Bar chart: **Average Conversion Rate**
* Bar chart: **Average Cost per Purchase**

---

### 6. Final Decision Logic

Significance level:

```
α = 0.05
```

Campaign B is approved **only if all three tests are statistically significant**:

* Z-test p-value < 0.05
* T-test p-value < 0.05
* Chi-square p-value < 0.05

---

## 📊 Output & Interpretation

### Possible Outcomes

✅ **LAUNCH Campaign B**
Reason:

* Higher conversion rate
* Lower cost per purchase
* Improved funnel behavior

❌ **DO NOT LAUNCH Campaign B**
Reason:

* No statistically significant improvement

---

## 📈 Visual Outputs

* Conversion rate comparison
* Cost per purchase comparison

These visuals help stakeholders quickly understand performance differences.

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib scipy statsmodels
   ```
3. Place `test_group.csv` in the project directory
4. Run the Python script

---

## 📌 Use Cases

* Marketing A/B testing
* Performance-based campaign launch decisions
* Experiment-driven growth strategy
* Portfolio project for Data Science roles

---

## 👤 Author

**Khubaib**
Aspiring AI Engineer | Data Science & Experimentation

---

## ⭐ Notes

* Always validate sample sizes before testing
* Statistical significance does not guarantee business impact
* Combine test results with domain knowledge

---

If you find this project useful, feel free to ⭐ the repository and adapt it for your own A/B testing workflows.
