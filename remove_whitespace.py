import win32clipboard

### Remove whitespace
# Maybe keep empty lines?

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content_list = content.splitlines()
content_list = [x.strip()+'\r' for x in content_list if x.strip() != '']
content = ''.join(content_list)
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()