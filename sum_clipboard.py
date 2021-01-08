import win32clipboard
import re

### Sum numbers
# Extract all numbers
regex = r"(\d+\.?\d*|\d*\.\d+)"

win32clipboard.OpenClipboard()
content = win32clipboard.GetClipboardData()
total = sum([sum([float(number) for number in re.findall(regex, line)]) for line in content.splitlines()])

win32clipboard.CloseClipboard()
input(f'{total}\n')

###	Other possibility - Set clipboard to sum:
# win32clipboard.EmptyClipboard()
# win32clipboard.SetClipboardText(str(total))
# win32clipboard.CloseClipboard()
