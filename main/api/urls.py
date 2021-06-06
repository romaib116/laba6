from django.urls import path, re_path

from django.conf.urls import url
from .api_views import AstroRegisterAPIView, tutorial_detail , tutorial_list, AstroRegisterDetail, AstroRegisterList


urlpatterns=[
    path('astroregisters/', AstroRegisterList.as_view()),
    path('astroregisters/<int:pk>/', AstroRegisterDetail.as_view()),
]
