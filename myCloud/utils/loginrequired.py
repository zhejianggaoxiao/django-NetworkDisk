"""
-------------------------------------------------
   File Name：     loginrequired
   Description :
   Author :       gaox
   date：          4/29/18
-------------------------------------------------
   Change Activity:
                   4/29/18:
-------------------------------------------------
"""
__author__ = 'gaox'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
