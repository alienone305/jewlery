from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from jewlery.models import JewleryModel

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home','accounts:wait','commonuser:signup','company:aboutus','company:faqs',
                'company:contactus','company:termsandconditions','jewlery:publiclist','accounts:login',]
    def location(self, item):
        return reverse(item)

class SnippetSitemap(Sitemap):
    def items(self):
        return JewleryModel.objects.all()
