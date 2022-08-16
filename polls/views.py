from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Question, Choice
from django.template import loader
from django.urls import reverse
from datetime import timezone
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list" : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("you are looking at question %s." % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #question = get_object_or_404(Question, pk=question_id)
    context ={
        'question' : question
    }
    return render (request, 'polls/details.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    #return HttpResponse("you're voting on question %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):

        # redisplay the question voting form
        return render(request, 'polls/details.html',{
            'question' : question,
            'error_message' : "you didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))