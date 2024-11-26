# CS 504 Team 3 Project 🧑‍💻👩‍💻

## Kaggle 
Kaggle is mainly used to house the dataset. Kaggle can also provide notebooks with pyspark in case teammates don't have the necessary compute power to run the datasets locally. Copy and Paste the code from linked notebooks to newly created notebooks.

Links:
- Cleaned dataset: https://www.kaggle.com/datasets/matt2434/cleaned-ecommerce-data
- Notebook joining with pyspark (preferred): https://www.kaggle.com/code/matt2434/import-using-pyspark
- Notebook joining with pandas: https://www.kaggle.com/code/matt2434/cs-504-project

## Kaggle API
The Kaggle API is used to interface between Kaggle and your coding environment. You need to first create a json token file and put it in the .kaggle/ local directory, or load the .json using the provided code in main. When you call the Kaggle API for a download for example, the files are stored locally in a specfic path. If you are using the cloud, the files are also stored in a specific path in that environment. 

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

## Brief Descriptions of Folders

- Aporiori:
    - Azure Databricks Notebook that utilizes the FPGrowth algorithm to do Market Basket Analysis.
    - Loads in data using Kaggle API and not kagglehub.
- main:
    - Presents how the data was cleaned in cleaned.ipynd.
    - Showcases how to load kaggle.json from Jupyter directory and how the datasets are joined in Main.ipynb
    - Contains requirements.txt of packages needed as well, which can be installed using `pip install -r requirements.txt`.
    - The .gitignore file ignores .json file that is put in the main github folder.