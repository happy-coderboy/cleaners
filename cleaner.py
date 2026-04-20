# Cleaner module
from pathlib import Path
from shutil import move


# Takes all the files in the current directory and puts files of the given extension into the given folder name
def cleanup(extension: str, folder_name: str):
    """
    Takes all the files in the current directory and puts files of the given extension into the given folder name

    Args:
        extension (str): The extension of the files to clean (like these -> py, html, txt, etc)
        folder_name (Path): The folder to put the files into

    Raises:
        ValueError: If folder name contains spaces or the extensions contain periods
    """

    if (len(folder_name.split(" ")) > 1):
        raise ValueError("Folder name cannot contain spaces")
    if extension[0] == ".":
        raise ValueError("Only the extension has to be typed, no period is required")
    
    main_directory = Path(__file__).parent
    new_directory = Path(main_directory / folder_name)

    if not new_directory.exists():
        new_directory.mkdir()
        
    for file in main_directory.glob("*." + extension):
        move(str(file), str(new_directory / file.name))


# Same as cleanup but cleans multiple extensions. 
# Accepts a dictionary with extensions as keys and folder names as values.
def clean_all(folder_names_dictionary=None):
    """
    Similar to clean all, but cleans many extensions simultaneously by iteratively running the cleanup function

    Args:
        folder_names_dictionary (dict): A dictionary where keys are extensions and values are folder names.
                                        If no dictionary is given, then all files are sorted into one "File" folder
    """
    if folder_names_dictionary is None:
        folder_names_dictionary = {"*": "Files"}

    for extension, folder_name in folder_names_dictionary.items():
        cleanup(extension, folder_name)  


# Same as clean_all but can accept an additional list
# Containing names of files not to put in folders
def clean_all_except(folder_names_dictionary = None, except_files = None):
    if folder_names_dictionary is None:
        folder_names_dictionary = {"*": "Files"}
    if except_files is None:
        except_files = []

    resolved_exceptions = set()
    for file in except_files:
        file_var = Path(file)
        if not file_var.exists():
            raise FileNotFoundError(f"{file_var} does not exist or has been typed incorrectly")
        resolved_exceptions.add(file_var.resolve())

    for extension, folder_name in folder_names_dictionary.items():
        if (len(folder_name.split(" ")) > 1):
            raise ValueError("Folder name cannot contain spaces")
        if extension[0] == ".":
            raise ValueError("Only the extension has to be typed, no period is required")
        
        main_directory = Path(__file__).parent
        new_directory = Path(main_directory / folder_name)

        if not new_directory.exists():
            new_directory.mkdir()

        for file in main_directory.glob("*." + extension):
            if file.resolve() not in resolved_exceptions:
                move(str(file), str(new_directory / file.name))


