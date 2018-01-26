from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

import todos.views

urlpatterns = [
    url(_(r'^$'),
        todos.views.TodoListSimpleListView.as_view(),
        name='list_todos'),
    url(_(r'^(?P<pk>\d+)/$'),
        todos.views.TodoListViewSet.as_view({
            "get": "retrieve",
            "patch": "partial_update",
            "delete": "destroy"
        }),
        name='todos'),
    url(_(r'^tasks/$'),
        todos.views.TaskCreateView.as_view(),
        name='task_create'),
    url(_(r'^tasks/(?P<pk>\d+)/$'),
        todos.views.TaskViewSet.as_view({
            "patch": "partial_update",
            "delete": "destroy"
        }),
        name='tasks'),
]