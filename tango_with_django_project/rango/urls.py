from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)


#urlpatterns = patterns('',
#                       url(r'^$', views.index, name='index'),
#                       url(r'^about/$', views.about, name='about'),
#                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'), # New!
#                        )

# For section 4.7 Exercise
# Creating an about page with a link back to the main index page
#urlpatterns = patterns('',
#                       url(r'^$', views.index, name='index'),
#                       url(r'^about/', views.about, name='about')
#                        )
