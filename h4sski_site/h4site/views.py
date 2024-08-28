from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index'
    
    skills = [
        {
            'name': 'AutoCAD',
            'level': 5,
        },
        {
            'name': 'Excel',
            'level': 5,
        },
        {
            'name': 'MS Office',
            'level': 4,
        },
    ]
    
    cards = [
        {
            'img_link': 'https://creadis.com/wp-content/uploads/2023/04/0_logo_black.png',
            'company_name': 'Creadis Sp. z o. o.',
            'role': 'Senior Mechanical Engineer',
            'start_date': '2022 May',
            'end_date': 'Present',
            'duration': '2 yrs 4 mos',
            'description': 'Consultant for Haldor Topsoe A/S as Piping Engineer',
        },
        {
            'img_link': 'data:image/png;base64,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',
            'company_name': 'Vestas',
            'role': 'Team Lead, Tech Lead, Specialist',
            'start_date': '2018 December',
            'end_date': '2022 April',
            'duration': '3 yrs 5 mos',
            'description': "Consultant for Vestas as Engimeering Change Manager - Mechanical Team \n- reviewing ECR's, accept / reject / forward to other Team\n- communicating and consulting with many specialist teams to provide the best solution",
        },
    ]
    
    context = {
        'nickname': 'h4sski',
        'cards': cards,
        'skills': skills,
    }
    
    def get(self, request):
        return render(request, 'index.html', self.context)

class SubView(TemplateView):
    template_name = 'sub_view'
    cards = [
        {
            'img_link': 'data:image/png;base64,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',
            'company_name': 'Vestas',
            'role': 'Team Lead, Tech Lead, Specialist',
            'start_date': '2018 December',
            'end_date': '2022 April',
            'duration': '3 yrs 5 mos',
            'description': "Consultant for Vestas as Engimeering Change Manager - Mechanical Team \n- reviewing ECR's, accept / reject / forward to other Team\n- communicating and consulting with many specialist teams to provide the best solution",
        },
    ]
    
    context = {
        'nickname': 'sub_view',
        'cards': cards,
    }
    
    def get(self, request):
        
        return render(request, 'index.html', self.context)