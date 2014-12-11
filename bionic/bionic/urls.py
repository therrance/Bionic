from django.conf.urls import patterns, include, url
from django.contrib import admin
import coursera.views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bionic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',coursera.views.ListStudentView.as_view(),
        name='student-list')
)
