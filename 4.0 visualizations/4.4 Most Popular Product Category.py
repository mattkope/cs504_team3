import kagglehub
import os
import pandas as pd

#downloading the dataset
dataset_name = "matt2434/cleaned-ecommerce-data"
download_path = kagglehub.dataset_download(dataset_name)

#listing the files
downloaded_files = os.listdir(download_path)

#finding the first csv file in directory
csv_filename = [f for f in downloaded_files if f.endswith('.csv')][0]

#read the CSV file into a pandas DataFrame
df = pd.read_csv(os.path.join(download_path, csv_filename))

#printing the headers
print(df.columns.tolist())

#printing the top 5 most frequent category_codes
top_5_category_codes = df['category_code'].value_counts().head(5)
print(top_5_category_codes)

plt.figure(figsize=(8, 8))  # Set the size of the plot
wedges, texts, autotexts = plt.pie(
    top_5_category_codes, 
    labels=top_5_category_codes.index, 
    autopct='%1.1f%%',  # Display percentage on the wedges
    startangle=90,      # Start the pie chart at a specific angle
    wedgeprops={'edgecolor': 'black'}  # Optional: Adds black edge around the wedges
)

#creating the donut chart
plt.gca().add_artist(plt.Circle((0, 0), 0.5, color='white', linewidth=0))  # Adds the "hole" in the middle

#adding title
plt.title('Top 5 Most Frequent Products', fontsize=16)

#showing plot
plt.show()
