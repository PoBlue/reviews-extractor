from data_extractor import headers_key, get_description_row_from_json
from utils import get_data_from_path, export_csv

def get_desc_row(_review_id):
    desc_json_path = "example-data/description/{r_id}.json".format(r_id=_review_id)
    desc_json = get_data_from_path(desc_json_path)
    desc_row = get_description_row_from_json(desc_json)
    return desc_row

rows = []
row = get_desc_row("508858")
rows.append(row)

review_csv_path = "review-csv/"
desc_path = review_csv_path + "description.csv"

export_csv(headers_key, rows, desc_path)
