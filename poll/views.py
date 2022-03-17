from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
# import datetime
# Create your views here.
from .models import Question, Choices

"""
The views were initially written as function based views- but later updated to 
class based views.
"""


class IndexView(generic.ListView):
    template_name = "poll/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "poll/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


def index(request):
    # now = datetime.datetime.now()
    # local = now.astimezone()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)


def detail(request, question_id):
    """
    The objects.get and raise 404 can be clubbed together as django provides a
    shortcut for the operation.
    """
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    # the above is a shortcut....
    context = {'question': question}
    return render(request, 'poll/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
