import pikepdf
import os
from datetime import datetime


def pdf_metadata(path):
    try:
        pdf = pikepdf.Pdf.open(path)
        pdf_data = dict(pdf.docinfo)
        return pdf_data
    except Exception as e:
        print(f"Error: {e}")
        return None


def format_date(creation_date):
    try:
        creation_date_str = str(creation_date)

        date = creation_date_str[2:10]
        time = creation_date_str[10:18]
        timezone = creation_date_str[18:].replace("'", "")

        formatted_time = f"{date} {time}{timezone}"
        creation_date = datetime.strptime(formatted_time, "%Y%m%d %H%M%S%z")

        return creation_date.strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception as e:
        print(f"Error formatting date: {e}")
        return None


def print_metadata(metadata, path):
    if metadata is not None:
        print(f"File: {path}")
        for key, value in metadata.items():
            if key == "/CreationDate":
                formatted_date = format_date(value)
                print(f'{key} : {formatted_date}')
            else:
                print(f'{key} : {value}')

        file_size = os.path.getsize(path)
        modification_date = datetime.fromtimestamp(os.path.getmtime(path))
        creation_date = datetime.fromtimestamp(os.path.getctime(path))

        print(f'File has size of: {file_size} bytes.')
        print(f'Modification date: {modification_date}.')
        print(f'Creation date: {creation_date}.')

    else:
        print("Failed to get PDF data, please try again!")


if __name__ == "__main__":
    path = '185.pdf'
    metadata = pdf_metadata(path)
    print_metadata(metadata, path)
