import os
import win32clipboard

### Save YouTube videos to file for later download.
save_location = f'{os.environ["DEVICE_IDENTIFIER"]}/Programming/yt2mp3'
yt_url_file = f'{save_location}/to_ytdl.txt'

if not os.path.exists(save_location):
	os.makedirs(save_location)

def clean_yt_url(base_url):
	if 'youtu.be' in base_url:
		base_url = f'www.youtube.com/watch?v=[base_url.find("youtu.be/")+9:]'
	if '&list=' in base_url:
		base_url = base_url[:base_url.find('&list=')]
	return base_url

win32clipboard.OpenClipboard()
yt_url = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

yt_url = f'{clean_yt_url(yt_url)}\n'

with open(yt_url_file, 'w') as file:
	file.write(yt_url)
