import os
import re
import csv

# Specify the directory to search
directory = './content/post'

# Regex pattern to find URLs containing "pix.ie"
url_pattern = re.compile(r'https?://[^\s]+flickr\.com[^\s]*')

# CSV file to store results
csv_filename = 'found_flickr_urls.csv'

# Prepare to collect data
data_to_write = []

# Iterate through all files in the specified directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as md_file:
                content = md_file.read()
                urls = url_pattern.findall(content)
                for url in urls:
                    data_to_write.append([file, url])

# Write collected data to CSV file
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Filename', 'URL'])
    writer.writerows(data_to_write)

print(f"Process completed. Data written to {csv_filename}")
