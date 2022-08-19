from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewQuestion
from .models import Question
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

def base(response, **kwargs):
    return render(response, 'main/base.html', {})


def home(response, **kwargs):
    return render(response, 'main/home.html', {})


def question(response, **kwargs):
    if response.method == "POST":
        form = CreateNewQuestion(response.POST)
        if form.is_valid():
            n = form.cleaned_data["question"]
            if len(n) > 5:
                q = Question(name=n)
                if len(response.user.question_search.all()) <= 6:
                    q.save()
                    response.user.question_search.add(q)

        return HttpResponseRedirect("../show_questions/")
    else:
        form = CreateNewQuestion()

    return render(response, 'main/question.html', {"form": form})


def show_questions(response, **kwargs):
    question_list = Question.objects.all()

    return render(response, 'main/show_questions.html', {'question_list': question_list})


def delete(response, id):

    question_id = Question.objects.get(id=id)
    question_id.delete()

    return render(response, 'main/delete.html', {'id': id})

## try to access the form with ['questionTwo'] ::D:D:D:D:

def edit(response, id):
    question_id = Question.objects.get(id=id)
    form = CreateNewQuestion(response.POST or None, instance=question_id)
    # form['questionTwo'].value = 'ey'
    if form.is_valid():
        form.save()
        return redirect('show_questions')

    return render(response, 'main/edit.html', {'question_id': question_id, 'form': form})
