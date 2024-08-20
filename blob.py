from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Set up connection details
connect_str = "your_connection_string"
container_name = "test"
local_file_name = "your_local_file.txt"
blob_name = "your_blob_name.txt"

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Create the container if it does not exist
try:
    container_client.create_container()
except Exception as e:
    print(f"Container {container_name} already exists.")

# Upload the file
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

with open(local_file_name, "rb") as data:
    blob_client.upload_blob(data)

print(f"File {local_file_name} uploaded to container {container_name} as blob {blob_name}.")
