from EmojiCloud import EmojiCloud

# set emoji weights by a dict with key: emoji by codepoint, value: weight
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


