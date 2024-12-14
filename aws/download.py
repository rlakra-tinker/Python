#
# Author: Rohtash Lakra
#
import csv
from io import BytesIO, TextIOWrapper
from io import StringIO

import boto3
import pandas as pd


class S3Client:

    # read as csv
    def readCsvFile(self, csv_bytes):
        print("readCsvFile")
        csv_bytes.seek(0)
        reader = csv.DictReader(csv_bytes)
        print(f"reader={reader}")
        for row in reader:
            print(f"row={row}")

    def readCsvBytes(self, csv_bytes):
        print("readCsvBytes")
        """Reads the Csv Bytes as String"""
        # Decode bytes to a string and wrap in StringIO
        # with open(file_name, encoding='utf-8-sig') as csvfile:
        string_io = StringIO(csv_bytes.getvalue())
        # string_io = StringIO(csv_bytes)
        # Read the CSV data using csv.reader
        csv_bytes.seek(0)
        reader = csv.reader(string_io)
        # Convert to a list of dictionaries
        output_list = [dict(zip(reader.__next__(), row)) for row in reader]
        print(output_list)

    def readCsvByte(self, csv_bytes):
        print("readCsvByte")
        # Read the CSV data
        csv_bytes.seek(0)
        reader = csv.reader(TextIOWrapper(csv_bytes, encoding='utf-8-sig'))
        print(f"reader={reader}")
        for row in reader:
            print(f"row={row}")

    def readCsvWithPandas(self, csv_bytes):
        # Read the CSV data into a DataFrame
        print("readCsvWithPandas")
        csv_bytes.seek(0)
        df = pd.read_csv(csv_bytes)
        print("reading pandas")
        print(df)

        for index, (key, value) in enumerate(df.items()):
            print(f"index={index}, key={key}, value={value}")

        print()
        column_names, columns = zip(*df.items())
        print(f"column_names={column_names}")
        print(f"columns={columns}")

    def download(self, bucket_name, file_name) -> BytesIO:
        print(f"+download({bucket_name}, {file_name})")
        s3_file_bytes = BytesIO()  # Buffered I/O implementation using an in-memory bytes buffer.
        # print(f"s3_file_bytes={s3_file_bytes}")
        s3 = boto3.client('s3')
        s3.download_fileobj(bucket_name, file_name, s3_file_bytes)
        print(f"-download() {bucket_name}/{file_name}, s3_file_bytes={s3_file_bytes}")
        return s3_file_bytes


if __name__ == '__main__':
    s3Client = S3Client()
    bucket_name = "tod-s3-dev-ue1-push-notification-rxlo"
    file_name = "prod_11_28.csv"
    s3_file_bytes = s3Client.download(bucket_name, file_name)
    print(f"s3_file_bytes={s3_file_bytes}")
    # s3Client.readCsvFile(s3_file_bytes)  # not Working
    # s3Client.readCsvBytes(s3_file_bytes) # Not Working
    # s3Client.readCsvByte(s3_file_bytes) # Working
    s3Client.readCsvWithPandas(s3_file_bytes)  # Working
