import re
import win32clipboard

###	Removing references (and _some_ content within parentheses) from papers / wikipedia text for speedreading.

references_re = re.compile(' ?\((...+?|)\)|\[\d+\]')

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
content = re.sub(references_re, '', content)
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(content)
win32clipboard.CloseClipboard()