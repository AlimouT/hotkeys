import win32clipboard

# Sort Content of clipboard by line and remove empty lines

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content_dict = {line.lower(): line for line in content.splitlines() if line.strip() != ''}
content_list = [content_dict[key] for key in sorted(content_dict.keys())]
content = '\n'.join(content_list)
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()