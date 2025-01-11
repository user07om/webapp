from django.shortcuts import render
from django.views import View

import logging

logger = logging.getLogger(__name__)

# Create your views here.
class HelloUser(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        logger.info("initated the get reqeust!")
        context = {
            'name': 'john.diago',
            'email': 'johndiago7@gmail.com'
        return render(request, self.template_name, context)
