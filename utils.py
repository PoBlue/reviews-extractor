import json
import csv
import glob, os

# save json data to file
def save_data_to_path(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def get_data_from_path(path):
    with open(path) as json_file:  
        data = json.load(json_file)
        return data


def export_csv(_headers, _rows, _path):
    """
    _rows: [ 
        (a,b,c), 
        (f,g,h), 
    ]
    _header: [a, b, c]
    """
    with open(_path, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(_headers)
        f_csv.writerows(_rows)


def list_file_name_with_extension(path, extension):
    """list all file name with extension"""
    oldpwd = os.getcwd()
    os.chdir(path)
    files = glob.glob("*.%s"%(extension)) 
    os.chdir(oldpwd)
    return files

