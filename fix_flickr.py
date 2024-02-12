import csv
import os
import requests
import time

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

def update_markdown_file(markdown_filename, original_url, local_path):
    with open(markdown_filename, 'r') as file:
        content = file.read()
    content = content.replace(original_url, local_path)
    with open(markdown_filename, 'w') as file:
        file.write(content)

def main(csv_filename):
    flickr_dir = 'flickr'
#    os.makedirs(flickr_dir, exist_ok=True)

    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            markdown_filename = row['filename']
            original_url = row['urls']

            # Extract the filename from the URL
            url_parts = original_url.split('/')
            filename = url_parts[-1]

            # Change _m to _c in filename if necessary
            if filename.endswith('_m.jpg'):
                filename = filename.replace('_m.jpg', '_c.jpg')

            bigger_url = original_url
            if original_url.endswith('_m.jpg'):
                bigger_url = original_url.replace('_m.jpg', '_c.jpg')
            elif original_url.endswith('_c.jpg'):
                bigger_url = original_url
            elif original_url.endswith('_o.jpg'):
                bigger_url = original_url.replace('_o.jpg', '_c.jpg')
            else:
                bigger_url = original_url.replace('.jpg', '_c.jpg')

            local_filename = os.path.join(flickr_dir, filename)
            download_image(bigger_url, local_filename)

            time.sleep(2)

            # Update the local path for markdown replacement
            local_path = f'/images/flickr/2024_download/{filename}'
            update_markdown_file(markdown_filename, original_url, local_path)

if __name__ == "__main__":
    csv_filename = 'found_flickr_urls.csv'
    main(csv_filename)
