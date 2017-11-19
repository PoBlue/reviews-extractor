# =VLOOKUP(B:B, '/Users/moweiquan/Desktop/review-excel-support/[content.csv]content'!$B:$C,  2, FALSE)
def main():
    # auto uppcase
    lookup_value_col = 'B'
    path_to_csv = '/Users/moweiquan/Desktop/review-excel-support/'
    file_name = 'content'
    table_name = 'content'
    from_col_be_look_up = 'B'
    to_col_be_look_up = 'C'
    index_col = '2'
    match_flag = 'FALSE'

    cmd = "=VLOOKUP({match_col}:{match_col}," \
          "'{csv_path}[{file_name}.csv]{table_name}'!${from_col}:${to_col}," \
          "  2, FALSE)".format()
    print(cmd)
    pass

if __name__ == '__main__':
    main()
