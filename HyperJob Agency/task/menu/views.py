from django.views import View
from django.shortcuts import render

# Create your views here.

AVAILABLE_PAGES = {
    'Login page': "/login",
    'Logout page': "/logout",
    'Sign up page': "/signup",
    'Vacancy list': "/vacancies",
    'Resume list': "/resumes",
    'Personal profile': "/home"
}


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/index.html', context={'links': AVAILABLE_PAGES})