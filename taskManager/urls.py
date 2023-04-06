#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
# INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

from django.conf.urls import include, url
from django.contrib import admin
from taskManager.views import index
from taskManager import taskManager_urls

urlpatterns = [
    url(r'^$',
        index,
        name='index'),
    url(r'^taskManager/',
        include(taskManager_urls,
                namespace="taskManager")),
    url(r'^admin/', admin.site.urls),
]
