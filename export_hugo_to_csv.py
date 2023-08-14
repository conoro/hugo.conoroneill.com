import csv
import os

def extract_data_from_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()

        # Split by the +++ delimiter
        parts = content.split("+++")
        print(len(parts))
        if len(parts) < 3:
            return None
        
        # Extract header and content
        header = parts[1]
        post_content = parts[2].strip()

        # Extract date and title from the header
        date = title = None
        for line in header.strip().split("\n"):
            line = line.strip()
            if line.startswith("date = "):
                date = line.split("=", 1)[1].strip()
            elif line.startswith("title = "):
                title = line.split("=", 1)[1].strip().strip('"')

        if date and title:
            return date, title, post_content

    return None

def main(directory, output_csv):
    blogposts = []

    # Iterate over each file in the specified directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                print(filename)
                result = extract_data_from_file(os.path.join(root, filename))
                if result:
                    blogposts.append(result)

    # Write to CSV
    with open(output_csv, 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["date", "title", "contents"])
        writer.writerows(blogposts)

if __name__ == '__main__':
    # Adjust the 'directory' and 'output_csv' values as needed
    directory = "C:/gitwork/hugo.conoroneill.com/content/post"
    output_csv = "exported_blogposts.csv"
    main(directory, output_csv)
