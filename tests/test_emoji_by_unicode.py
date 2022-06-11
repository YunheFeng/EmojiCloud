from EmojiCloud import EmojiCloud

# set emoji weights by a dict with key: emoji by unicode, value: weight
dict_weight = {'🇦🇨': 1.1, '💧': 1.2, '😂': 1.3, '🛴': 1.4, '🛵': 1.5, '🛶': 1.6, '🛷': 1.7, '🛸': 1.8, '🛹': 1.9, '🛺': 2.0, '😜': 2.1, '🍉': 2.2, '🟠': 2.3, '🦢': 2.4, '🦄': 2.5, '🕊': 2.6, '🦥': 2.7, '🦦': 2.8, '🦨': 2.9, '🦩': 3.0}

# emoji vendor 
emoji_vendor = 'Google'

# rectangle canvas 
canvas_w = 72*5
canvas_h = 72*5
saved_emoji_cloud_name = 'emoji_cloud_circle.png'
EmojiCloud.plot_ellipse_canvas(canvas_w, canvas_h, emoji_vendor, dict_weight, saved_emoji_cloud_name)
