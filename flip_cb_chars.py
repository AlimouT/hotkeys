import win32clipboard

### Reverse saved string

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content[::-1])
win32clipboard.CloseClipboard()

