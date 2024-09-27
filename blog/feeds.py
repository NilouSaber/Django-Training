from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import post
from django.utils.timezone import now
current_time = now()
class LatestEntriesFeed(Feed):
    title = "blog newest post"
    link = "/rss/feed"
    description = "my blog update"

    def items(self):
        return post.objects.filter(status=1, publishedDate__lte=current_time)

    def item_title(self, item):
        return item.title

    def item_content(self, item):
        return item.content[:100]
