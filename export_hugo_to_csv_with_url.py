import csv
import os
from datetime import datetime

def extract_data_from_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()

        # Split by the +++ delimiter
        parts = content.split("+++")
        if len(parts) < 3:
            return None
        
        # Extract header and content
        header = parts[1]
        post_content = parts[2].strip()

        # Extract date and title from the header
        post_datetime = post_date = title = post_url = None
        for line in header.strip().split("\n"):
            line = line.strip()
            if line.startswith("date = "):
                post_date = line.split("=", 1)[1].strip()
                post_date = post_date.replace('"', '')
                # 2002-06-28T15:56:41+00:00
                post_datetime = datetime.strptime(post_date[:-6], '%Y-%m-%dT%H:%M:%S')
            if line.startswith("slug = "):
                slug = line.split("=", 1)[1].strip()
                slug = slug.replace('"', '')
            elif line.startswith("title = "):
                title = line.split("=", 1)[1].strip().strip('"')

        post_url = "https://conoroneill.com/" + str(post_datetime.year) + "/" + str(post_datetime.month) + "/" + str(post_datetime.day) + "/" + slug + "/"
        print(post_url)

        return title, post_content, post_url

    return None

def main(directory, output_csv):
    blogposts = []

    # Iterate over each file in the specified directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                # print(filename)
                result = extract_data_from_file(os.path.join(root, filename))
                if result:
                    blogposts.append(result)

    # Write to CSV
    with open(output_csv, 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["title", "content", "url"])
        writer.writerows(blogposts)

if __name__ == '__main__':
    # Adjust the 'directory' and 'output_csv' values as needed
    directory = "C:/gitwork/hugo.conoroneill.com/content/post"
    output_csv = "exported_blogposts_with_url.csv"
    main(directory, output_csv)
