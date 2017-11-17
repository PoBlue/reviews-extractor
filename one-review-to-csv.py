from data import ONE_REVIEW_CSV_JSON_PATH, ONE_REVIEW_ROOT_JSON_PATH
from dataToCSV import export_review

if __name__ == '__main__':
    export_review(ONE_REVIEW_ROOT_JSON_PATH, ONE_REVIEW_CSV_JSON_PATH)