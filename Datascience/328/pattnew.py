import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load iris dataset from CSV file
df = pd.read_csv('iris.csv')

# Convert dataframe into a list of transactions
transactions = []
for i, row in df.iterrows():
    transaction = []
    transaction.append(row['species'])
    if row['sepal_length'] < 5.0:
        transaction.append('sepal_length_short')
    elif row['sepal_length'] >= 5.0 and row['sepal_length'] < 6.0:
        transaction.append('sepal_length_medium')
    else:
        transaction.append('sepal_length_long')
    if row['sepal_width'] < 3.0:
        transaction.append('sepal_width_narrow')
    elif row['sepal_width'] >= 3.0 and row['sepal_width'] < 3.5:
        transaction.append('sepal_width_medium')
    else:
        transaction.append('sepal_width_wide')
    if row['petal_length'] < 2.0:
        transaction.append('petal_length_short')
    elif row['petal_length'] >= 2.0 and row['petal_length'] < 5.0:
        transaction.append('petal_length_medium')
    else:
        transaction.append('petal_length_long')
    if row['petal_width'] < 0.5:
        transaction.append('petal_width_narrow')
    else:
        transaction.append('petal_width_wide')
    transactions.append(transaction)

# Perform one-hot encoding on transactions
te = TransactionEncoder()
te_transactions = te.fit(transactions).transform(transactions)
df_transactions = pd.DataFrame(te_transactions, columns=te.columns_)

# Find frequent itemsets using Apriori algorithm
frequent_itemsets = apriori(df_transactions, min_support=0.2, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# Print association rules
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
