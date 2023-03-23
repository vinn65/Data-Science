import csv

data = [
(1, 'Lotion', 'Cosmetics'),
(2, 'Lotion', 'Cosmetics'),
(3, 'Lotion', 'Cosmetics'),
(4, 'Lotion', 'Cosmetics'),
(5, 'Lotion', 'Cosmetics'),
(6, 'Samsung', 'Electronics'),
(7, 'Samsung', 'Electronics'),
(8, 'Samsung', 'Electronics'),
(9, 'Samsung', 'Electronics'),
(10, 'Samsung', 'Electronics'),
(11, 'Shampoo', 'Cosmetics'),
(12, 'Shampoo', 'Cosmetics'),
(13, 'Shampoo', 'Cosmetics'),
(14, 'Shampoo', 'Cosmetics'),
(15, 'Shampoo', 'Cosmetics'),
(16, 'iPhone', 'Electronics'),
(17, 'iPhone', 'Electronics'),
(18, 'iPhone', 'Electronics'),
(19, 'iPhone', 'Electronics'),
(20, 'iPhone', 'Electronics')
]

# create a CSV file and write the data to it
with open('data1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product_id', 'product_name','product_type'])
    for row in data:
        writer.writerow(row)
