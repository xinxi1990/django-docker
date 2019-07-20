#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from servers.android_server import AnroidServer
from django.views.decorators.csrf import csrf_exempt

# from .models import Choice, Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    print context
    for a in latest_poll_list:
        print a.id
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

@csrf_exempt
def android_add(request):
    print("------- android_add --------")
    parames = eval(request.body)
    print(parames)
    resp = AnroidServer().add_android(parames)
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def android_update(request):
    print("------- android_update --------")
    parames = eval(request.body)
    print(parames)
    resp = AnroidServer().update_android(parames)
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def android_del(request):
    print("------- android_del --------")
    parames = eval(request.body)
    print(parames)
    resp = AnroidServer().del_android(parames)
    return HttpResponse(json.dumps(resp), content_type="application/json")
