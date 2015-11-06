# courseExtract.py: Automates process of adding courses from course catalog page to coursepicker databse
#
# Run this script from django shell by doing the following:
#
# python ../manage.py shell
# with open("courseExtract.py") as f:
# 	code = compile(f.read(), "courseExtract.py", 'exec')
# 	exec(code)

from courses.models import Course, Dept, Prof, Period, Term, Distrib, WC
from django.db import IntegrityError
import urllib.request

with open("15F.html") as fp:
	i = 1
	#Iterate through lines in the HTML file, knowing that each course's data is represented in blocks of 34 lines following a consistent pattern
	for line in fp:
		if i == 2:
			crn = line[4:-6]

		if i == 3:
			if len(line) == 14:
				dept = line[4:-6]
			elif len(line) == 13:
				dept = line[4:-6]
			else:
				dept = line.split('>')[2][1:-3]
			print(dept)

		if i == 4:
			num = line[4:-6]

		if i == 5:
			sec = line[4:-6]

		if i == 19:
			url = line.split('\'')[1]
			response = urllib.request.urlopen(url)
			html = str(response.read())
			if len(html.split('<p><p>')) > 1:
				descrpt = html.split('<p><p>')[1].split('</p')[0]
			else:
				descrpt = 'None'
			course = line.split('>')[2][:-3]

		if i == 24:
			per = line.split('>')[1][:-4]
			if per == "&nbsp;":
				per = "<"
			if "<" in per:
				per = "Course-Specific"
			print(per)

		if i == 25:
			rm = line[4:-6]
			if rm == "&nbsp;":
				rm = ""

		if i == 26:
			bldg = line[4:-6]
			if bldg == "&nbsp;":
				bldg = ""

		if i == 27:
			profs = line[4:-6]											#Take out html tags
			proflist = []
			if profs != "&nbsp;":										#Make sure there is a professor's name in the line
				#Split line by commas in case there are multiple professors for one course
				for prof in profs.split(', '):
					proflist.append(prof)
			else:
				profs = ""

		if i == 28:
			wc = line[4:-6]
			if wc == "&nbsp;":
				wc = ""

		if i == 29:
			dists = line[4:-6]
			distlist = []
			if dists != "&nbsp;":
				for dist in dists.split(' or '):
					distlist.append(dist)
			else:
				dists = ""


		if i == 30:
			lim = line[4:-6]
			if lim == "&nbsp;":
				lim = "-"

		if i == 31:
			enrl = line[4:-6]
			if enrl == "&nbsp;":
				enrl = "-"

			if wc == "":
				q = Course(name = course, number = num, section = sec, CRN = crn, room = rm, building = bldg, limit = lim, enrollment = enrl, dept = Dept.objects.get(abbrv=dept), period = Period.objects.get(name=per), term = Term.objects.get(abbrv="15F"), description = descrpt)
			else:
				q = Course(name = course, number = num, section = sec, CRN = crn, room = rm, building = bldg, limit = lim, enrollment = enrl, dept = Dept.objects.get(abbrv=dept), period = Period.objects.get(name=per), term = Term.objects.get(abbrv="15F"), description = descrpt, WC = WC.objects.get(abbrv=wc))
			
			try:
				q.save()
			except IntegrityError:
				pass

			q = Course.objects.get(CRN=crn)
			for prof in proflist:
				q.professors.add(Prof.objects.get(fullname=prof))

			for dist in distlist:
				q.distribs.add(Distrib.objects.get(abbrv=dist))
		i+=1
		#Reset line counter every 34 lines
		if i == 35:
			i = 1