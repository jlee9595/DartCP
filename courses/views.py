from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic
from .models import Course, Dept, Prof
from .forms import DeptFilterForm, SearchForm
# Create your views here.

def home(request):
	form = DeptFilterForm()
	return render(request, 'courses/home.html', {'form': form})

def search(request):
	if request.method == 'GET':
		form = SearchForm(request.GET)
		if form.is_valid():
			entry = form.cleaned_data['search']
			searchcourses = []
			for course in Course.objects.filter(name__contains=entry):
				searchcourses.append(course)
			for prof in Prof.objects.filter(fullname__contains=entry):
				for course in prof.course_set.all():
					searchcourses.append(course)
			return render(request, 'courses/search.html', {'entry': entry, 'searchcourses': searchcourses})


def filter_by_dept(request):
	if request.method == 'GET':
		form = DeptFilterForm(request.GET)
		if form.is_valid():
			filterdepts = form.cleaned_data['filterdepts']
			filteredcourses = []
			i=0
			while (i < len(filterdepts)):
				for course in Dept.objects.get(id=filterdepts[i]).course_set.all():
					filteredcourses.append(course)
				i += 1

			return render(request, 'courses/filtered.html', {'filteredcourses': filteredcourses})

def index(request):
	course_list = Course.objects.order_by('dept')

	template = loader.get_template('courses/index.html')
	context = RequestContext(request, {
		'course_list': course_list,
	})
	return HttpResponse(template.render(context))

def course_detail(request, course_id):
	try:
		course = Course.objects.get(pk=course_id)
	except Course.DoesNotExist:
		raise Http404("Course does not exist")

	# singleprof = Prof.objects.get(fullname=course.prof)
	return render(request, 'courses/course_detail.html', {'course': course})