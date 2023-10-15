import json

"""
Filters out videos that have cap_count_threshold uppercase characters back to back in them
"""

cap_count_threshold = 2

with open("videos.json") as f:
    videos = json.load(f)

caps_videos = {}

for url, title in videos.items():
    has_caps = False
    for i in range(0, len(title)-cap_count_threshold+1):
        if title[i:(i+cap_count_threshold)].isalpha() and title[i:(i+cap_count_threshold)].isupper():
            has_caps = True
            break
    if has_caps:
        caps_videos[url] = title

with open(f"{cap_count_threshold}_caps_videos.json", "w") as f:
    json.dump( caps_videos, f, indent=4 )
