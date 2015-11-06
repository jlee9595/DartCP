# DartCP
Running at 'http://jlee9595.pythonanywhere.com/'

To run locally, run 'python manage.py runserver'

This is an individual project that aims to eventually reach a point where the information for all Dartmouth classes would be much less of a pain to access than through the clunky website provided by the college.

Currently the site holds all the data necessary to make this happen.

Next steps: add increased filtering capabilities

To see the python scripts that pull data from 'http://oracle-www.dartmouth.edu/dart/groucho/timetable.main', check out DataExtract/. This contains the html source code for the pages on Dartmouth's site and the scripts that I used to parse them

Most of the meat of the website is located in courses/