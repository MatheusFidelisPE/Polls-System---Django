from django.http import HttpResponse

# Os métodos nesse arquivo views.py que são invocados no arquivo polls/urls.py precisam ter como primeiro argumento
# um argumento chamado request


def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")


def detail(request, question_id):
    return HttpResponse("Você está procurando pela questão %s" % question_id)


def results(request, question_id):
    response = "Você está procurando pelos resultados da questão %s"
    return HttpResponse(response%question_id)


def vote(request, question_id):
    return HttpResponse("Você estará vontando na questão %s" % question_id)


