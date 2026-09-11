"""
### Assignment 2: Multi-Format Log Converter (Text to CSV & JSON)
#### Scenario
A server records raw access events as unformatted plain-text log lines. You need to parse the log lines into structured records and export them to both CSV and JSON formats.

#### Problem Description
Create a function `convert_log_file(input_log_path, output_csv_path, output_json_path)`:
1. Each line in `input_log_path` follows the format:
   `"<TIMESTAMP> | <USER_ID> | <ENDPOINT> | <STATUS_CODE>"`
   (e.g., `"2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200"`).
2. Parses each line into a dictionary containing keys: `timestamp`, `user_id`, `endpoint`, `status_code` (as integer).
3. Writes all parsed records to `output_csv_path` with a header row using `csv.DictWriter`.
4. Writes the list of records to `output_json_path` with an indentation of 2 spaces using `json.dump()`.

#### Example Walkthrough
```python
convert_log_file("server_access.log", "access_records.csv", "access_records.json")
```

---
"""
import csv
import json

logs=[
    "2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200",
    "2026-09-01 10:20:10 | USR103 | /api/v1/login | 200",
    "2026-09-01 10:25:45 | USR104 | /api/v1/predict | 404"
]

with open("server_access.log","w") as file:
    for log in logs:
        file.write(log+"\n")

def convert_log_file(input_log_path,output_csv_path,output_json_path):
    records=[]

    with open(input_log_path,"r") as file:
        for line in file:
            parts=line.strip().split("|")

            record={
                "timestamp":parts[0].strip(),
                "user_id":parts[1].strip(),
                "endpoint":parts[2].strip(),
                "status_code":int(parts[3].strip())
            }

            records.append(record)

    with open(output_csv_path,"w",newline="") as file:
        fields=["timestamp","user_id","endpoint","status_code"]
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

    with open(output_json_path,"w") as file:
        json.dump(records,file,indent=2)

convert_log_file("server_access.log","access_records.csv","access_records.json")