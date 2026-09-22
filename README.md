# 🛒 Supermarket Sales & Customer Analytics Dashboard

## 📌 Project Overview

The **Supermarket Sales & Customer Analytics Dashboard** is an interactive data analytics and business intelligence application developed using Python and Streamlit. The project analyzes supermarket transaction data to understand sales performance, customer purchasing behavior, product performance, profitability, payment preferences, branch performance, and sales trends.

The system transforms raw supermarket transaction data into meaningful **Key Performance Indicators (KPIs), visual insights, business trends, risks, opportunities, and actionable recommendations**. The dashboard is designed to help supermarket management understand overall business performance and support data-driven decision-making.

---

## 📖 Abstract

The **Supermarket Sales & Customer Analytics Dashboard** is an interactive data analytics and business intelligence application designed to help supermarket management understand and improve overall business performance. Supermarkets generate large volumes of transactional data related to products, sales, customers, quantities, revenue, costs, profits, payment methods, and locations, but raw data alone is difficult to interpret and use for decision-making. This project transforms raw supermarket transaction data into meaningful business insights through data cleaning, preprocessing, exploratory data analysis, KPI calculation, and interactive visualization. The dashboard provides key performance indicators such as total revenue, total transactions, total profit, average order value, and total quantity sold, along with detailed analysis of sales trends, product and category performance, customer purchasing behavior, payment methods, and location-wise performance. Interactive filters allow users to explore specific time periods, products, categories, customer groups, and other business dimensions. The system also identifies important trends, high- and low-performing areas, potential risks, and business opportunities from the analyzed data. Based on these findings, the dashboard presents actionable recommendations that can support decisions related to product management, customer engagement, sales improvement, and profitability. The project demonstrates how data analytics can convert raw supermarket data into clear, understandable, and actionable information, enabling management to make data-driven business decisions more effectively.

---

## 🎯 Problem Statement

Supermarkets generate a large amount of transactional data every day. However, raw transaction records are difficult to interpret directly and may not provide management with a clear understanding of business performance.

Management may need answers to questions such as:

* Which product categories generate the highest revenue?
* Which categories generate the highest profit?
* Which locations and branches perform better?
* Which customer groups contribute more revenue?
* Which payment methods are commonly used?
* How does revenue change over time?
* Which areas require attention?
* Where are potential business opportunities?
* What actions can improve sales and profitability?

This project addresses these challenges by providing an interactive dashboard that converts raw transaction data into meaningful insights and actionable recommendations.

---

## 🎯 Objectives

The main objectives of the project are:

1. Load and analyze supermarket transaction data.
2. Clean and preprocess the raw dataset.
3. Calculate important business KPIs.
4. Analyze sales and revenue trends.
5. Analyze product and category performance.
6. Analyze customer purchasing behavior.
7. Analyze payment method usage.
8. Compare branch and city performance.
9. Analyze revenue, profit, and profit margin.
10. Identify important business trends and patterns.
11. Identify potential risks and opportunities.
12. Generate data-based business recommendations.
13. Present all analysis through an interactive Streamlit dashboard.

---

## 📊 Dataset

The project uses a supermarket sales dataset containing:

* **1,000 transaction records**
* **17 columns**

### Main Dataset Fields

* Invoice ID
* Branch
* City
* Customer Type
* Gender
* Product Line
* Unit Price
* Quantity
* Tax
* Total
* Date
* Time
* Payment
* COGS
* Gross Margin Percentage
* Gross Income
* Rating

---

## 🔗 Dataset Source

The dataset used in this project is stored locally as:

```text
data/supermarket_sales.csv
```

Source:

https://raw.githubusercontent.com/selva86/datasets/master/supermarket_sales.csv

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Dashboard Framework

* Streamlit

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Plotly

---

## ✨ Main Features

### 1. Executive Overview

The dashboard provides a quick summary of supermarket performance through KPI cards.

The main KPIs are:

* Total Revenue
* Total Transactions
* Total Profit
* Average Order Value
* Total Quantity Sold
* Average Customer Rating
* Overall Profit Margin

---

### 2. Sales Performance Analysis

This section analyzes overall sales performance.

It includes:

* Monthly Revenue Trend
* Revenue by City
* Revenue by Product Category
* Revenue by Supermarket Branch
* Time-based sales performance

---

### 3. Product Performance Analysis

This section helps identify strong and weak product categories.

It includes:

* Revenue by category
* Quantity sold by category
* Profit by category
* Product category performance table
* High-performing categories
* Lower-performing categories

---

### 4. Customer Analysis

This section analyzes customer purchasing behavior.

It includes:

* Revenue by customer type
* Revenue by gender
* Number of transactions
* Average order value
* Customer purchasing patterns

---

### 5. Payment Method Analysis

The dashboard analyzes customer payment behavior using:

* Transaction share by payment method
* Revenue by payment method
* Payment behavior by customer type

---

### 6. Supermarket Branch Analysis

The dashboard compares the performance of different supermarket branches.

The presentation names used in the dashboard are:

* **Main Branch**
* **City Center Branch**
* **Express Branch**

Branch analysis includes:

* Revenue
* Profit
* Transactions
* Quantity sold

---

### 7. City Analysis

The dashboard provides city-wise performance analysis.

The presentation city names used in the dashboard are:

* **Hyderabad**
* **Vijayawada**
* **Visakhapatnam**

The analysis includes:

* Revenue by city
* Profit by city
* Transactions by city
* Quantity sold
* Average order value
* Average customer rating

---

## 💰 Profitability Analysis

The project evaluates business performance beyond sales revenue.

The dashboard analyzes:

* Revenue
* Gross Income / Profit
* Profit Margin
* Revenue versus Profit
* Profit by product category
* Profit margin by category

### Profit Margin Formula

```text
Profit Margin = Gross Income / Total Revenue × 100
```

### Average Order Value Formula

```text
Average Order Value = Total Revenue / Total Transactions
```

---

## ⏰ Time-Based Analysis

The project analyzes sales according to time-related information available in the dataset.

The dashboard can display:

* Monthly revenue
* Revenue by hour
* Transactions by hour
* Sales patterns over time

---

## ⭐ Customer Satisfaction Analysis

The dataset contains customer ratings, which are used to understand customer satisfaction.

The dashboard provides:

* Customer rating distribution
* Average customer rating
* Average rating by product category

---

## 🔎 Interactive Filters

Users can interactively filter the dashboard using:

* Date range
* City
* Supermarket branch
* Product category
* Customer type
* Gender
* Payment method

When filters are changed, the dashboard updates the KPIs and visualizations based on the selected records.

---

## 💡 Key Insights

The dashboard generates data-based insights such as:

* Highest revenue product category
* Lowest revenue product category
* Highest-performing city
* Highest-performing supermarket branch
* Highest-revenue customer type
* Most-used payment method
* Overall profit margin

All values are calculated from the actual dataset.

---

## ⚠️ Risk Analysis

The dashboard highlights areas that may require further business investigation, such as:

* Lower-performing product categories
* Locations with comparatively lower revenue
* Categories with weaker profitability
* High sales with comparatively low profit
* Areas showing weaker customer ratings

These are presented as areas for investigation based on the data and are not treated as unsupported conclusions.

---

## 🚀 Business Opportunities

The analysis can help identify opportunities such as:

* Strong-performing product categories
* Higher-revenue customer segments
* Better-performing locations
* High-profit categories
* Strong sales periods
* Frequently used payment methods

---

## 🎯 Business Recommendations

Based on the observed data, the dashboard provides recommendations related to:

* Product performance
* Category management
* Customer engagement
* Branch performance
* City performance
* Payment preferences
* Profitability improvement

The recommendations are connected to the data analysis rather than being manually invented.

---

## 🔄 Project Methodology

The project follows the following data analytics workflow:

```text
Raw Transaction Data
        ↓
Data Loading
        ↓
Data Cleaning
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
KPI Calculation
        ↓
Sales Analysis
        ↓
Product Analysis
        ↓
Customer Analysis
        ↓
Profitability Analysis
        ↓
Visualization
        ↓
Insights
        ↓
Risks & Opportunities
        ↓
Business Recommendations
```

---

## 📁 Project Structure

```text
Supermarket_Sales_Analytics/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── supermarket_sales.csv
│
├── assets/
│   └── screenshots/
│
└── .gitignore
```

---

## ⚙️ Installation

### Step 1: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 2: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

Make sure the dataset exists at:

```text
data/supermarket_sales.csv
```

Then run:

```bash
streamlit run app.py
```

The application will open in a local web browser.

---

## 📦 Requirements

The project uses the following direct Python packages:

```text
streamlit
pandas
numpy
plotly
```

---

## 📤 Data Export

The dashboard provides an option to download the currently filtered dataset as a CSV file.

This allows users to export the data currently being analyzed.

---

## 📌 Important Note About Location Labels

The original dataset contains its own branch and city labels. For the presentation of this project as an Indian supermarket business scenario, the application displays customized branch and city names.

### Branch Presentation Labels

| Original | Displayed          |
| -------- | ------------------ |
| A        | Main Branch        |
| B        | City Center Branch |
| C        | Express Branch     |

### City Presentation Labels

| Original  | Displayed     |
| --------- | ------------- |
| Yangon    | Hyderabad     |
| Mandalay  | Vijayawada    |
| Naypyitaw | Visakhapatnam |

These changes are **display-level relabeling only**. The underlying transaction amounts and analytical calculations are unchanged.

---

## 📈 Expected Business Benefits

The dashboard can help supermarket management to:

* Monitor overall business performance
* Understand revenue trends
* Identify high-performing products
* Identify categories requiring attention
* Understand customer purchasing behavior
* Compare branch and city performance
* Monitor profitability
* Understand payment preferences
* Identify business opportunities
* Support evidence-based decision-making

---

## ⚠️ Limitations

* The quality of insights depends on the quality and scope of the available dataset.
* The project is based on historical transaction records.
* The dashboard does not guarantee future business performance.
* Location names displayed in the dashboard are customized presentation labels.

---

## 🔮 Future Enhancements

Future versions of the project could include:

* Sales forecasting
* Customer segmentation
* Inventory analysis
* Demand prediction
* Anomaly detection
* Automated business alerts
* Advanced predictive analytics
* Real-time database integration
* Role-based dashboard access

---

## ✅ Conclusion

The **Supermarket Sales & Customer Analytics Dashboard** demonstrates how raw supermarket transaction data can be transformed into meaningful business intelligence.

Through data cleaning, preprocessing, exploratory data analysis, KPI calculation, sales analysis, customer analysis, product analysis, profitability analysis, visualization, and recommendation generation, the project provides a comprehensive view of supermarket business performance.

The dashboard focuses not only on presenting charts and statistics but also on converting analytical findings into understandable insights and potential business actions. This demonstrates the practical application of data analytics and business intelligence for supporting data-driven decision-making.

---

## 👩‍💻 Author

**Ch. Lakshmi Mani Mala**

B.Tech — Computer Science / AI & ML

**Project:** Supermarket Sales & Customer Analytics Dashboard

```
```
