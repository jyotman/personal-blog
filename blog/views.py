from django.shortcuts import render
from django.utils import timezone
from .models import Post, Parking, ProfileImage
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ProfileImageForm, ContactMe
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import FormView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.core.mail import send_mail


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@csrf_exempt
def parkingUpdate(request):
    if request.method == "POST":
        Slot = request.POST['id']
        Status = request.POST['status']
        #p = Parking(slot=int(Slot), status=Status)
        p = Parking.objects.get(pk=int(Slot))
        setattr(p, 'status', Status)
        p.save()
        return HttpResponse('Slot Success')
    else:
        return HttpResponse('Blank Page')

@csrf_exempt
def parkingAccess(request):
    querySet = Parking.objects.all()
    data = [{'slot':item.slot, 'status':item.status} for item in querySet]
    response = JsonResponse(data, safe=False)
    return HttpResponse(response)

def aboutme(request):
    return render(request, 'blog/resume.html')


class ProfileImageView(FormView):
    template_name = 'blog/profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id
        return HttpResponse("Request Succesful")

def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactMe(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['jyotman94@gmail.com']

            msg = 'Name : ' + name + '\n\nMobile : ' + str(mobile) + '\n\nEmail : ' + str(email) + '\n\nMessage :\n\n' + message 

            send_mail('New Hire Request', msg, 'jyotman94@gmail.com', recipients)

            # return HttpResponseRedirect('/thanks/')
            return HttpResponse('Successful Submission')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactMe()

    return render(request, 'blog/contact.html', {'form': form.as_p()})