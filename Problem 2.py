# Customers Placing the Largest Number of Orders

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number')['order_number'].count().reset_index()
    df = df.sort_values('customer_number', ascending=False)['customer_number'].head(1).reset_index()
    print(pd.DataFrame(df['customer_number']))
    return pd.DataFrame(df['customer_number'])

data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

largest_orders(orders)