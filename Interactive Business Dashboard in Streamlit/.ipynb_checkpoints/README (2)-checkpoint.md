# Global Superstore — Interactive Business Dashboard

> **Task 5 | DevelopersHub Internship**

---

##  Task Objective

Develop an interactive Streamlit dashboard for analyzing **sales, profit, and segment-wise performance** using the Global Superstore dataset. The goal is to enable business stakeholders to explore KPIs through dynamic filters and rich visualizations.

---

##  Dataset

**Global Superstore Dataset**
- Contains transactional sales data from a global retail company
- Includes: Orders, Customers, Products, Regions, Sales, Profit, Discounts
- Source: [Kaggle — Global Super Store Dataset](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset)

---

##  My Approach

### 1. Data Cleaning & Preprocessing
- Loaded CSV with `latin1` encoding to handle special characters
- Parsed `Order Date` and `Ship Date` as datetime
- Dropped rows with missing `Sales` or `Profit`
- Engineered new features: `Year`, `Month`, `Profit Margin`, `Ship Days`

### 2. Exploratory Data Analysis (EDA)
- Analyzed sales and profit distributions
- Identified regional, category, and segment-level trends
- Examined discount vs profit relationship
- Ranked top customers by revenue

### 3. Streamlit Dashboard
Built an interactive dashboard with:
- **Sidebar filters**: Region, Category, Sub-Category, Year, Segment
- **KPI cards**: Total Sales, Profit, Orders, Units Sold, Avg Margin
- **Charts**: Monthly trends, regional bar charts, treemaps, pie charts, customer rankings, profit margin analysis

---

##  Results & Findings

| Insight | Finding |
|---|---|
|  Sales Trend | Consistent growth, peaks in Q4 |
|  Top Region | Central & APAC lead in sales |
|  Best Category | Technology has highest profit margins |
|  Problem Area | High discounts (>40%) cause losses |
|  Top Customer | Significant revenue from top 5 customers |
| Loss-making | Tables & Bookcases sub-categories run at a loss |

---

## How to Run

### Prerequisites
```bash
pip install streamlit pandas plotly numpy
```

### Run Dashboard
```bash
streamlit run dashboard.py
```

### Run Jupyter Notebook
Open `Global_Superstore_Analysis.ipynb` in Jupyter or VS Code

---

## File Structure

```
├── dashboard.py                      # Streamlit dashboard
├── Global_Superstore_Analysis.ipynb  # EDA Jupyter Notebook
├── Global_Superstore2.csv            # Dataset (not uploaded)
└── README.md                         # This file
```

---

## Tech Stack

- **Python** — Core language
- **Streamlit** — Dashboard framework
- **Plotly** — Interactive charts
- **Pandas / NumPy** — Data processing
- **Matplotlib / Seaborn** — EDA plots
