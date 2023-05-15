from PIL import Image, ExifTags


def extract_all_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image.getexif()

        if exif_data:
            for tag, value in exif_data.items():
                tag_name = ExifTags.TAGS.get(tag, tag)
                print(f'{tag_name} : {value}')
        else:
            print("No Exif data found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    image_path = 'IMG_20230722_233459.jpg'
    extract_all_metadata(image_path)
