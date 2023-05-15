import os
from datetime import datetime


def modify_date_metadata(file, original_timestamp, modified_timestamp):
    try:
        og_timestamp = original_timestamp.timestamp()
        mod_timestamp = modified_timestamp.timestamp()

        os.utime(file, (og_timestamp, mod_timestamp))

        print(f"Metadata modified for file: {file}")
    except Exception as e:
        print(f"Error updating metadata timestamp! {e}")


if __name__ == "__main__":
    file = 'limpi.png'

    current_time = datetime.now()

    modified_time_str = input("Please enter the desired timestamp configuration (YYYY-MM-DD HH:MM:SS). example: "
                              "'2022-02-16 16:20:37' ")

    try:
        modified_time = datetime.strptime(modified_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid timestamp! Use YYYY-MM-DD HH:MM:SS!")
        exit()

    new_creation_time = current_time
    new_modification_time = modified_time

    modify_date_metadata(file, new_creation_time, new_modification_time)
