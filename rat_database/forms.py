from django import forms


class AddRat(forms.Form):
    new_rat_name=forms.CharField(label='Rat Name', max_length=10, required=True)
    new_rat_age=forms.IntegerField(max_value=100, min_value=0)

class InitialAction(forms.Form):
    CHOICES= (
        ('a','choice 1'),
        ('b','choice 2'),

    )

    option_selected=forms.MultipleChoiceField(choices=CHOICES,widget=forms.Select())