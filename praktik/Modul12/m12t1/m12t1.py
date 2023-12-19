import pandas as pd

data = pd.read_csv('D:/THIS PC/Documents/Python/Praktik/m12t1')

# Print the data frame
print("Data Frame:")
print(data)

# Calculate mean (rata-rata) and standard deviation
mean_values = data.mean()
std_values = data.std()

# Print the results
print("\nMean (Rata-rata):")
print(mean_values)

print("\nStandar Deviasi:")
print(std_values)
