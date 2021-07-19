from django.db.models import fields
from django.forms import ModelForm, widgets
from knowledge_base.models import *
from django import forms

class FormKnowledgeBase(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
		#exclude = ['slug',]
