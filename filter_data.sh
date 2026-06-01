#!/bin/bash

#Check input file available
if [ ! -f "employees.csv" ]; then
    echo "Error: file employees.csv is not available!"
    exit 1
fi

#Save header into a new file
head -n 1 employees.csv > data_dept_employees.csv
#Read each line of file, find the word "Data" and connect (>>) with new file
grep "Marketing" employees.csv >> data_dept_employees.csv

echo "Filter successfully! file: data_dept_employees.csv"
echo "--- The information filtered ---"
cat data_dept_employees.csv
