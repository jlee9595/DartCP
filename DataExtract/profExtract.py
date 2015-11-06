# profExtract.py: Automates process of adding professors from course catalog page to coursepicker databse
#
# Run this script from django shell by doing the following:
#
# python ../manage.py shell
# with open("profExtract.py") as f:
# 	code = compile(f.read(), "profExtract.py", 'exec')
# 	exec(code)

from courses.models import Prof
from django.db import IntegrityError

with open("15F.html") as fp:
	i = 1
	#Iterate through lines in the HTML file, knowing that each course's data is represented in blocks of 35 lines and every 28th line in each block contatin's the professor's name
	for line in fp:
		if i == 28:
			proflist = line[4:-6]											#Take out html tags
			if proflist != "&nbsp":										#Make sure there is a professor's name in the line

				#Split line by commas in case there are multiple professors for one course
				for prof in proflist.split(', '):

					#Add to database
					q = Prof(fullname = prof, first_name = prof.split(' ', 1)[0], last_name = prof.split(' ', 1)[1])
					try:
						q.save()
					#Keep going if an already existing prof is found
					except IntegrityError:
						pass
		i+=1
		#Reset line counter every 35 lines
		if i == 36:
			i = 1