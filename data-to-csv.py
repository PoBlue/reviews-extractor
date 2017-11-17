#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from data_extractor import DESC_HEADERS_KEY, get_description_row_from_json, CONTENT_HEADERS_KEY, get_content_row_from_json, COMMENT_HEADERS_KEY, get_comment_row_from_json, CRITIQUE_HEADERS_KEY, get_critique_row_from_json
from utils import get_data_from_path, export_csv, list_file_name_with_extension
from data import DESC_JSON_PATH, DESC_CSV_PATH, CONTENT_CSV_PATH, CONTENT_JSON_PATH, COMMENT_CSV_PATH, COMMENT_JSON_PATH, REVIEW_ROOT_JSON_PATH, CRITIQUE_CSV_PATH, CRITIQUE_JSON_PATH, REVIEW_ROOT_CSV_PATH, ONE_REVIEW_ROOT_JSON_PATH, ONE_REVIEW_CSV_JSON_PATH


def get_critique_row(_file_name):
    """
    get critique row to create csv
    """
    print("critique csv --> %s" % _file_name)
    critique_json_path = CRITIQUE_JSON_PATH + _file_name
    critique_json = get_data_from_path(critique_json_path)
    critique_rows = []
    for critique in critique_json:
        critique_row = get_critique_row_from_json(critique)
        critique_rows.append(critique_row)
    return critique_rows


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


def export_critique(_json_path, _csv_path):
    critique_files = list_file_name_with_extension(_json_path, "json")

    csv_rows = []
    for file_name in critique_files:
        rows = get_critique_row(file_name)
        csv_rows.extend(rows)

    export_csv(CRITIQUE_HEADERS_KEY, csv_rows, _csv_path)


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


def export_review(_json_path, _csv_path):
    export_desc(_json_path + DESC_JSON_PATH, _csv_path + DESC_CSV_PATH)
    export_content(_json_path + CONTENT_JSON_PATH, _csv_path + CONTENT_CSV_PATH)
    export_comment(_json_path + COMMENT_JSON_PATH, _csv_path + COMMENT_CSV_PATH)
    export_critique(_json_path + CRITIQUE_JSON_PATH, _csv_path + CRITIQUE_CSV_PATH)


def main():
    arguments = sys.argv[1:]
    if not arguments:
        print("please offer argument: 1 for one review, 2 for all reviews")
        return
    if arguments[0].strip() == '1':
        export_review(ONE_REVIEW_ROOT_JSON_PATH, ONE_REVIEW_CSV_JSON_PATH)
    elif arguments[0].strip() == '2':
        export_review(REVIEW_ROOT_JSON_PATH, REVIEW_ROOT_CSV_PATH)
    else:
        print("please offer argument: 1 for one review, 2 for all reviews")


if __name__ == '__main__':
    main()

