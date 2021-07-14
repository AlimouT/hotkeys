import win32clipboard

### Remove Duplicates
# Maybe remove empty lines that are consecutive?
# Maybe make case insensitive?

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content_list = content.splitlines()
content_list = list(set(content_list))
content = '\n'.join(content_list)
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()