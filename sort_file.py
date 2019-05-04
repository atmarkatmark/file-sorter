# coding: utf-8

import sys
import os
import shutil

config = 'config.txt'
rules = []
'''
rules = [
	{ 'key': '.txt', 'dest': '.\TEXT' },
	{ 'key': '.csv', 'dest': '.\CSV' }
]
'''

def errorExit(message, code = -1):
	print(message)
	sys.exit(code)

# Check arguments
if len(sys.argv) != 2:
	errorExit('Usage: {[0]} TARGET_DIR'.format(sys.argv))

target = sys.argv[1]

# Check rules
with open(config, encoding = 'utf-8') as f:
	for l in f.readlines():
		l = l.split('\t')
		rules.append({
			'key': l[0].strip(),
			'dest': l[1].strip()
		})
if len(rules) < 1:
	errorExit('No rules defined.')

# Check target path
if not os.path.isdir(target):
	errorExit('The directory you specified is not a directory.')

# Scan target dir
for file in os.listdir(target):
	path = os.path.join(target, file)

	# Currently, recursive scanning is disabled
	if os.path.isdir(path):
		print('{} is a directory. Skipping.'.format(path))
		continue
	
	for i in rules:
		if i['key'] in file:
			sys.stdout.write('Copying {} ... '.format(file))
			try:
				shutil.move(path, i['dest'])
			except:
				print('failed. Skipping...')
			else:
				print('done.')
			break