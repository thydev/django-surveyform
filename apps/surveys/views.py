from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        'greeting': 'Hi from Django'
    }
    return render(request,"surveys/index.html", context)

def surveys_process(request):
    if request.method == "POST":
        if 'num_submit' in request.session:
            request.session['num_submit'] += 1
        else:
            request.session['num_submit'] = 1
        request.session['survey'] = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comment': request.POST['comment']
        }
        
        return redirect('/surveys/result')

    return redirect('/')

def result(request):

    return render(request, "surveys/result.html")