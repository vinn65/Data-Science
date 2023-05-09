import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# Load iris dataset from CSV file
df = pd.read_csv('iris.csv')

# Convert dataframe to list of transactions
transactions = []
for index, row in df.iterrows():
    transactions.append(row.tolist())

# Convert transactions to one-hot encoded format
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_array, columns=te.columns_)

# Find frequent itemsets using Apriori algorithm
frequent_itemsets = apriori(df_encoded, min_support=0.1, use_colnames=True)

# Print frequent itemsets
print(frequent_itemsets)
