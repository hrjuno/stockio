from django.shortcuts import render


def show_main(request):
    context = {
        'app_name': 'Stockio',
        'name': 'Harjuno Abdullah',
        'class' : 'PBP C'
    }

    return render(request, "main.html", context)