from django.http import JsonResponse
from django.shortcuts import render
from django.views import View, generic
from .models import Category, Article, Post, Posts


def index(request):
    rows = Category.objects.order_by("order")
    context = {"rows": rows}
    return render(request, "portfolio/portfolio.html", context)


def fappy_borbs(request):
    return render(request, "portfolio/fappy_borbs/fappy_borbs.html")


class page(generic.DetailView):
    model = Article
    template_name = "portfolio/page.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return context


def safe_get(dict_obj, *keys):
    for key in keys:
        if not isinstance(dict_obj, dict):
            return None
        dict_obj = dict_obj.get(key)
    return dict_obj


class init(View):
    def get(request, *args, **kwargs):
        Post.objects.all().delete()
        posts = Posts.objects.first()
        db = posts.db
        for post in db:
            properties = post.get("properties", {})
            name = properties.get("Name").get("title")[0].get("plain_text")
            slug = safe_get(properties, "Slug", "rich_text")
            if slug:
                slug = slug[0].get("plain_text")
            else:
                slug = name.strip().lower().replace(" ", "-")
            cover = post.get("cover", {})
            cover = safe_get(cover, "file", "url") or safe_get(cover, "external", "url")
            published = safe_get(properties, "Published", "date", "start")
            public = safe_get(properties, "Public", "checkbox")
            featured = safe_get(properties, "Featured", "checkbox")
            school = safe_get(properties, "School Project", "checkbox")
            work = safe_get(properties, "Work", "checkbox")
            pet = safe_get(properties, "Pet Project", "checkbox")
            blog = safe_get(properties, "Blog", "checkbox")
            Post.objects.create(
                name=name,
                slug=slug,
                cover=cover,
                published=published,
                public=public,
                featured=featured,
                school=school,
                work=work,
                pet=pet,
                blog=blog,
            )
        # Posts.objects.all().delete()
        return JsonResponse({"status": "success"})
