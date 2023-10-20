from django import formsfrom .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        fields = ('comment', 'rate')