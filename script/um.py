# Remove Ums from the given transcript file
# ToDo:
# show stats how many were removed
# file encoding

import argparse
import re

# Remove um at the start of a sentence, and capitalise the next word
def remove_first_um(text, um):
	um = '([.?!:]) ' + um + ' ([A-Za-z0-9])'
	return re.sub(
		re.compile(um,flags=re.IGNORECASE),
		lambda pat: pat.group(1) + ' ' + pat.group(2).upper(),
		text)

# Remove all Ums
def remove_all_um(text, um):
	return re.sub(' ' + um + ' ',
		' ',
		text,
		flags=re.IGNORECASE)

def main():
	ums = ['um', 'uh', 'mhm']
	
	parser = argparse.ArgumentParser()
	parser.add_argument("path")
	args = parser.parse_args()
	filename = args.path

	f = open(filename, 'r') # , encoding='utf-8'
	text = f.read()
	f.close()

	# Keep removing ums from the start of sentences until none are removed
	new_length = len(text)
	old_length = new_length + 1
	while new_length < old_length:
		old_length = new_length
		for um in ums:
			text = remove_first_um(text, um)
		new_length = len(text)

	for um in ums:
		text = remove_all_um(text, um)

	f = open(filename, 'w')
	f.write(text)
	f.close()

main()
