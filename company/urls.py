from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from company.views import (ContactUsView, AboutUsView, ContactUsListView,
                            ContactUsDeleteView, FAQsView, TermandConditionsView)
from company.sitemaps import StaticViewSitemap, SnippetSitemap

app_name ='company'
sitemaps = {
    'static': StaticViewSitemap,'jewlery': SnippetSitemap
}
urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('about-us/',AboutUsView, name = 'aboutus'),
    path('faqs/', FAQsView, name = 'faqs'),
    path('terms-and-conditions/',TermandConditionsView, name = 'termsandconditions'),
    path('contact-us/',ContactUsView, name = 'contactus'),
    path('contact-us-list/',ContactUsListView, name = 'contactuslist'),
    path('contact-us-delete/<int:pk>',ContactUsDeleteView, name = 'contact-us-delete'),

]
