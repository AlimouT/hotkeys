import win32clipboard

### Reverse by character

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content = content[::-1]
content = content.replace('\n\r', '\r\n')
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()