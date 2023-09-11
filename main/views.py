from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Kezia Lasma Angelica',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)