from django.views.generic import ListView
from django.db.models import Q
from .models import Dish


class IndexView(ListView):
    template_name = "foodprod/index.html"
    model = Dish

    def get_queryset(self):
        search_query = self.request.GET.get('search_query')
        if search_query:
            object_list = self.model.objects.filter(Q(name__icontains=search_query) |
                                                    Q(description__icontains=search_query))
        else:
            object_list = self.model.objects.all()
        return object_list
