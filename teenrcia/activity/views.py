from django.shortcuts import render, redirect
from django.views import View

import datetime

import utilities

from .models import Activity, Section, Item, Comment

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


class ItemEditView(View):
    template_name = 'activity/item_edit.html'

    def get(self, request, activity_index, item_pk):
        activity = Activity.objects.get(index=activity_index)
        item = Item.objects.get(pk=item_pk)
        comments = Comment.objects.filter(item=item)
        error_msg = ''
        if len(comments) > 0:
            error_msg = 'People have made comments on this item. You may want to be careful about editing it.'
        context = {'activity': activity, 'item': item, 'comments': comments, 'error': error_msg}
        return render(request, self.template_name, context)

    def post(self, request, activity_index, item_pk):
        activity = Activity.objects.get(index=activity_index)
        item = Item.objects.get(pk=item_pk)
        item.text = request.POST['item_text']
        item.save()
        return redirect('activity:section', activity_index, item.section.index)


class CommentCreateView(View):
    template_name = 'activity/comment_create.html'

    def get(self, request, activity_index, item_pk):
        activity = Activity.objects.get(index=activity_index)
        item = Item.objects.get(pk=item_pk)
        comments = Comment.objects.filter(item=item)
        context = {'activity': activity, 'item': item, 'comments': comments}
        return render(request, self.template_name, context)

    def post(self, request, activity_index, item_pk):
        activity = Activity.objects.get(index=activity_index)
        item = Item.objects.get(pk=item_pk)
        new_comment = Comment(user=request.user, item=item, text=request.POST['comment_text'])
        new_comment.save()
        return redirect('activity:section', activity_index, item.section.index)
