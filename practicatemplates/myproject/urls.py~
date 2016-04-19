from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^annotated/lista/', 'cms.views.listadoplantilla'),
    url(r'^annotated/(\d+)','cms.views.paginaplantilla'),
    url(r'^annotated/?(.*)', 'cms.views.indexplantilla'),
    url(r'^accounts/profile/$', 'cms.views.usuario'),
    url(r'^lista/', 'cms.views.listado'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'(\d+)','cms.views.pagina'),
    url(r'/?(.*)', 'cms.views.index'),
)
