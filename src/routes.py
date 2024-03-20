import json
import os
from fastapi import APIRouter

router = APIRouter()


# Get the absolute path to the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(script_dir, 'apiConfig.json')


# Load JSON configuration
with open(config_file_path) as f:
    api_config = json.load(f)

# Initialize a dictionary to store service instances
service_instances = {}

# Iterate over each configuration
for config in api_config:
    # Get the service name from the configuration
    service_name = config["serviceName"]

    # Check if the service instance is already created
    if service_name not in service_instances:
        # Import the module dynamically based on the component and service name
        module_path = f'src.services.{config["fileName"]}'
        service_module = __import__(module_path, fromlist=[''])

        # Get the service instance from the module dynamically
        service_instance = getattr(service_module, service_name, None)
        if service_instance is None:
            print(f"Service instance {service_name} not found in module {module_path}")
            continue

        # Add the service instance to the dictionary
        service_instances[service_name] = service_instance

    # Get the service function from the service instance
    service_function = getattr(service_instances[service_name], config["functionName"], None)
    if service_function is None:
        print(f"Function {config['functionName']} not found in service {service_name}")
        continue

    # Add route dynamically based on method type
    method_type = config["methodType"].upper()
    methods = [method_type]

    if method_type not in ["GET", "POST", "PUT", "PATCH"]:
        print(f"Unsupported method type: {config['methodType']}")
    else:
        # Include a forward slash before the API endpoint
        router.add_api_route("/" + config["apiName"], service_function, methods=methods)
