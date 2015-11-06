from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^search/$', views.search, name='search'),
	url(r'^courses/filtered/$', views.filter_by_dept, name='filtered'),
	#ex: /courses/
	url(r'^courses/$', views.index, name='index'),
	#ex: /courses/5/
	url(r'^courses/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),

	# url(r'^depts/(?P<dept_id>[0-9]+)/$', views.dept_detail, name='dept_detail'),
	]