from django.shortcuts import render,get_object_or_404
from djangotask.forms import UserForm, UserProfileForm
from django.http import HttpResponse,HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile,User
# Create your views here.


def home(request):
    #print request.user.is_authenticated()
    if request.user.is_authenticated():
        obj = get_object_or_404(UserProfile,user=request.user)
        #print obj
        context = {
            'obj':obj
        }
        return render(request,'index.html',context)
    else:
	   return render(request,'index.html',{})

def register(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    if registered:
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")


    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)



def user_login(request):
    context = RequestContext(request)
    print request.user.is_authenticated()
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        print 'yo'
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', {}, context)



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def autocomplete(request):
    if request.method=='GET':
        uname = request.GET['uname']
        user = User.objects.filter(username=uname)
        if user:
            data = "True"
        else:
            data ="False"
    else:
        return HttpResponse('fail')
    return HttpResponse(data)