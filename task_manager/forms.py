from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from task_manager.models import Position


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"
