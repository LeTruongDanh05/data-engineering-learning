if [ -z "$TARGET_DEPT" ]; then
    echo "Error: You did not declare environment variable yet! TARGET_DEPT!"
    echo "Please type this context first: export TARGET_DEPT=\"Tên_Phòng_Ban\""
    exit 1
  fi
> data_dept_employees.csv
grep "$TARGET_DEPT" employees.csv >> data_dept_employees.csv
echo "Filtered successfully! $TARGET_DEPT"
