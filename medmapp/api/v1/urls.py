from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('bosh-sahifa/', include('bosh_sahifa.urls')),
    path('narxlar/', include('narxlar.urls')),
    path('sharhlar/', include('sharhlar.urls')),
    path('shifoxonalar/', include('shifoxonalar.urls')),
    path('xizmatlar/', include('xizmatlar.urls')),
    path('shifokorlar/', include('shifokorlar.urls')),
]
