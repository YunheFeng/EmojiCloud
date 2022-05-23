# EmojiCloud

We propose and develop open-source EmojiCloud to visualize a cluster of emojis according to associated frequency weights.

## Description

EmojiCloud is an open-source Python-based emoji cloud visualization tool that generates a quick and straightforward understanding of emojis from the perspective of frequency and importance. EmojiCloud is flexible enough to support diverse drawing shapes, such as rectangles, ellipses, and image masked canvases. We also follow inclusive and personalized design principles to cover the unique emoji designs from seven emoji vendors (e.g., Twitter, Apple, and Windows) and allow users to customize plotted emojis and background colors. We hope EmojiCloud can benefit the whole emoji community due to its flexibility, inclusiveness, and customizability.

## Getting Started

### Dependencies

* [PIL](https://pypi.org/project/Pillow/)

### Installing

```
pip install EmojiCloud
```

### Usage

* **Plot different canvases**
```Python 
from EmojiCloud import EmojiCloud

# set emoji weights by a dict with key: emoji in unicode, value: weight
dict_weight = {'1f1e6-1f1e8': 1.1, '1f4a7': 1.2, '1f602': 1.3, '1f6f4': 1.4, '1f6f5': 1.5, '1f6f6': 1.6, '1f6f7': 1.7, '1f6f8': 1.8, '1f6f9': 1.9, '1f6fa': 2.0, '1f6fb': 2.1, '1f6fc': 2.2, '1f7e0': 2.3, '1f9a2': 2.4, '1f9a3': 2.5, '1f9a4': 2.6, '1f9a5': 2.7, '1f9a6': 2.8, '1f9a8': 2.9, '1f9a9': 3.0}

# emoji vendor 
emoji_vendor = 'Twitter'

# masked canvas 
img_mask = 'twitter-logo.png'
thold_alpha_contour = 10 
contour_width = 5
contour_color = (0, 172, 238, 255)
saved_emoji_cloud_name = 'emoji_cloud_masked.png'
EmojiCloud.plot_masked_canvas(img_mask, thold_alpha_contour, contour_width, contour_color, emoji_vendor, dict_weight, saved_emoji_cloud_name)

# rectangle canvas 
canvas_w = 72*10
canvas_h = 72*4
saved_emoji_cloud_name = 'emoji_cloud_rectangle.png'
EmojiCloud.plot_rectangle_canvas(canvas_w, canvas_h, emoji_vendor, dict_weight, saved_emoji_cloud_name)

# ellipse canvas
canvas_w = 72*10
canvas_h = 72*4
saved_emoji_cloud_name = 'emoji_cloud_ellipse.png'
EmojiCloud.plot_ellipse_canvas(canvas_w, canvas_h, emoji_vendor, dict_weight, saved_emoji_cloud_name)
```

<p float="left">
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_masked.png" height="100" />
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_rectangle.png" height="100" />
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_ellipse.png" height="100" />
</p>

* **Plot different vendors**
```Python 
from EmojiCloud import EmojiCloud

# set emoji weights by a dict with key: emoji in unicode, value: weight
dict_weight = {'U+1F600': 1.1, 'U+1F601': 1.2, 'U+1F602': 1.3, 'U+1F603': 1.4, 'U+1F604': 1.5, 'U+1F605': 1.6, 'U+1F606': 1.7, 'U+1F607': 1.8, 'U+1F608': 1.9, 'U+1F609': 2.0, 'U+1F610': 2.1, 'U+1F612': 2.2, 'U+1F613': 2.3, 'U+1F614': 2.4, 'U+1F616': 2.5, 'U+1F617': 2.6, 'U+1F618': 2.7, 'U+1F619': 2.8, 'U+1F620': 2.9, 'U+1F621': 3.0, 'U+1F622': 3.1, 'U+1F624': 3.2, 'U+1F625': 3.3, 'U+1F628': 3.4, 'U+1F629': 3.5, 'U+1F630': 3.6, 'U+1F631': 3.7, 'U+1F632': 3.8, 'U+1F633': 3.9, 'U+1F634': 4.0, 'U+1F635': 4.1, 'U+1F637': 4.2, 'U+1F638': 4.3, 'U+1F639': 4.4, 'U+1F640': 4.5, 'U+1F641': 4.6, 'U+1F642': 4.7, 'U+1F643': 4.8, 'U+1F644': 4.9, 'U+1F910': 5.0, 'U+1F911': 5.1, 'U+1F912': 5.2, 'U+1F913': 5.3, 'U+1F914': 5.4, 'U+1F915': 5.5, 'U+1F917': 5.6, 'U+1F920': 5.7, 'U+1F921': 5.8, 'U+1F922': 5.9, 'U+1F923': 6.0, 'U+1F924': 6.1, 'U+1F925': 6.2, 'U+1F927': 6.3, 'U+1F929': 6.4, 'U+1F970': 6.5, 'U+1F971': 6.6, 'U+1F973': 6.7, 'U+1F974': 6.8, 'U+1F975': 6.9, 'U+1F976': 7.0, 'U+1FAE1': 7.1, 'U+1FAE2': 7.2, 'U+1FAE3': 7.3}

# emoji vendors
list_vendor = ['Google', 'Windows', 'Apple', 'Twitter', 'Meta', 'JoyPixels', 'Samsung']
for emoji_vendor in list_vendor:
    # circle canvas
    canvas_w = 72*10
    canvas_h = 72*10
    saved_emoji_cloud_name = 'emoji_cloud_circle_' + emoji_vendor + '.png'
    EmojiCloud.plot_ellipse_canvas(canvas_w, canvas_h, emoji_vendor, dict_weight, saved_emoji_cloud_name)
```

<p float="left">
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_circle_Google.png" height="140" />
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_circle_Windows.png" height="140" />
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_circle_Apple.png" height="140" />
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_circle_Twitter.png" height="140" />
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_circle_Meta.png" height="140" />
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_circle_JoyPixels.png" height="140" />
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_circle_Samsung.png" height="140" />
</p>


* **Plot customized emojis**
```Python 
from EmojiCloud import EmojiCloud

# set emoji weights by a dict with key: emoji in unicode, value: weight
dict_weight = {'1F1E6-1F1F7': 1.1, '1F1E7-1F1EA': 1.2, '1F1E7-1F1F7': 1.3, '1F1E8-1F1E6': 1.4, '1F1E8-1F1F4': 1.5, '1F1E8-1F1F5': 1.6, '1F1E9-1F1EA': 1.7, '1F1E9-1F1F0': 1.8, '1F1EA-1F1E8': 1.9, '1F1EA-1F1F8': 2.0, '1F1EC-1F1ED': 2.1, '1F1EC-1F1F7': 2.2, '1F1ED-1F1F7': 2.3, '1F1EE-1F1F7': 2.4, '1F1EF-1F1F5': 2.5, '1F1F0-1F1F7': 2.6, '1F1F2-1F1FD': 2.7, '1F1F3-1F1F1': 2.8, '1F1F5-1F1F1': 2.9, '1F1F5-1F1F9': 3.0, '1F1F6-1F1E6': 3.1, '1F1F7-1F1F8': 3.2, '1F1F8-1F1E6': 3.3, '1F1F8-1F1F3': 3.4, '1F1FA-1F1F8': 3.5, '1F1FA-1F1FE': 3.6, '26BD': 3.7, '1F3C6': 3.8}
dict_customized = {'1F3C6':'./trophy_emoji.png'}
# dict_customized = {}

# emoji vendor 
emoji_vendor = 'Twitter'

# rectangle canvas 
canvas_w = 72*10
canvas_h = 72*4
canvas_color = 'green'
# saved_emoji_cloud_name = 'emoji_cloud_customized.png'
saved_emoji_cloud_name = 'emoji_cloud_original.png'
EmojiCloud.plot_rectangle_canvas(canvas_w, canvas_h, emoji_vendor, dict_weight, saved_emoji_cloud_name, dict_customized, canvas_color)
```

<p float="left">
    <img src="https://github.com/YunheFeng/EmojiCloud/blob/main/tests/test_results/emoji_cloud_original.png" height="100" />
</p>

**All the above testing scripts and data are available at https://github.com/YunheFeng/EmojiCloud/tree/main/tests.**

## Authors

Contributors names and contact info

[Yunhe Feng](https://yunhefeng.me/)

## License

See the LICENSE.md file for details

## Paper

Our [paper](https://yunhefeng.me/material/EmojiCloud.pdf) has been accepted at the 5th International Workshop on Emoji Understanding and Applications in Social Media ([EMOJI@NAACL 2022](https://aiisc.ai/emoji2022/)). Online EmojiCloud services will be available soon at [www.emojicloud.org](www.emojicloud.org). 
