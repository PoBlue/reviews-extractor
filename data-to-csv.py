#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data_extractor import headers_key, get_description_row_from_json
from utils import get_data_from_path, export_csv, list_file_name_with_extension
from data import DESC_JSON_PATH, DESC_CSV_PATH

def get_desc_row(_file_name):
    print(_file_name)
    desc_json_path = "example-data/description/{0}".format(_file_name)
    desc_json = get_data_from_path(desc_json_path)
    desc_row = get_description_row_from_json(desc_json)
    return desc_row


def export_desc(_json_path, _csv_path):
    desc_files = list_file_name_with_extension(_json_path, "json")

    rows = []
    for file_name in desc_files:
        row = get_desc_row(file_name)
        rows.append(row)

    export_csv(headers_key, rows, _csv_path)


export_desc(DESC_JSON_PATH, DESC_CSV_PATH)
# get_desc_row("786705.json")