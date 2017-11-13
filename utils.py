import json

# save json data to file
def save_data_to_path(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def get_data_from_path(path):
    with open(path) as json_file:  
        data = json.load(json_file)
        return data