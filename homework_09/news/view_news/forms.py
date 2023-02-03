from django import forms
from .models import Posts, Req_Urls


class PostForm(forms.ModelForm):
    from_url = forms.ModelChoiceField(label='url', queryset=Req_Urls.objects.all())

    class Meta:
        model = Posts
        fields = ('title', 'text', 'url', 'from_url')

    #def __init__(self, *args, **kwargs):
        #user = kwargs.pop('user')
        #super(FolderForm, self).__init__(*args, **kwargs)
    #    self.fields['from_url'].queryset = Req_Urls.objects.filter()#user=user)
