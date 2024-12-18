# CS 504 Team 3 Project 🧑‍💻👩‍💻

## Brief Descriptions of Folders
- 3.1 xgboost:
    - Notebook 3.1.2 shows the accuracy of the xg boost.
    - Notebook 5.1 shows memory error explained in section 5.1 of paper.
    - Other notebooks run the algorithm on different months, these were not used in the final paper. 
- 3.2 aporiori:
    - Notebook 3.2.2 shows memory error using Aporiori algorithm locally. 
    - Azure Databricks Notebook 3.2.3 utilizes the FP-Growth algorithm to do Market Basket Analysis.
- 3.3 k-means:
    - Notebook 3.3.2 uses K-means algorithm to group event type and price. 
    - Azure Databricks Untitled Notebook utilizes the K-means algorithm to group two feature variables. This was not used in the final paper.
- 4.0 visualizations:
    - Covers all the visualizations from section 4.0 of the paper except for visualization 4.5 as that was made using PowerBI.
- main:
    - Presents how the data was cleaned in cleaned.ipynd.
    - Showcases how to load kaggle.json from Jupyter directory and how the datasets are joined in Main.ipynb
    - Contains requirements.txt of packages needed as well, which can be installed using `pip install -r requirements.txt`.
    - The .gitignore file ignores .json file that is put in the main github folder.

## Analytics Stack 
- Azure
- Azure Databricks
- ChatGPT
- Jupyter Notebooks
- Kaggle
- Kaggle API
- Kaggle Notebooks
- PowerBI 
- Spark (interfaced through PySpark)

## Azure & Azure Databricks
Azure is used to gain access to data analytics software like Databricks. Databricks has Spark preconfigured on the instance. Students get a free 100$ credit to spin up compute resources. This was used as an alternative to the AWS credits provided in class.
- To access databricks click on the search bar in the Azure console and type `databricks`. Azure databricks should pop up. 
- Create a new resource, and use all default settings. 
- Go to notebooks and use the lowest compute offered. 
- When finished make sure to delete all resources similar to AWS. 

Links:
- Azure Student Credits: https://azure.microsoft.com/en-us/free/students
- Azure Databricks Documentation: https://learn.microsoft.com/en-us/azure/databricks/

## Kaggle 
Kaggle was used to source and house the data for the project. The dataset used for the project was the cleaned dataset of a dataset found on Kaggle. This new dataset was stored on Kaggle as up to 100 GB can be stored on Kaggle for free. Kaggle can also provide notebooks with pyspark in case teammates don't have the necessary compute power to run the datasets locally. 

Links:
- Cleaned dataset: https://www.kaggle.com/datasets/matt2434/cleaned-ecommerce-data
- Original dataset: https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store
- Notebook joining with pyspark (preferred): https://www.kaggle.com/code/matt2434/import-using-pyspark
- Notebook joining with pandas: https://www.kaggle.com/code/matt2434/cs-504-project

## Kaggle API
The Kaggle API is used to interface between Kaggle and your coding environment. You need to first create a json token file and put it in the .kaggle/ local directory, or load the .json using the provided code in main. When you call the Kaggle API for a download for example, the files are stored locally in a specific path. If you are using the cloud, the files are also stored in a specific path in that environment. 

Refer to the documention below for more detailed information:
- https://www.kaggle.com/docs/api
- https://github.com/Kaggle/kagglehub

## Setting up the Environment
- Click on your Kaggle profile picture in the upper right hand corner -> Click on Settings -> Scroll down and Select Create New Token under the API section.
    - A .json file should have downloaded
- Take created .json file and put in directory `C:\Users\<Windows-username>\.kaggle\kaggle.json` on Windows and `~/.kaggle/kaggle.json` on Linux, OSX, and other UNIX-based operating systems
    - Doing this step will automatically authenticate token going forward
- Install Kaggle in python environment using the command `pip install kaggle` & `pip install kagglehub` (if using kagglehub statement)
- To load directly put the .json in your active Jupyter directory and run the first code block in main.ipynb

Here is a YouTube video that goes over how to import kaggle datasets in Collab:
- https://www.youtube.com/watch?v=gkEbaMgvLs8
