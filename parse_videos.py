import re
import json

"""
Parses video URLs and titles from HTML extracted from channel page into videos.json
"""

videos = {}

with open("videos.html") as f:
    for video in f.readlines():
        parts = re.search(r'title="([^"]+)" href="([^"&]+)("|&)', video)
        videos[parts.group(2)] = parts.group(1)

outfile = open("videos.json", "w")
json.dump( videos, outfile, indent=4 )
outfile.close()

