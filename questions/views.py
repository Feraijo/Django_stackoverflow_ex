# pylint: disable=no-member
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Answer, Question


class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):        
        return Question.objects.filter(pub_date__lte=timezone
            .now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'questions/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class QuestionCreateView(generic.CreateView):
    model = Question
    fields = ('question_text', 'pub_date', )
    success_url = '/questions/'
    initial = {'pub_date':timezone.now()}         

class AnswerCreateView(generic.CreateView):
    model = Answer
    fields = ('answer_text',  )    
       
    def dispatch(self, request, *args, **kwargs):        
        self.question = get_object_or_404(Question, pk=kwargs['pk'])        
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse('questions:detail', kwargs={'pk':self.pk})

    def form_valid(self, form):
        form.instance.question = self.question        
        self.pk = self.question.pk
        return super().form_valid(form)        

class SearchView(generic.ListView):    
    context_object_name = 'results'
    template_name = 'questions/search.html'
    def get_queryset(self):    
        q = self.request.GET.get('query', '')
        qs = Question.objects.filter(question_text__icontains=q)
        ans = Answer.objects.filter(answer_text__icontains=q)
        res = {'Questions':qs, 'Answers':ans}
        return res