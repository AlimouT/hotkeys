import win32clipboard

# Sort content of clipboard by line and remove line-pairs (lines that are there are even number of times)
# Lines that exist an odd number of times are kept once.

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content_list = content.splitlines()
content_list.sort()
content_list = [x+'\n' for x in content_list if x != '']
temp_line = ''
i = 1
while i < len(content_list):
	if content_list[i] == content_list[i-1]:
		content_list.pop(i)
		content_list.pop(i-1)
	else:
		i+=1
content = ''.join(content_list)
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()