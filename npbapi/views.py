# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import json
from collections import OrderedDict
from npbapi.models import Scores, pastScore, Mail
from npbapi.forms import DateForm, MailForm


# top page
def index(request):
    d = {
        'ce_scores': Scores.objects.filter(league='Ce'),
        'pa_scores': Scores.objects.filter(league='Pa'),
        'form':DateForm()
    }
    return render(request, 'npbapi/index.html', d)

def api(request):
    return render(request, 'npbapi/api.html')

def render_json_response(request, data, status=None):
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type = 'application/json; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type = 'application/json; charset=UTF-8', status=status)
    return response

# 試合速報
def today(request):
    game = []
    for data in Scores.objects.all():
        data_dict = OrderedDict([
            ('inning', data.inning),
            ('home_team', data.home_score),
            ('home_score', data.home_score),
            ('visitor_team', data.visitor_team),
            ('visitor_score', data.visitor_score),
            ('start_at', data.start_at),
            ])
        game.append(data_dict)
    gamedata = OrderedDict([('game', game)])
    return render_json_response(request, gamedata)

# 試合結果
def feedjson(request, date_id):
    game = []
    for data in pastScore.objects.filter(date=date_id):
        data_dict = OrderedDict([
            ('date', data.date),
            ('home_team', data.home_team),
            ('home_score', data.home_score),
            ('visitor_team', data.visitor_team),
            ('visitor_score', data.visitor_score),
            ('start_at', data.start_at),
            ])
        game.append(data_dict)
    gamedata = OrderedDict([('game', game)])
    return render_json_response(request, gamedata)

def mail_form(request):
    formset = MailForm(request.POST)
    if request.method == 'POST':
        if formset.is_valid():
            formset.save()
            return redirect('about')
    return render(request, 'npbapi/about.html', {'formset': formset,})

# for cron
def update(request):
    return HttpResponse()
def refresh(request):
    return HttpResponse()
