from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import F

from .models import Choice, Question

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
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html',
				  {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		choice_id = request.POST['choice']
		selected_choice = question.choice_set.get(pk=choice_id)
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/details.html',
					  {'question': question,
					   'error_message': "No choice has been selected yet"})
	else:
		selected_choice.vote_tally = F('vote_tally') + 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',
					  args=(question_id,)))


