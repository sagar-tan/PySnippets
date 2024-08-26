'''Given a DataFrame containing sales data with columns: 'Product', 'Region', 'Sales', and 'Date', 
write a Python function that: 
• Groups the data by 'Product' and calculates the total sales for each product. 
• Groups the data by 'Region' and 'Product', then calculates the mean sales for each 
combination.'''
import pandas as pd
def analyse_dat(df):
    product_dta = df.groupby('Product')['Sales'].sum()
    print(product_dta)

    Region_sale = df.groupby(['Product', 'Region'])['Sales'].mean()
    print(Region_sale)



data = {
    'Product': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Sales': [100, 150, 200, 250, 300, 350],
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'])
}
df = pd.DataFrame(data)
analyse_dat(df)
