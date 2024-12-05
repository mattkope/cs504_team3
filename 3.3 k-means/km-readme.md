# K Means Template Used

## Preprocess the Data
1. Choose Features as Price and Brand
2. Indexed Brand to get it to Numerical Values
3. Removed Outliers in Price 

```python
from pyspark.ml.feature import VectorAssembler

# Assuming you want to cluster based on 'feature1' and 'feature2'
assembler = VectorAssembler(
    inputCols=['feature1', 'feature2'],
    outputCol='features'
)

feature_df = assembler.transform(df)
```
## Import and Train the Model
```python
from pyspark.ml.clustering import KMeans

# Set the number of clusters (k)
kmeans = KMeans().setK(3).setSeed(1)
model = kmeans.fit(feature_df)
```
## Evaluate the Model
```python
# Make predictions
predictions = model.transform(feature_df)
predictions.show()

# Evaluate clustering by computing Within Set Sum of Squared Errors (WSSSE)
wssse = model.summary.trainingCost
print("Within Set Sum of Squared Errors = " + str(wssse))
```
## Analyze the Results
```python
# Display cluster centers
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
```
## Visualize the Clusters
```python
import matplotlib.pyplot as plt

pandas_df = predictions.select("feature1", "feature2", "prediction").toPandas()

plt.scatter(pandas_df['feature1'], pandas_df['feature2'], c=pandas_df['prediction'], cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

Full Coding Log: Chatgpt coding logs: https://chatgpt.com/share/6746bfba-d0b4-800b-bc2b-174ce9b3e79a


