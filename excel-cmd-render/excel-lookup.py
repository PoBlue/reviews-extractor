# =VLOOKUP(B:B, '/Users/moweiquan/Desktop/review-excel-support/[content.csv]content'!$B:$C,  2, FALSE)
from utils import copy_text_to_mac_pasteboard

def look_up_cmd(lookup_value_col, path_to_csv, file_name, table_name, from_col_be_look_up, to_col_be_look_up, index_col):
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
    return cmd


def get_look_up_desc(lookup_value_col, from_col_be_look_up, to_col_be_look_up, index_col):
    path_to_csv = ''
    file_name = 'description'
    table_name = 'description'
    return look_up_cmd(lookup_value_col, path_to_csv,
                       file_name, table_name, 
                       from_col_be_look_up, to_col_be_look_up,
                       index_col)


def get_look_up_content(lookup_value_col, from_col_be_look_up, to_col_be_look_up, index_col):
    path_to_csv = ''
    file_name = 'content'
    table_name = 'content'
    return look_up_cmd(lookup_value_col, path_to_csv,
                       file_name, table_name, 
                       from_col_be_look_up, to_col_be_look_up,
                       index_col)


def main():
    #set your path to csv
    # path_to_csv = '/Users/moweiquan/Desktop/review-excel-support/'
    path_to_csv = ''
    match_flag = 'FALSE'

    desc_or_content = input('look up to descripiton(1) or content(2) answer 1 or 2 >').strip()
    lookup_value_col = input('what is the orignal match col: >').strip() # 'B'
    from_col_be_look_up = input('what is the col you start looking for >').strip() # 'B'
    to_col_be_look_up = input('what is the col you end up looking >').strip() # 'C'
    index_col = input('what is index of col to present (num) >').strip() # '2'

    if (desc_or_content == '1'):
        cmd = get_look_up_desc(lookup_value_col, from_col_be_look_up, to_col_be_look_up, index_col)
    elif (desc_or_content == '2'):
        cmd = get_look_up_content(lookup_value_col, from_col_be_look_up, to_col_be_look_up, index_col)
    else:
        print('you should choose either 1 for description, 2 for content')

    print("sucess!!" + '-' * 10)
    print(cmd)
    copy_text_to_mac_pasteboard(cmd)

if __name__ == '__main__':
    main()
