# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.forms import modelformset_factory

from django.views.generic import FormView
from .forms import *
from .models import *

class JobForm(FormView):
    template_name = 'jobs/job_form.html'
    form_class = JobFormSet
    success_url = reverse_lazy('job_form') 

    def form_valid(self, formset):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        for form in formset:
            form.save()
        return super(JobForm, self).form_valid(formset)


def test_form(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {
        'job_id': job_id,
        'job': job,
        'formset': TestRecordFormSet(instance=job, queryset=TestRecord.objects.filter(job_id=job_id)),
        }

    if request.method == "POST":
        print 'Here', request.POST
        formset = TestRecordFormSet(request.POST, instance=job, queryset=TestRecord.objects.filter(job_id=job_id))
        for form in formset:
            print 'is valid?', form.is_valid()
            print 'where', form.cleaned_data.get('where', False)
            if form in formset.deleted_forms:
                to_delete = form.instance
                TestRecord.objects.get(id=to_delete.id).delete()
                print 'Deleted'
            elif form.is_valid() and form.cleaned_data.get('where', False):
                test_record = form.save(commit=False)
                test_record.job = job
                test_record.save()
                print 'Saved'
        context['form'] = formset
    return render(request, 'jobs/test_form.html', context)
