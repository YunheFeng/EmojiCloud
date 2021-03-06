from EmojiCloud import EmojiCloud

# set emoji weights by a dict with key: emoji by unicode, value: weight
dict_weight = {'ðĶðĻ': 1.1, 'ð§': 1.2, 'ð': 1.3, 'ðī': 1.4, 'ðĩ': 1.5, 'ðķ': 1.6, 'ð·': 1.7, 'ðļ': 1.8, 'ðđ': 1.9, 'ðš': 2.0, 'ð': 2.1, 'ð': 2.2, 'ð ': 2.3, 'ðĶĒ': 2.4, 'ðĶ': 2.5, 'ð': 2.6, 'ðĶĨ': 2.7, 'ðĶĶ': 2.8, 'ðĶĻ': 2.9, 'ðĶĐ': 3.0}

# emoji vendor 
emoji_vendor = 'Google'

# circle canvas 
canvas_w = 72*5
canvas_h = 72*5
saved_emoji_cloud_name = 'emoji_cloud_circle.png'
EmojiCloud.plot_ellipse_canvas(canvas_w, canvas_h, emoji_vendor, dict_weight, saved_emoji_cloud_name)


