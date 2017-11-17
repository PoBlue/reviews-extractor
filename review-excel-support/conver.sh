#!/bin/bash

# file_path="../review-csv"
# take one param, like: `bash conver.sh ../one-review/`, file path for conver it
file_path=$1
for file in `ls ${file_path}`
do
    echo ${file}
    iconv -f UTF-8 -t GB18030 "${file_path}/${file}" > ${file}
done