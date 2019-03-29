def group_by_owners(files):
	dict1={}
	for file in files:
		value = files[file]
		dict1[value] = [k for k,v in files.items() if v == value]
	return dict1



files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))