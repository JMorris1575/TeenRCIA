from django.shortcuts import render
from django.views import View

import datetime

import utilities

from .models import Activity, Section

class WelcomeView(View):
    template_name = 'activity/welcome.html'

    def get(self, request):
        activities = Activity.objects.filter(publish_date__lte=datetime.date.today(), archive=False)
        context = {'activities': activities, 'image': utilities.get_quote_image()}
        return render(request, self.template_name, context)


class SummaryView(View):
    template_name = 'activity/summary.html'

    def get(self, request, activity_index):
        activity = Activity.objects.get(index=activity_index)
        sections = Section.objects.filter(activity=activity, visible=True)
        context = {'activity': activity, 'sections': sections}
        return render(request, self.template_name, context)


class SectionView(View):
    pass