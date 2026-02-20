
from django.urls import path

from demo_app.views import sql_injection_demo_view

urlpatterns = [
	path("", sql_injection_demo_view, name="sql_injection_demo"),
]
