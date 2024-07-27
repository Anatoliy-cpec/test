from typing import Any
from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.utils.encoding import smart_str

class CounterFile(models.Model):
    session_id = models.TextField(blank=True, null=True, max_length=400)
    file = models.FileField(verbose_name='Файл', blank=True, null=True, upload_to='files/%Y/%m/%d/')

    @staticmethod
    def create_counter_file(session_id, file):
        _obj = CounterFile.objects.create()
        _obj.session_id = session_id
        _obj.add_file(file)
        _obj.save()


    def add_file(self, file):
        self.file = file
        self.save()

    def delete_file(self):
        self.file.delete()
        self.save()

    def get_text_from_file(self):
        print("get_text_from_file")
        return self.file.open('r').read()
    
    def set_session_id(self, session_id):
        self.session_id = session_id
        self.save()

    def __str__(self) -> str:
        return self.session_id