# 📊 Business Sales Performance Dashboard

**A consultant-style data analytics project analyzing sales performance across Indian cities**

---

## 🎯 Project Overview

This project demonstrates real-world business intelligence skills by analyzing sales data from a fictional company operating in multiple Indian cities. The dashboard provides actionable insights to help management make data-driven decisions.

### Business Problem
> "Management wants to know why profits are falling in some regions and which products drive growth."

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone or create project folder**
```bash
mkdir sales-dashboard
cd sales-dashboard
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
sales-dashboard/
│
├── data/                          # Generated data and database
│   ├── sales_data.csv
│   ├── sales_database.db
│   └── business_insights.png
│
├── src/                           # Source code
│   ├── 1_data_generation.py      # Generate dummy data
│   ├── 2_sql_analysis.py         # SQL queries and analysis
│   ├── 3_business_analysis.py    # Python analysis + visualizations
│   └── 4_streamlit_dashboard.py  # Interactive dashboard
│
├── sql/
│   └── sales_queries.sql         # Reusable SQL queries
│
├── requirements.txt
└── README.md
```

---

## 🔧 How to Run

### Step 1: Generate Data
```bash
python src/1_data_generation.py
```
**Output:** Creates `data/sales_data.csv` with 5,000 sales records

### Step 2: SQL Analysis
```bash
python src/2_sql_analysis.py
```
**Output:** Creates SQLite database and prints business insights

### Step 3: Business Analysis
```bash
python src/3_business_analysis.py
```
**Output:** Generates visualizations and saves to `data/business_insights.png`

### Step 4: Launch Interactive Dashboard
```bash
streamlit run src/4_streamlit_dashboard.py
```
**Output:** Opens interactive dashboard in browser (http://localhost:8501)

---

## 📊 Key Features

### 1. **Data Generation**
- 5,000+ realistic sales records
- 12 Indian cities across 5 regions
- 5 product categories
- Time range: Jan 2023 - Dec 2024
- Includes loss-making scenarios for realism

### 2. **SQL Analysis**
- Revenue & profit by region
- City-wise performance rankings
- Category analysis
- Loss-making product-city combinations
- Monthly/quarterly trends
- Sales rep performance

### 3. **Business Insights**
- KPI dashboard (Revenue, Profit, Orders, Margin)
- Regional performance comparison
- Top/bottom performers
- YoY growth analysis
- **Consultant-style recommendations**

### 4. **Interactive Dashboard**
- Filter by year, region, category
- Real-time KPI updates
- Interactive charts (Plotly)
- Detailed tables
- Business recommendations

---

## 💡 Business Insights Discovered

### ✅ High-Performance Areas
- **Best Region:** West (Mumbai, Pune)
- **Top Category:** Electronics (highest margin)
- **Star Product:** Laptops drive 35% of profit

### ⚠️ Areas Needing Attention
- **Underperforming:** Kolkata (low margins)
- **Loss-making:** Tablet sales in Kolkata
- **Recommendation:** Stop selling specific products in unprofitable cities

### 📈 Growth Opportunities
- Corporate segment has 45% higher margins than Consumer
- Increase marketing spend in high-performing cities
- Replicate Mumbai strategy in Tier-2 cities

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Data processing & analysis |
| **Pandas** | Data manipulation |
| **SQLite** | Database management |
| **SQL** | Business queries |
| **Matplotlib/Seaborn** | Static visualizations |
| **Plotly** | Interactive charts |
| **Streamlit** | Web dashboard |

---

## 📸 Screenshots

### Dashboard Preview
![Dashboard](data/business_insights.png)

---

## 🎤 Interview Talking Points

### "Tell me about your project"
> "I built a consultant-style sales performance dashboard that helps business leaders make data-driven decisions. The project analyzes 5,000+ sales records across 12 Indian cities to identify why profits are falling in certain regions and which products drive growth."

### "What insights did you find?"
> "I discovered that while our West region (Mumbai, Pune) performs exceptionally well, we're losing money selling tablets in Kolkata. My recommendation was to discontinue that product-city combination, which could save ₹2.5 lakhs annually. I also found that Corporate customers have 45% higher margins, so we should focus sales efforts there."

### "What SQL queries did you use?"
> "I wrote complex queries like regional aggregations with profit margins, loss-making product-city combinations using HAVING clauses, and YoY growth comparisons. For example, I used GROUP BY with CASE statements to segment customers by discount levels and analyze profitability impact."

### "How would you present this to management?"
> "I created an interactive Streamlit dashboard where executives can filter by year, region, and category to drill down into specific areas. The dashboard shows KPIs at the top, trends in the middle, and actionable recommendations at the bottom. I also exported a static report for presentations."

---

## 📈 Future Enhancements

- [ ] Add predictive analytics (sales forecasting)
- [ ] Customer segmentation with ML
- [ ] Real-time data pipeline
- [ ] Email alert system for low-margin sales
- [ ] Integration with Power BI/Tableau
- [ ] API for external applications

---

## 🤝 Contributing

This is a portfolio project, but suggestions are welcome!

---



## 📄 License

This project is for educational and portfolio purposes.

---

**⭐ If you found this helpful, please star the repository!**


