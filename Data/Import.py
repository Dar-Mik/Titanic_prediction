import kagglehub
import shutil
import os

def get_data(target_folder = "./"):
    # Download the dataset
    path = kagglehub.dataset_download("yasserh/titanic-dataset")

    print("Path to dataset files:", path)


    # Make sure the target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Copy files from download path to target folder
    for file_name in os.listdir(path):
        full_file_name = os.path.join(path, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, target_folder)

    print("Files copied to:", target_folder)