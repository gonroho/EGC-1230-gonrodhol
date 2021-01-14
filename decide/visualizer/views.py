import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from voting.models import Voting
from django.db import models


from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        return context

class ContactUs(TemplateView):
    try:
        template_name = 'visualizer/contactUs.html'
    except:
        raise Http404

class AboutUs(TemplateView):
    try:
        template_name = 'visualizer/aboutUs.html'
    except:
        raise Http404

class VisualizerHome(TemplateView):    
    queryset= Voting.objects.all()
    template_name = 'visualizer/visualizer_home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        votings = Voting.objects.all()
        context.update({'votings': votings})
        return context

    
    