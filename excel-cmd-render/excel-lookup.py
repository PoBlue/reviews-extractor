# =VLOOKUP(B:B, '/Users/moweiquan/Desktop/review-excel-support/[content.csv]content'!$B:$C,  2, FALSE)
from utils import copy_text_to_mac_pasteboard

def main():
    #set your path to csv
    path_to_csv = '/Users/moweiquan/Desktop/review-excel-support/'
    match_flag = 'FALSE'

    lookup_value_col = input('what is the orignal match col: >').strip() # 'B'
    file_name = input('what is the name of file you looking for: >').strip() # 'content'
    table_name = input('what is name of table yout looking for: >').strip() # 'content'
    from_col_be_look_up = input('what is the col you start looking for >').strip() # 'B'
    to_col_be_look_up = input('what is the col you end up looking >').strip() # 'C'
    index_col = input('what is index of col to present (num) >').strip() # '2'

    cmd = "=VLOOKUP({match_col}:{match_col}, " \
          "'{csv_path}[{file_name}.csv]{table_name}'!${from_col}:${to_col}, " \
          " {look_index_col}, FALSE)".format(
              match_col=lookup_value_col.upper(),
              csv_path=path_to_csv,
              file_name=file_name,
              table_name=table_name,
              from_col=from_col_be_look_up.upper(),
              to_col=to_col_be_look_up.upper(),
              look_index_col=index_col)

    print("sucess!!" + '-' * 10)
    print(cmd)
    copy_text_to_mac_pasteboard(cmd)

if __name__ == '__main__':
    main()
