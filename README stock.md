
<a id="readme-top"></a>

<div align="center">
  <h3 align="center">🐄 Livestock Production Analysis — Kazakhstan 2024</h3>

  <p align="center">
    Analyze, visualize, and compare livestock production in Kazakhstan using official data from 2023 and 2024.
    <br />
    <a href="#usage"><strong>View Demo »</strong></a>
    <br />
    <br />
    <a href="#features">Features</a>
    ·
    <a href="#installation">Installation</a>
    ·
    <a href="#usage">Usage</a>
  </p>
</div>

---

## 📌 About The Project

This project provides a structured analysis of livestock production data in Kazakhstan using data extracted from official statistics. It helps:
- Clean and preprocess livestock production data
- Compare 2023 vs 2024 indicators
- Calculate year-over-year growth rates
- Visualize trends with charts

Perfect for analysts, students, or policymakers studying agricultural trends in Kazakhstan.

---

## 🛠️ Built With

- Python 3
- pandas
- matplotlib
- openpyxl

---

## 📁 Dataset

- **Source**: [Bureau of National Statistics — stat.gov.kz](https://stat.gov.kz/)
- **File**: `livestock_kazakhstan_2024.xlsx`
- **Sheet**: `1.`

---

## 🚀 Getting Started

### Prerequisites

Install the required Python libraries:

```bash
pip install pandas matplotlib openpyxl
```

### Installation

1. Clone the repository or download the script `analysiss.py`
2. Make sure the file `livestock_kazakhstan_2024.xlsx` is in the same directory
3. Run the analysis script:

```bash
python analysiss.py
```

---

## 💡 Usage

The script performs the following:
- Loads the Excel sheet with livestock data
- Cleans and preprocesses the data
- Calculates growth rates for each product category
- Saves two charts:
  - 📊 `bar_chart_readable.png` — side-by-side bar chart comparing 2023 and 2024
  - 📈 `histogram_2024_readable.png` — histogram of 2024 production volumes

---

## ✅ Features

- [x] Load and clean real-world Excel data
- [x] Compare multi-year livestock production
- [x] Calculate % growth per category
- [x] Export clean visualizations
- [x] Plain output in terminal for easy review

---

## 📊 Sample Output

```
Пропущенные значения:
Продукция    0
2024 год     0
2023 год     1

Первые строки:
                     Продукция  2024 год  2023 год     Рост (%)
0   Крупный рогатый скот          15000.0   12000.0   25.00
1   Овцы                          8000.0     6000.0   33.33
...

Графики сохранены как bar_chart_readable.png и histogram_2024_readable.png
```

---

## 🖼️ File Structure

```
livestock-analysis/
├── analysiss.py
├── livestock_kazakhstan_2024.xlsx
├── bar_chart_readable.png
├── histogram_2024_readable.png
└── README.md
```

---

## 🤝 Authors

Adil and Jansaya

---

<p align="right">(<a href="#readme-top">back to top</a>)</p>
