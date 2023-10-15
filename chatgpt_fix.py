import openai
import time
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_titles():
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        request_timeout=20,
        messages=[
            {
                "role": "system",
                "content": "You will be given a Louis Rossmann video title. Louis wants to stop using FULLY CAPITALIZED words from his titles and make them less clickbaity. Convert CAPITALIZED words into regular words in one version of the title (with no other modifications), and create another, less clickbaity title with more modifications if neccessary. Acronyms shall stay capitalized."
            },
            {
                "role": "user",
                "content": title
            }
        ],
        function_call={"name": "give_titles", "arguments": ["uncapitalized", "unclickbaitified"]},
        functions=[
            {
                "name": "give_titles",
                "description": "Use this function to give the user the modified titles",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "uncapitalized": {
                            "type": "string",
                            "description": "The uncapitalized title, with no other modifications"
                        },
                        "unclickbaitified": {
                            "type": "string",
                            "description": "The unclickbaitified title"
                        }
                    }
                }
            }
        ]
    )

with open(f"2_caps_videos.json") as f:
    videos = json.load(f)

if os.path.exists("new_titles.json"):
    with open(f"new_titles.json") as f:
        data = json.load(f)
else:
    data = []

skip = 0 # for skipping if JSON parsing fails
number = 0
for url, title in videos.items():
    number += 1

    if number < skip:
        continue

    retry = True
    while retry:
        try:
            response = get_titles()
            retry = False
        except Exception:
            print("NOTICE: Retry...")
            time.sleep(5)

    titles = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])

    print(str(number) + ": " + title + " => " + str(titles.get("uncapitalized")) + " => " + str(titles.get("unclickbaitified")))

    data.append({
        "url": url,
        "original": title,
        "uncapitalized": titles.get("uncapitalized"),
        "unclickbaitified": titles.get("unclickbaitified"),
    })

    with open("new_titles.json", "w") as f:
        json.dump( data, f, indent=4 )

