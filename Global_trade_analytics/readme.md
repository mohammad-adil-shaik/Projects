# 🌍 TradeSphere — Global Trade Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-brightgreen)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-cyan)
![Altair](https://img.shields.io/badge/Altair-5.0%2B-red)
![Streamlit-Echarts](https://img.shields.io/badge/Streamlit--Echarts-0.4%2B-purple)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive Streamlit dashboard to explore and analyze global import-export flows, commodity trends, and trade strengths across countries and years.

---

## 🚀 Features

- 🌍 **Country-wise Trade Analysis** — Select any country and analyze trade.
- 📅 **Year Range Filtering** — Focus on a specific time period dynamically.
- 📦 **Trade Type Filtering** — Choose Import, Export, Re-Import, Re-Export flows.
- 📈 **Trade Flow Trends** — Dynamic line charts for different trade types.
- 🥧 **Trade Value by Category** — Visual insights with Pie Charts and Treemaps.
- 🔥 **Advanced Insights** — Heatmap, Pareto Chart (Top 20 Commodities), and Bubble Chart (Trade Value vs Weight).
- 🚚 **Import vs Export Strength** — Analyze top commodities based on trade flow balance.
- 🎨 **Custom Branding** — Includes logo and background image integration.

---

## 🛠 Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Altair**
- **Streamlit-Echarts**

---

## 📸 Screenshots

| Dashboard Home       | Trade Flow Trends          | Crossflow                 |
| :------------------- | :------------------------- | :------------------------ |
| ![](assets/home.png) | ![](assets/trade_flow.png) | ![](assets/crossflow.png) |

---

## ⚙️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/mohammad-adil-shaik/Projects/Global_trade_analytics.git


# Navigate into the project
cd Projects/Global_trade_analytics

# (Optional) Create and activate virtual environment

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📂 Project Structure

```
/assets/           # Logo and background images
app.py            # Main Streamlit app
Raw_data.csv       # Trade data file
README.md          # Project overview
```

---

## 📢 Project Status

- ✅ Basic Analytics Dashboard Completed
- 🚀 Future Enhancements Planned:
  - Predictive trade analytics
  - Country vs Country comparison
  - Animated year-wise trade evolution

---
