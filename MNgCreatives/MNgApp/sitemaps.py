# sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return [
            "index",
            "portfolio",
            "services",
            "about",
            "resume",
            "contact",
            "testimonials",
        ]

    def location(self, item):
        return reverse(item)
