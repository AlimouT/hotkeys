import win32clipboard

### Remove Duplicates
# Maybe keep empty lines?
# Maybe remove empty lines that are consecutive?

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content_list = content.splitlines()
content_list = list(dict.fromkeys(content_list))
content_list = [x+'\r' for x in content_list if x != '']
content = ''.join(content_list)
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()