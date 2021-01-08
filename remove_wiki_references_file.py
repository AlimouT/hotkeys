import re
import os

###	Removing references (and _some_ content within parentheses) from papers / wikipedia text for speedreading.

# Identify Computer (by user account name, and provide the path to the users directory)
run_location = os.environ['DEVICE_IDENTIFIER']
input_file = f'{run_location}/Desktop/Temp/raw_wiki.txt'
output_file = f'{run_location}/Desktop/Temp/processed_wiki.txt'

references_re = re.compile(' ?\((...+?|)\)|\[\d+\]')

with open(input_file, 'r') as input, open(output_file, 'w') as output:
	output.write(re.sub(references_re, '', input.read()))
