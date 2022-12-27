from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('newpoll/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'newpoll/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    response = "You're looking at the results of question %s."
    return render(request, 'newpoll/results.html', {'question': response%question})
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    response = "You're voting on question %s."
    return render(request, 'newpoll/vote.html', {'question': response%question})
# Create your views here.
