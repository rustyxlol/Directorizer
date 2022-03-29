import os
import shutil


def get_files(src):
    """
    Returns all the files in src
    """
    return [i for i in os.listdir(src) if os.path.isfile(os.path.join(src, i))]


def get_matches(file_name, categories):
    """Check if file_name contains any category

    Args:
        file_name (str): file name
        categories (list): list of categories

    Returns:
        list: list of valid categories that the file can be categorized into
    """
    return [match for match in categories if match in file_name.lower()]


def create_directories(src, categories):
    for category in categories:
        dir_name = os.path.join(src, category)
        try:
            os.makedirs(dir_name)
        except OSError:
            print("File already exists!")


def move_file(src, dst):
    if os.path.isfile(src):
        shutil.move(src, dst)


if __name__ == "__main__":
    input_source = input("Enter source path: ")
    input_categories = input(
        "Enter categories separated by comma(a,b,c): ").split(",")
    all_categories = [i.lower().strip() for i in input_categories if i]

    create_directories(input_source, all_categories)

    fileNames = get_files(input_source)

    for fileName in fileNames:
        matches = get_matches(fileName, all_categories)
        if matches:
            srcFile = os.path.join(input_source, fileName)
            dstFile = os.path.join(input_source, matches[0], fileName)
            move_file(srcFile, dstFile)
    print("Finished the job boss")
