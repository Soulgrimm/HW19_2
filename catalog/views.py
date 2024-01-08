from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from catalog.models import Product, Blog
from pytils.translit import slugify


# def index(request):
#     products_list = Product.objects.all()
#     content = {
#         'object_list': products_list
#     }
#     return render(request, 'main/index.html', content)

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'publication_sign')

    # success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('slug')])


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:list')


class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'


# def contacts(request):
#     return render(request, 'catalog/contacts.html')
