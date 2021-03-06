from .models import Entry, Tag, Visit
from django.shortcuts import render, get_object_or_404
from .forms import ContactMe
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.utils import timezone


class BlogIndex(ListView):
	template_name = "blog/home.html"
	#paginate_by = 2

	def increment_count(self):
		try:
			visits = Visit.objects.get(name="Home", date=timezone.now())
			visits.totalCount += 1
			visits.dailyCount += 1
			visits.save()
		except Visit.DoesNotExist:
			visits = Visit.objects.filter(name="Home")
			if visits.exists():
				visits = visits.reverse()[0]
				visits.dailyCount = 1
				visits.totalCount += 1
				# to create a new visit object from an existing visit object
				visits.pk = None
			else:
				visits = Visit.objects.create(name='Home', post=False)
				visits.dailyCount = 1
				visits.totalCount += 1
			visits.save()

	def get_queryset(self):
		self.increment_count()
		return Entry.objects.all()

class BlogIndexTag(ListView):
	template_name = "blog/tag_list.html"

	def get_queryset(self):
		self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
		return Entry.objects.filter(tag=self.tag)

	def get_context_data(self, **kwargs):
		context = super(BlogIndexTag, self).get_context_data(**kwargs)
		context['slug_selected'] = self.tag
		return context

class BlogDetail(DetailView):
	model = Entry
	template_name = "blog/post.html"

	def increment_count(self, title):
		try:
			visits = Visit.objects.get(name=title, date=timezone.now())
			visits.totalCount += 1
			visits.dailyCount += 1
			visits.save()
		except Visit.DoesNotExist:
			visits = Visit.objects.filter(name=title)
			if visits.exists():
				visits = visits.reverse()[0]
				visits.dailyCount = 1
				visits.totalCount += 1
				# to create a new visit object
				visits.pk = None
			else:
				visits = Visit.objects.create(name=title, post=True)
				visits.dailyCount = 1
				visits.totalCount += 1
			visits.save()

	def get_object(self):
		entry = super(BlogDetail, self).get_object()
		self.increment_count(entry.title)
		return entry

def privacyPolicy(request):
	return render(request, 'blog/privacy.html')

def terms(request):
	return render(request, 'blog/terms.html')

def aboutme(request):
	return render(request, 'blog/resume.html')

def webmasterVerify(request):
	return render(request, 'blog/googlef70e42b57a682b5c.html')


def contact(request):
	if request.method == 'POST':
		print("HERE2")
		# create a form instance and populate it with data from the request:
		form = ContactMe(request.POST)
		# check whether it's valid:
		if form.is_valid():
			print("HERE3")
			name = form.cleaned_data['name']
			mobile = form.cleaned_data['mobile']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			recipients = ['jyotman94@gmail.com']

			msg = 'Name : ' + name + '\n\nMobile : ' + str(mobile) + '\n\nEmail : ' + str(email) + '\n\nMessage :\n\n' + message 

			send_mail('New Hire Request', msg, 'jyotman94@gmail.com', recipients)
			
			# return HttpResponse('Successful Submission')
			return HttpResponseRedirect('/?redirect=true')
		# else:
		# 	print("HERE4")
		# 	print(form.errors)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactMe()

	return render(request, 'blog/contact.html', {'form': form})