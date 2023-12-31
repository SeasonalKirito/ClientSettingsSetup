#import requests
#import sys
#import os
#import time
#
#def download_file(url, destination):
#    response = requests.get(url, stream=True)
#    total_size = int(response.headers.get('content-length', 0))
#
#    if total_size <= 0:
#        sys.stdout.write("Unable to determine file size. Downloading...\n")
#    else:
#        sys.stdout.write("Downloading...\n")
#
#    current_size = 0
#
#    with open(destination, 'wb') as file:
#        for data in response.iter_content(chunk_size=1024):
#            current_size += len(data)
#            file.write(data)
#
#            if total_size > 0:
#                downloading_animation(total_size, current_size)
#                sys.stdout.flush()
#                time.sleep(0.1)  # Adjust the sleep duration for a slower animation
#
#    sys.stdout.write("\nDownload complete.\n")
#
#def downloading_animation(total_size, current_size):
#    progress_bar_length = 20
#    progress = int((current_size / total_size) * progress_bar_length)
#    percentage = int((current_size / total_size) * 100)
#
#    bar = "[" + "#" * progress + "-" * (progress_bar_length - progress) + "]"
#    closing_bracket_position = progress_bar_length
#    sys.stdout.write("\r{} {}%]".format(bar, min(percentage, 100)))
#    sys.stdout.flush()
#
## Example usage
#url = "https://raw.githubusercontent.com/movie-web/movie-web/dev/src/index.tsx"
#destination = "index.tsx"
#
#if os.path.exists(destination):
#    os.remove(destination)
#
#download_file(url, destination)

import requests
import sys
import os
import time

def download_file(url, destination):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    if total_size <= 0:
        sys.stdout.write("Unable to determine file size. Downloading...\n")
    else:
        sys.stdout.write("Downloading...\n")

    current_size = 0

    with open(destination, 'wb') as file:
        for data in response.iter_content(chunk_size=1024):
            current_size += len(data)
            file.write(data)

            if total_size > 0:
                downloading_animation(total_size, current_size)
                sys.stdout.flush()
                time.sleep(0.1)  # Adjust the sleep duration for a slower animation

    sys.stdout.write("\nDownload complete.\n")

def downloading_animation(total_size, current_size):
    percentage = int((current_size / total_size) * 100)
    sys.stdout.write("\r[{}%]".format(min(percentage, 100)))
    sys.stdout.flush()

# Example usage
url = "https://raw.githubusercontent.com/movie-web/movie-web/dev/src/index.tsx"
destination = "index.tsx"

if os.path.exists(destination):
    os.remove(destination)

download_file(url, destination)
