from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Load the existing Azure Machine Learning workspace
ws = Workspace.from_config()

# Replace with your deployed web service name
service_name = "bank-marketing-predictor"  

# Load the deployed service
service = Webservice(name=service_name, workspace=ws)

# Enable Application Insights
service.update(enable_app_insights=True)

# Confirm the update
print(f"✅ Application Insights enabled for {service_name}.")