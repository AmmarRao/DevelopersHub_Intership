# 🛒 Customer Segmentation using K-Means Clustering

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat-square&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=flat-square&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

> A machine learning project that segments mall customers into distinct groups based on their annual income and spending behavior using the **K-Means Clustering** algorithm, with **PCA** for visualization.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Marketing Strategies](#marketing-strategies)
- [Project Structure](#project-structure)
- [Author](#author)

---

## 📖 Overview

Customer segmentation helps businesses understand different customer types and design targeted marketing strategies. This project uses **K-Means Clustering** to group mall customers and **PCA** to visualize the clusters in 2D.

---

## 🎯 Problem Statement

The objective of this project is to segment customers into different groups based on their **spending behavior** and **income** using unsupervised learning techniques. These segments enable businesses to design targeted marketing strategies for each customer group.

---

## 📊 Dataset

**File:** `Mall_Customers.csv`

| Column | Description |
|--------|-------------|
| `CustomerID` | Unique customer identifier |
| `Genre` | Gender of the customer (Male/Female) |
| `Age` | Age of the customer |
| `Annual Income (k$)` | Annual income in thousands of dollars |
| `Spending Score (1-100)` | Score assigned by the mall based on spending behavior |

- **Total Records:** 200 customers (5 features)

**Key Stats:**
- Average Age: ~39 years (range: 18–70)
- Average Annual Income: ~$60.5k (range: $15k–$137k)
- Average Spending Score: ~50.2 (range: 1–99)

---

## 🔄 Project Workflow

```
Raw Data  →  EDA  →  Feature Selection  →  Scaling  →  Elbow Method  →  K-Means (k=5)  →  PCA  →  Cluster Analysis
```

**Steps:**
1. **Data Loading & Overview** — `data.head()`, `data.shape`, `data.describe()`
2. **EDA** — Gender distribution, Age histogram, Income vs Spending scatter plot
3. **Feature Selection** — `Annual Income (k$)` and `Spending Score (1-100)`
4. **Feature Scaling** — `StandardScaler` (zero mean, unit variance)
5. **Optimal K** — Elbow Method (WCSS for k=1 to 10) → **k=5**
6. **K-Means Clustering** — `KMeans(n_clusters=5, random_state=42)`
7. **PCA Visualization** — Reduced to 2 components (100% variance retained)
8. **Cluster Analysis** — Mean values per cluster

---

## 🛠️ Technologies Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical computations |
| `matplotlib` | Data visualization |
| `seaborn` | Statistical plots (countplot, histplot, scatterplot) |
| `scikit-learn` | KMeans, StandardScaler, PCA |

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/AmmarRao/Customer_Segmentation_KMeans.git
cd Customer_Segmentation_KMeans
```

**2. Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```

**3. Install dependencies**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## ▶️ Usage

**1.** Make sure `Mall_Customers.csv` is in the root folder.

**2.** Open and run the notebook:

```bash
jupyter notebook Customer_Segmentation__K-Means_.ipynb
```

---

## 📈 Results

The Elbow Method confirmed **k=5** as the optimal number of clusters. K-Means identified **5 distinct customer segments**:

| Cluster | Size | Avg Income | Avg Spending | Profile |
|---------|------|------------|--------------|---------|
| **0** | 81 | $55.3k | 49.5 | Medium income, medium spending |
| **1** | 39 | $86.5k | 82.1 | High income, high spending ⭐ |
| **2** | 22 | $25.7k | 79.4 | Low income, high spending |
| **3** | 35 | $88.2k | 17.1 | High income, low spending |
| **4** | 23 | $26.3k | 20.9 | Low income, low spending |

PCA retained **100% of the variance** with 2 components, providing clear 2D cluster separation.

---

## 🎯 Marketing Strategies

| Cluster | Strategy |
|---------|----------|
| **High Income + High Spending (1)** | Premium offers, loyalty programs |
| **High Income + Low Spending (3)** | Encourage spending via exclusive deals |
| **Low Income + High Spending (2)** | Offer affordable luxury products |
| **Low Income + Low Spending (4)** | Discounts and promotions |
| **Medium Customers (0)** | General marketing campaigns |

---

## 📁 Project Structure

```
Customer_Segmentation_KMeans/
│
├── Mall_Customers.csv                         # Dataset
├── Customer_Segmentation__K-Means_.ipynb     # Main Jupyter Notebook
└── README.md                                  # Project documentation
```

---

## 👤 Author

**Muhammad Ammar Rao**
- GitHub: [@AmmarRao](https://github.com/AmmarRao)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*⭐ If you found this project helpful, consider giving it a star on GitHub!*
