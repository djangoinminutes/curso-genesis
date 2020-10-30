
from django.urls import path, include
from core.views import CorePageView

#@[p_core_urls_01]

core_patterns = ([
	path('',CorePageView.as_view(),name='home'),
#@[p_core_urls_02]
],'core')

#@[p_core_urls_03]


