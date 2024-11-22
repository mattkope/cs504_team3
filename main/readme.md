## Kaggle Data
If you are unable to run the dataset locally, using kaggle notebooks would be your best option. We can then commit your changes to main. The dataset will be stored in Kaggle.
Link to https://www.kaggle.com/datasets/matt2434/cleaned-ecommerce-data

## Kaggle API for local & cloud use
You need to read the documentation on how to authenticate with the kaggle API. You need to first create a json token file. This short video shows where to get it along with where to put it in your computer system so you don't have errors: https://www.youtube.com/watch?v=hzcV0hDkfzs&t=230s

There are multiple different ways to authenticate. The API example shows putting the .json in the active directory, so it pulls from that in the first block of code. Since then I have put it in the .kaggle/ directory so it automaticially checked on my system. 

## How to use Kaggle API
- Install Kaggle in environment using the command `pip install kaggle`
- Click on your Kaggle profile picture in the upper right hand corner -> Click on Settings -> Scroll down and Select Create New Token under the API section.
- Take created .json file and put in directory `C:\Users\<Windows-username>\.kaggle\kaggle.json` on Windows and `~/.kaggle/kaggle.json` on Linux, OSX, and other UNIX-based operating systems
  - Doing this step will automaticially authenticate token going forward
- To load directly put the .json in your active jupyter directory and run the API.ipynb code block

If you have any other problems refer to documentation:
- https://www.kaggle.com/docs/api
- https://github.com/Kaggle/kagglehub

## Brief Descriptions of Uploaded Datasets:
- Main - the main notebook that we should use going forward
- cleaned - how the data was cleaned for Main and cleaned kaggle eccomerce dataset

## Scope of Project
From November 1st - December 2nd (Cyber Monday)

## Other
Add required packages to requirements.txt. Use anaconda environment for environment management.
pip install -r requirements.txt
