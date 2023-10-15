# GPT-Unbaitifier

A YouTube video title un-clickbaitifier just for Louis Rossmann <3

## How it works

The list of videos was scraped by pressing PageDown on the channel page for 5 minutes and copying the source code from Chrome dev tools + doing some VSCode magic to make lines look like this:
```html
</ytd-playlist-thumbnail></div><div id="thumbnail-underlay" class="style-scope ytd-rich-grid-media" hidden=""></div><div id="details" class="style-scope ytd-rich-grid-media"><a id="avatar-link" class="yt-simple-endpoint style-scope ytd-rich-grid-media" tabindex="-1" title="undefined" hidden=""><yt-img-shadow id="avatar" width="48" class="style-scope ytd-rich-grid-media no-transition"><!--css-build:shady--><!--css-build:shady--><img id="img" draggable="false" class="style-scope yt-img-shadow" alt="" width="48"></yt-img-shadow></a><div id="meta" class="style-scope ytd-rich-grid-media"><h3 class="style-scope ytd-rich-grid-media"><ytd-badge-supported-renderer class="top-badge style-scope ytd-rich-grid-media" collection-truncate="" disable-upgrade="" hidden=""></ytd-badge-supported-renderer><a id="video-title-link" class="yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media" aria-label="Title is here" title="Title is here" href="/watch?v=URL_IS_HERE"><yt-formatted-string id="video-title" class="style-scope ytd-rich-grid-media" aria-label="Title is here">Title is here
```

The HTML was then parsed with `parse_videos.py` into `videos.json` with the URLs and titles of videos.

Then `filter_caps.py` was run to filter out titles that do not have capitalized text (more than two consecutive capital letters)

Finally `chatgpy_fix.py` generates an un-capitalized title and an unclickbaity title with ChatGPT API into `new_titles.json`
