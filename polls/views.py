from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

# Create your views here.
def index(request):
	latest_question_list = \
		Question.objects.order_by('-pub_date')[:5]
	return render(request, 'polls/index.html', 
				  {'latest_question_list' : latest_question_list})

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html',
				  {'question': question})

def results(request, question_id):
	return render(request, 'polls/results.html',
				  {'question_id': question_id})

def vote(request, question_id):
	return render(request, 'polls/vote.html',
				  {'question_id': question_id})


