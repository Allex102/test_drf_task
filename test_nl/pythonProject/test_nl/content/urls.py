from django.urls import path

from .views import PageViewSet, PageDetailViewSet

app_name = "page"
urlpatterns = [
    path("page/", PageViewSet.as_view({"get": "list"}), name="page_list"),
    path(
        "page/<int:pk>/",
        PageDetailViewSet.as_view({"get": "retrieve"}),
        name="page_detail",
    ),
]
