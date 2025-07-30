# Private Equity Screener

This project enables filtering of listed companies based on key financial metrics to identify potential private equity investment opportunities. It is designed as a lightweight, functional dashboard to assist in preliminary financial screening.

## Project Objective

To create a tool that helps private equity analysts or retail investors quickly identify undervalued and fundamentally strong companies using structured financial data.

## Key Features

- Load and process financial data from CSV format
- Apply custom filters on:
  - Revenue (in Cr)
  - PE Ratio
  - Return on Equity (ROE)
  - Profit Margin
  - Debt-to-Equity Ratio
- Sort companies based on selected financial metrics
- Present results in a clear, tabular format

## Dataset

The project uses a sample dataset (`companies.csv`) containing financial details of listed companies.

**Example columns:**
- Company
- Revenue_Cr
- PE_Ratio
- ROE
- Profit_Margin
- Debt_to_Equity

You can replace this with actual data sourced from platforms like Screener.in or Moneycontrol.

## Project Structure

```
private_equity_screener/
│
├── analysis.ipynb           # Jupyter Notebook for full project logic and results
├── screener.py             # Optional Python module for data loading/filtering
├── companies.csv           # Input dataset (can be updated)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

## Tools and Libraries Used

- Python 3.x
- pandas – for data manipulation
- matplotlib – for visualizations (if needed)
- Jupyter Notebook – for analysis interface
- (Optional) Power BI – for interactive dashboards

## How to Run

### Local Setup (Jupyter Notebook)
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/private_equity_screener.git
   cd private_equity_screener
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the notebook:
   ```bash
   jupyter notebook analysis.ipynb
   ```

4. Run all cells to filter data and view results.

## Example Use Case

An investor wants to identify companies with:
- PE Ratio under 20
- ROE above 15%
- Profit Margin above 10%
- Low debt

Using this screener, they can narrow down large datasets to a small, high-potential shortlist for further analysis.

## What I Learned

- Translating investment criteria into programmatic filters
- Working with real-world financial data
- Data cleaning, filtering, and visualization in pandas
- Presenting insights in a reproducible and readable format

## License

This project is open-sourced under the MIT License.