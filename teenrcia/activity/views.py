from django.shortcuts import render, redirect
from django.views import View

import datetime

import utilities

from .models import Activity, Section, Item

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
    template_name = 'activity/section.html'

    def get(self, request, activity_index, section_index):
        activity = Activity.objects.get(index=activity_index)
        section = Section.objects.get(activity=activity, index=section_index)
        items = Item.objects.filter(section=section)
        context = {'activity': activity, 'section': section, 'items': items, 'user': request.user}
        return render(request, self.template_name, context)


class ItemCreateView(View):
    template_name = 'activity/item_create.html'

    def get(self, request, activity_index, section_index):
        activity = Activity.objects.get(index=activity_index)
        section = Section.objects.get(activity=activity, index=section_index)
        items = Item.objects.filter(section=section)
        context = {'activity':activity, 'section':section, 'items': items}
        return render(request, self.template_name, context)

    def post(self, request, activity_index, section_index):
        activity = Activity.objects.get(index=activity_index)
        section = Section.objects.get(activity=activity, index=section_index)
        items = Item.objects.filter(section=section)
        index = len(items) + 1
        new_item = Item(index=index, section=section, text=request.POST['item_text'], author=request.user)
        new_item.save()
        return redirect('activity:section', activity_index, section_index)