
import kagglehub
import os

path = kagglehub.dataset_download(
    "prathamtripathi/drug-classification"
)

print("Dataset downloaded to:", path)

print("Files:")
for file in os.listdir(path):
    print(file)