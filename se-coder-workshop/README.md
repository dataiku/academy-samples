SE CODER WORKSHOP WITH MLFLOW EXPRIMENT TRACKING
LAST TESTED ON DATAIKU CLOUD 12.5.1

--------- Instructions setup --------------

Spin up a Trainer instance
Add yourself and Workshop attendees

The starter project can be found in this git repo 
The starter and completed project needs to be uploaded to the instance.

A code env needs to be created on the instance with the following requirements:
Name: mlflow
Python version: 3.8
Packages to install:
mlflow
scikit-learn
statsmodels
protobuf
pytest==7.2.2



There have been some issues with the Custom Modeling notebook SSH requests. The current process requires some additional backend work to support.
Install the Admin Access extension on the Launchpad and make yourself an Admin

Generate a global API key, make sure impersonation is set to ‘dkuadmin’ and copy secret. If you are using cloud evaluation instances the cloud team can generate a key for you. 

In the starter project replace the API_KEY with your API secret generated or recived from the cloud team. 
In the starter project replace the SPACE_URL  with the your space url

This is needed in the custom modelling notebook(the line that assigns the Dataiku remote). Future versions of MLFlow may not require this 


