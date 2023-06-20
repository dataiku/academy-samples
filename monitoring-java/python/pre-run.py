import dataiku
import os
import zipfile

client = dataiku.api_client()
project = client.get_project(dataiku.default_project_key())
os.mkdir('python')

# Finding model in managed folder and downloading it
handle = project.get_managed_folder("3IHuPN7P")
python_model_file = open("python/model_package.zip", 'wb')
with handle.get_file('/python/model-initial-2023_01_27-16_20_13.zip') as f:
    data = f.content
    python_model_file.write(data)
python_model_file.close()

# Unzipping to local folder 
with zipfile.ZipFile('python/model_package.zip', 'r') as zip_ref:
    zip_ref.extractall("python/model")

# Downloading csv for scoring
scoring_file = open('python/pokemon_for_scoring.csv', 'wb')
with handle.get_file('pokemon_for_scoring.csv') as f:
    data = f.content
    scoring_file.write(data)
scoring_file.close()
