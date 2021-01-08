import win32clipboard

### Remove PDF linebreaks
#	If the line ends with a split word, remove the dash

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content = content.replace('­\r\n', '').replace('\r\n', ' ')
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()