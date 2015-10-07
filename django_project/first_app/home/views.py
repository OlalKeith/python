from django.shortcuts import render
from .forms import StudentForm
from .forms import FeedbackForm

# Create your views here.
def index(request):
	form = StudentForm(request.POST or None)

	context = {
		"hello_message": "Register new Student",
		"form":form
	}

	
	if form. is_valid():

		instance=form.save(commit=False)
		full_name = form.cleaned_data.get('full_name')
		if full_name == "Olal":
			full_name = "Developer"
		instance.full_name = full_name
		instance.save()

		context = {
		"hello_message":"Student Saved"
		}

	return render(request,'index.html', context)

def feedback(request):
	return render(request,'feedback.html',context)

