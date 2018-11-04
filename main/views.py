from django.shortcuts import render

from main.models import Visits
from main.tasks import forty_print_task


def home(request):
    template_name = 'main/home.html'
    context = {}

    forty_print_task.delay()

    try:
        c = Visits.objects.get(pk=1)
    except Visits.DoesNotExist:
        c = Visits(count=0)

    c.count += 1
    c.save()

    context['count'] = c.count

    return render(request, template_name, context=context)
