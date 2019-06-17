from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,get_object_or_404
from .forms import QuestionAddForm
from .models import Info,Question
# Create your views here.

MAX_WRONG_COUNT = 15
MAX_RIGHT_COUNT = 2

def question_add(request):
    template='questions/add.html'

    form=QuestionAddForm(request.POST or None)

    if form.is_valid():
        question = form.save(commit=False)
        if Info.objects.filter(iteration_num=1).exists():
            pass
        else:
            Info.objects.create()

        info = get_object_or_404(Info, iteration_num=1)
        info.total_questions += 1
        info.save()
        question.save()
        return redirect('add')

    context={
            'title':'add',
            'form': form,
            }

    return render(request,template,context)

def sort():
    for wrong_count in reversed(range(0,MAX_WRONG_COUNT+1)):
        queryset = Question.objects.filter(wrong_count=wrong_count)
        for query in queryset:
            query.date_created=timezone.now()
            query.save()

def get_first_question():
    queryset = Question.objects.all()
    min_time = queryset.first().date_created
    for query in queryset:
        if query.date_created<min_time:
            min_time = query.date_created
    return Question.objects.get(date_created=min_time)

def get_correct_answer(answer_num,question):
    if answer_num == 'a':
        answer = question.opt_a
    elif answer_num == 'b':
        answer = questin.opt_b
    elif answer_num == 'c':
        answer = question.opt_c
    else:
        answer = question.opt_d
    return answer

def answer(request):
    template='questions/answer.html'
    
    info = get_object_or_404(Info, iteration_num=1)
    
    if info.last_answered == 0:
        question = get_first_question()
    else:
        last_answered = Question.objects.get(num=info.last_answered)
        try:
            question = last_answered.get_next_by_date_created()
        except ObjectDoesNotExist:
            info = get_object_or_404(Info, iteration_num=1)
            deleted = Question.objects.filter(right_count=MAX_RIGHT_COUNT).delete()
            info.total_questions -= deleted[0]
            info.last_answered = 0
            info.save()
            sort()
            return redirect('home')

    if request.method == 'POST':
        answered_num = request.POST['answer']
        answer_num = question.answer
        answer = get_correct_answer(answer_num,question)

        if answered_num == question.answer:
            question.right_count += 1
            question.total_right_count += 1
            question.save()
            messages.success(request,
                    "Congratulations, correct answer is {}: {}."
                    .format(answer_num,answer))
        else:
            question.wrong_count += 1
            question.total_wrong_count += 1
            question.save()
            messages.success(request,
                    "The correct answer was {}: {}. but you selected {}. Good luck for this one"
                    .format(answer_num,answer,answered_num))
        info.last_answered = question.num
        info.save()
        return redirect('home')

    context={
            'title':'answer',
            'question': question,
            }

    return render(request,template,context)
