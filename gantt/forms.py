from django import forms
 
class AddForm(forms.Form):
    character_id_1 = forms.IntegerField()
    character_id_2 = forms.IntegerField()
    character_id_3 = forms.IntegerField()
    character_id_4 = forms.IntegerField()
    character_id_5 = forms.IntegerField()