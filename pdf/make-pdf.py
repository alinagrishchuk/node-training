import os

sections = [
	'intro/README.md',
	'node/README.md',
	'useful-resources/README.md'
]

for filename in sections:
	f = open(os.path.join('..', filename), 'rt')
	print f.read()	
	f.close()

# Making PDF slides:
# 1. Download deck2pdf
# 2. Run this script and output it to pdf.md
# 3. Place contents of pdf.md instead pdf.html's textarea section
# 4. Run deck2pdf --profile=remarkjs pdf.html pdf.pdf
