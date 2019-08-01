from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,get_object_or_404
from .forms import QuestionAddForm
from .models import Info,Question
# Create your views here.

MAX_WRONG_COUNT = 15
MAX_RIGHT_COUNT = 2
MAX_ITERATIONS = 15

def question_add(request):
    template='questions/add.html'

    form=QuestionAddForm(request.POST or None)
    if Info.objects.filter(identifier=1).exists():
        pass
    else:
        Info.objects.create()

    info = get_object_or_404(Info, identifier=1)

    if form.is_valid():
        question = form.save(commit=False)
        question.question_num=info.total_questions+1
        question.save()
        info.total_questions = question.question_num
        category_total_questions = getattr(info, "total_questions_"+question.category)
        category_total_questions += 1
        setattr(info, "total_questions_"+question.category, category_total_questions)
        info.save()
        return redirect('add')

    context={
            'title':'add',
            'form': form,
            'info': info
            }

    return render(request,template,context)

def sort(category):
    for wrong_count in reversed(range(0,MAX_WRONG_COUNT+1)):
        queryset = Question.objects.filter(category=category,wrong_count=wrong_count).order_by("question_num")
        for query in queryset:
            query.date_created=timezone.now()
            query.save()

def get_first_question(category):
    queryset = Question.objects.filter(category=category)
    min_time = queryset.first().date_created
    for query in queryset:
        if query.date_created<min_time:
            min_time = query.date_created
    return Question.objects.get(date_created=min_time)

def get_correct_answer(answer_num,question):
    if answer_num == 'a':
        answer = question.opt_a
    elif answer_num == 'b':
        answer = question.opt_b
    elif answer_num == 'c':
        answer = question.opt_c
    elif answer_num == 'd':
        answer = question.opt_d
    elif answer_num == 'e':
        answer = question.opt_e
    elif answer_num == 'f':
        answer = question.opt_f
    else:
        answer = "<< You entered option that was out of scope!!!"
    return answer

def answer(request):
    template='questions/answer.html'
    
    info = get_object_or_404(Info, identifier=1)
    category = request.path_info.replace("/","").replace("answer","")
    if category == "":
        category = "computer_misc"
    
    if getattr(info, "last_answered_"+category) == 0:
        question = get_first_question(category)
        old_question = None
    else:
        category_last_answered_question_num = getattr(info, "last_answered_"+category)
        last_answered = Question.objects.get(question_num=category_last_answered_question_num, category=category)
        if getattr(info, "iteration_num_"+category) == MAX_ITERATIONS:
            messages.warning(request,
                    "You have done max iterations of this question set, please update max_iterations if you want to keep going.")
            return redirect("about")
        try:
            question = last_answered.get_next_by_date_created(category=category)
        except ObjectDoesNotExist:
            deleted = Question.objects.filter(category=category, right_count=MAX_RIGHT_COUNT).delete()
            deleted_2 = Question.objects.filter(category=category, total_right_count=3).delete()
            sort(category)
            info.total_questions -= deleted[0]
            info.total_questions -= deleted_2[0]
            category_total_questions = getattr(info, "total_questions_"+category)
            category_total_questions -= deleted[0]
            category_total_questions -= deleted_2[0]
            setattr(info, "total_questions_"+category, category_total_questions)
            setattr(info, "last_answered_"+category, 0)
            category_iteration_num = getattr(info, "iteration_num_"+category)
            category_iteration_num += 1
            setattr(info,"iteration_num_"+category, category_iteration_num)
            info.save()
            return redirect(category)
    category_total_questions = getattr(info,"total_questions_"+category)
    
    if 'last_answered' in locals():
        old_question = last_answered

    if request.method == 'POST':
        answered_num = request.POST['answer']
        answer_num = question.answer
        answer = get_correct_answer(answer_num,question)

        if answered_num == question.answer:
            question.right_count += 1
            question.total_right_count += 1
            messages.success(request,
                    "Congratulations, correct answer is {}: {}."
                    .format(answer_num,answer))
        else:
            question.wrong_count += 1
            question.total_wrong_count += 1
            question.right_count = 0
            messages.warning(request,
                    "The correct answer was {}: {}. but you selected {}. Good luck for this one."
                    .format(answer_num,answer,answered_num))
        question.save()
        setattr(info,"last_answered_"+category, question.question_num)
        info.save()
        return redirect(category)

    context={
            'title':'answer',
            'question': question,
            'old_question': old_question,
            'info': info,
            'category_total_questions':category_total_questions,
            }

    return render(request,template,context)
