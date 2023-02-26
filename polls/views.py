from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question


# Os métodos nesse arquivo views.py que são invocados no arquivo polls/urls.py precisam ter como primeiro argumento
# um argumento chamado request


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Does Not Exist")
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question':question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "Você está procurando pelos resultados da questão %s"
    return HttpResponse(response%question_id)


def vote(request, question_id):
    return HttpResponse("Você estará vontando na questão %s" % question_id)


