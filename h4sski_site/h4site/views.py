from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index'
    
    skills = [
        {
        'name': 'Hard skills',
        'skills_list': [
                {
                    'level': 5,
                    'name': ['Excel', 'AutoCAD'],
                },
                {
                    'level': 4,
                    'name': ['Kanban', 'Jira', 'MS Teams', 'AutoCAD Plant 3D', 'Navisworks', 'SAP REP', 'MS Office', 'MS PowerPoint', 'MS OneNote'],
                },
                {
                    'level': 3,
                    'name': ['Python', 'Git', 'Linux', 'SQL', 'HTML', 'CSS', 'Solidworks', 'Windchill'],
                },
                {
                    'level': 2,
                    'name': ['Django', 'Flask', 'PyGame', 'Java'],
                },
                {
                    'level': 1,
                    'name': ['C++'],
                },
            ],
        },
        {
        'name': 'Soft skills',
        'skills_list': [
                {
                    'level': 4,
                    'name': ['Problem solving', 'Change Management'],
                },
                {
                    'level': 3,
                    'name': ['Scrum', 'Vendor Management'],
                },
            ],
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
        'max_stars': [1, 2, 3, 4, 5],
    }
    
    def get(self, request):
        return render(request, 'index.html', self.context)
    
    
    
    
class Index2View(TemplateView):
    template_name = 'index2'
    
    skills = [
        {
        'name': 'Hard skills',
        'skills_list': [
                {
                    'level': 5,
                    'name': ['Excel', 'AutoCAD'],
                },
                {
                    'level': 4,
                    'name': ['Kanban', 'Jira', 'MS Teams', 'AutoCAD Plant 3D', 'Navisworks', 'SAP REP', 'MS Office', 'MS PowerPoint', 'MS OneNote'],
                },
                {
                    'level': 3,
                    'name': ['Python', 'Git', 'Linux', 'SQL', 'HTML', 'CSS', 'Solidworks', 'Windchill'],
                },
                {
                    'level': 2,
                    'name': ['Django', 'Flask', 'PyGame', 'Java'],
                },
                {
                    'level': 1,
                    'name': ['C++', 'Docker'],
                },
            ],
        },
        {
        'name': 'Soft skills',
        'skills_list': [
                {
                    'level': 5,
                    'name': ['Problem solving'],
                },
                {
                    'level': 4,
                    'name': ['Change Management'],
                },
                {
                    'level': 3,
                    'name': ['Scrum', 'Vendor Management'],
                },
            ],
        },
    ]
    
    delivery_scope = [
        {
            'title': 'Python development',
            'description': 'Thanks to my consistency of getting more skills and more knowledge...'
        },
        {
            'title': 'Mechanical engineering',
            'description': 'Thanks to my background, knowledge and gain experience...'
        },
        {
            'title': 'Furniture design',
            'description': 'Thanks to many projects finished during my work for Smeulders Polska...'
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
            'company_name': 'Haldor Topsoe A/S',
            'role': 'Cad Designer, Piping Engineer, Mechanical Engineer, Specialist',
            'start_date': '2023 September',
            'end_date': '2024 July',
            'duration': '11 mos',
            'description': "The project was about complete plant factory design. The consultant was responsible for the piping design together with the Team. Responsible for keeping constant contact with other Team Members and other discipline stakeholders. Managing the changes in the model and updating it.\n\nSkills\n- Piping designing with the use of Plant3D\n- Multi-discipline coordination\n- Layout constant check of possible issues during design with the use of Navisworks\n- Layout drawings",
        },
        {
            'img_link': 'data:image/png;base64,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',
            'company_name': 'Vestas',
            'role': 'Team Lead, Tech Lead, Specialist',
            'start_date': '2018 December',
            'end_date': '2022 April',
            'duration': '3 yrs 5 mos',
            'description': "The scope of the project was to resolve ECR’s (Engineering Change Requests) in the way to continue the correct working of the WTG (Wind Turbine Generator). Cases were raised due to many reasons, like obsolete items, health or safety reasons, and technical documentation changes. Since tasks vary from each, every issue had to be resolved in a different, new way than the resolved ones. Actions needed to perform the investigation included contacting suppliers, contacting specialists within the company to discuss issues and potential impacts, CAD cross-checking if the new solution is possible to perform, preparing outcome documentation which allows the implementation change in the numbers of systems, partially implementing the change at some of the systems, and verifying if change resolves the problem.\n\nSkills:\n- Analytical thinking and resolving problems.\n- Communication inside and outside of the company.\n- 3D model analysis.\n- Work with technical documentation, including updating existing ones.\n- Getting knowledge and experience about many systems.",
        },
    ]
    
    context = {
        'nickname': 'h4sski',
        'cards': cards,
        'skills': skills,
        'delivery_scope': delivery_scope,
        'max_stars': [1, 2, 3, 4, 5],
    }
    
    def get(self, request):
        return render(request, 'index2.html', self.context)

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