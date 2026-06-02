if [ -z "$TARGET_DEPT" ]; then
    echo "Error: TARGET_DEPT is empty!"
    exit 1
  fi
BASE_DIR="/home/danh/de_foundations/session01/session01-bash"
  INPUT_FILE="$BASE_DIR/employees.csv"
  OUTPUT_FILE="$BASE_DIR/data_dept_employees.csv"
> "$OUTPUT_FILE"
/bin/grep "$TARGET_DEPT" "$INPUT_FILE" >> "$OUTPUT_FILE"
echo "Filtered successfully! $TARGET_DEPT"
