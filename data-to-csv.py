#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data_extractor import DESC_HEADERS_KEY, get_description_row_from_json, CONTENT_HEADERS_KEY, get_content_row_from_json, COMMENT_HEADERS_KEY, get_comment_row_from_json
from utils import get_data_from_path, export_csv, list_file_name_with_extension
from data import DESC_JSON_PATH, DESC_CSV_PATH, CONTENT_CSV_PATH, CONTENT_JSON_PATH, COMMENT_CSV_PATH, COMMENT_JSON_PATH, REVIEW_ROOT_JSON_PATH


def get_desc_row(_file_name):
    """
    get description row to create csv
    """
    print("description csv --> %s" % _file_name)
    desc_json_path = DESC_JSON_PATH + _file_name
    desc_json = get_data_from_path(desc_json_path)
    desc_row = get_description_row_from_json(desc_json)
    return desc_row


def get_content_row(_file_name):
    """
    get content row to create csv
    """
    print("content csv --> %s" % _file_name)
    content_json_path = CONTENT_JSON_PATH + _file_name
    content_json = get_data_from_path(content_json_path)
    content_rows = []
    for content in content_json:
        content_row = get_content_row_from_json(content)
        content_rows.append(content_row)
    return content_rows


def get_comment_row(_file_name):
    """
    get comment row to create csv
    """
    print("comment csv --> %s" % _file_name)
    comment_json_path = COMMENT_JSON_PATH + _file_name
    comment_json = get_data_from_path(comment_json_path)
    comment_rows = []
    for comment in comment_json:
        comment_row = get_comment_row_from_json(comment)
        comment_rows.append(comment_row)
    return comment_rows


def export_desc(_json_path, _csv_path):
    desc_files = list_file_name_with_extension(_json_path, "json")

    rows = []
    for file_name in desc_files:
        row = get_desc_row(file_name)
        rows.append(row)

    export_csv(DESC_HEADERS_KEY, rows, _csv_path)


def export_content(_json_path, _csv_path):
    content_files = list_file_name_with_extension(_json_path, "json")

    csv_rows = []
    for file_name in content_files:
        rows = get_content_row(file_name)
        csv_rows.extend(rows)
    
    export_csv(CONTENT_HEADERS_KEY, csv_rows, _csv_path)


def export_comment(_json_path, _csv_path):
    comment_files = list_file_name_with_extension(_json_path, "json")

    csv_rows = []
    for file_name in comment_files:
        rows = get_comment_row(file_name)
        csv_rows.extend(rows)
    
    export_csv(COMMENT_HEADERS_KEY, csv_rows, _csv_path)


def main():
    export_desc(DESC_JSON_PATH, DESC_CSV_PATH)
    export_content(CONTENT_JSON_PATH, CONTENT_CSV_PATH)
    export_comment(COMMENT_JSON_PATH, COMMENT_CSV_PATH)


main()