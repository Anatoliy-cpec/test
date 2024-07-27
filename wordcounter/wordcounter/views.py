from django.views.generic.edit import FormMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.encoding import smart_str

from .forms import FileForm

from .models import CounterFile

from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, View, TemplateView
)

class CountView(TemplateView, FormMixin):
    template_name = 'counter.html'
    form_class = FileForm
    success_url = '/counter'

    def get(self, request: HttpRequest, *args: reverse_lazy, **kwargs: reverse_lazy) -> HttpResponse:
        if request.session.session_key is None:
            request.session.save()


        
        return super().get(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
                
    def form_valid(self, form) -> HttpResponse:
        self.form = form.save(commit=False)
        request = self.request

        if CounterFile.objects.filter(session_id=request.session.session_key):
            
            session = CounterFile.objects.get(session_id=request.session.session_key)
            if request.FILES['file'].content_type.split('/')[0] == 'text':
                session.add_file(request.FILES['file'])

        else:
            if request.FILES['file'].content_type.split('/')[0] == 'text':
                CounterFile.create_counter_file(request.session.session_key, request.FILES['file'])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CountView, self).get_context_data(**kwargs)
        try:
            my_session = CounterFile.objects.get(session_id=self.request.session.session_key)
            context.update({'my_session': my_session})

            search_word = self.request.GET['search']

            if search_word == '':
                return context
            else:
                context.update({'search_word': search_word})

                file = my_session.file
                file_text = my_session.get_text_from_file().lower().split(' ')

                __counter = 0
                for word in file_text:
                    if search_word.lower() == word:
                        __counter += 1

                context.update({'search_word_count': __counter})

            return context
        except:
            return context
        

def clear(request):
    my_session = CounterFile.objects.get(session_id=request.session.session_key)
    
    my_session.file.delete()
    my_session.delete()

    return HttpResponseRedirect(reverse('counter'))
        
        


    
