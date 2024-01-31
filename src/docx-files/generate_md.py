import yaml
from datetime import date

import subprocess

updated_date = date.today()
updated_date = updated_date.strftime("%B %d, %Y")

def generate_post():
    metadata = {
        "layout": "../../layouts/MarkdownPostLayout.astro",
        "title": "My Fourth Blog Post",
        "author": "Harith Onigemo",
        "description": "This post will show up on its own!",
        "image": {
            "url": "https://docs.astro.build/default-og-image.png",
            "alt": "The word astro against an illustration of planets and stars.",
        },
        "pubDate": str(updated_date),
        "tags": ["astro", "successes"],
    }

    with open("./src/docx-files/metadata.yaml", "r") as file:
        metadata = yaml.load(file, Loader=yaml.FullLoader)
        metadata["pubDate"] = str(updated_date)
        print(metadata)

    for key, value in metadata.items():
        input_value = input(f"Enter {key} (default: {value}): ")
        if input_value:
            if key == "tags":
                metadata[key] = input_value.split(",")
            elif key == "image":
                metadata[key]["url"] = input_value
                metadata[key]["alt"] = input(f"Enter {key} alt (default: {value}): ")
            else:
                metadata[key] = input_value


    with open("./src/docx-files/metadata.yaml", "w") as file:
        yaml.dump(metadata, file)


    pandoc_command = [
        "pandoc",
        f"./src/docx-files/{metadata['title']}.docx",
        "-f",
        "docx",
        "-t",
        "markdown",
        "-s",
        "-o",
        f"./src/content/posts/{metadata['title']}.md",
        "--metadata-file=./src/docx-files/metadata.yaml",
        # "--list-tables=true",
        f"--extract-media=./public/{metadata['title']}",
        # "--template=./src/docx-files/custom_template.md",
    ]

    subprocess.run(pandoc_command)

def generate_meetings():
    metadata = {
        "layout": "../../layouts/MarkdownPostLayout.astro",
        "week": "week1",
        "author": "Harith Onigemo",
        "description": "This post will show up on its own!",
        "pubDate": str(updated_date),
        "tags": ["meetings"],
    }

    try:
        with open("./src/docx-files/meeting_metadata.yaml", "r") as file:
            if yaml.load(file, Loader=yaml.FullLoader) != None:
                metadata = yaml.load(file, Loader=yaml.FullLoader)
                metadata["pubDate"] = str(updated_date)
            print(metadata)
    except FileNotFoundError:
        print("File not found")

    meeting_file = f"---\n"

    for key, value in metadata.items():
        input_value = input(f"Enter {key} (default: {value}): ")
        if input_value:
            if key == "tags":
                metadata[key] = input_value.split(",")
            else:
                metadata[key] = input_value
                meeting_file += f"{key}: {input_value}\n"
        else:
            meeting_file += f"{key}: {value}\n"
    meeting_file += "---\n"

    try:
        with open(f"./src/content/meetings/{metadata['week']}.md", "w") as file:
            file.write(meeting_file)
            file.close()
    except FileNotFoundError:
        print("Could not write to file")


def main():
    post_type = input("Enter post type (meeting/post): ")
    if post_type.lower() == "meeting":
        generate_meetings()
    elif post_type.lower() == "post":
        generate_post()
    else:
        print("Invalid post type")

main()


