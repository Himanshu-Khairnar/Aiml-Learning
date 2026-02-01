# E-commerce Exploratory Data Analysis (EDA)

This project performs an exploratory data analysis on e-commerce sales data from October 2019 to derive insights into customer purchasing behavior and sales trends.

## Features

- **Data Cleaning**: Handling missing values and converting data types for analysis.
- **Revenue Analysis**:
  - Weekly revenue trends.
  - Sales performance by City (Revenue & Quantity).
  - Hourly sales patterns to identify peak shopping times.
- **Market Basket Analysis**: Identifying products that are frequently bought together.

## Observations

- **Peak Sales**: Analysis of hourly data typically reveals peaks in order volume around midday (11 AM - 12 PM) and early evening (7 PM), suggesting optimal times for advertising.
- **Location Impact**: Certain cities demonstrate significantly higher order volumes and revenue, indicating key markets.
- **Product Combinations**: Market basket analysis identifies pairs of items frequently purchased together (e.g., phones and charging cables), which can inform bundling strategies.

## Technologies Used

- **Python**
- **Pandas**: For data processing and aggregation.
- **Matplotlib**: For plotting graphs and charts.
- **NumPy**: For numerical operations.

## Files

- `EcommerceEDA.ipynb`: Main analysis notebook.
- `Sales_October_2019.csv`: Raw sales data.
