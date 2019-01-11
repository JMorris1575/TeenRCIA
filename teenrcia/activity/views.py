from django.shortcuts import render
from django.views import View


class WelcomeView(View):
    template_name = 'activity/welcome.html'

    def get(self, request):
        context = {}
        print("Do I get here?")
        return render(request, self.template_name, context)



