import urllib.request

response = urllib.request.urlopen('http://oracle-www.dartmouth.edu/dart/groucho/course_desc.display_course_desc?term=201509&subj=AAAS&numb=010')
html = str(response.read())
description = html.split('<p><p>')[1].split('</p')[0]
print(description)