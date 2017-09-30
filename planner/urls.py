from django.conf.urls import url

from . import views

app_name = 'planner'


'''
This project has just one app, planner. In real Django projects, there might be five, ten, twenty apps or more. 
How does Django differentiate the URL names between them? For example, the planner app has a detail view, and so might an app on the same 
project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?
(in index.html)
so we add an app_name variable as above and use 'planner:detail' in the link to specify which app's detail is being referred to
'''
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
