from django.conf.urls import url

from jobs.views import *



urlpatterns = [

    # Need to allow access the user (and profile) edit page, via a common non account specific url
    url(r'^$', JobForm.as_view(), name='job_form'),
    url(r'^tests/(?P<job_id>\d)$', test_form, name='test_form'),

]
