import win32clipboard

### Reverse by line

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content_list = content.splitlines()
content_list = content_list[::-1]
content_list = [x+'\r' for x in content_list if x != '']
content = ''.join(content_list)
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()