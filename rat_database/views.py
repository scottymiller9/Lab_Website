from django.shortcuts import render


def home(request):
    return render(request, 'rat_database/action_choice.html')