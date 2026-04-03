# Uncleaner module
from pathlib import Path
from shutil import move


# Takes all the files of the given directory and moves them to their parent directory
# Accepts the current directory if the folder is not given
def unclean(folder: Path =  None):
    if folder is None:
        folder = Path(__file__).parent
    if not folder.is_dir():
        raise ValueError("{folder} is not a folder. Please input a folder.")
    parent_folder_path = folder.parent
    for file in folder.glob("*"):
        if not file.name.startswith("."):
            destination = parent_folder_path / file.name
            if not destination.exists():
                move(str(file), str(parent_folder_path / file.name))


# Grabs all the files of the folders within the current directory
# And brings them out to the current directory
def unclean_all():
    current_folder = Path(__file__).parent
    
    for folder in current_folder.glob("*"):
        if folder.is_dir():
            unclean(folder.resolve())

