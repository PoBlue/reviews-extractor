#!/bin/bash

file_path="../review-csv"
for file in `ls ${file_path}`
do
    echo ${file}
    iconv -f UTF-8 -t GB18030 "${file_path}/${file}" > ${file}
done