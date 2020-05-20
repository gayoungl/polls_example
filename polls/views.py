from django.shortcuts import render
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list} # context는 키와 밸류값으로 이루어짐 ex) a ={'key(그냥 이름)' : value}
    print(latest_question_list)
    return render(request, 'polls/index.html', context) # render라는 함수를 통해 html템플릿을 열게끔 호출 & contxt를 같이 넘겨줌

def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
       selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(keyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question' : questino, 'error_message': "you didn't select a choice"})

    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
