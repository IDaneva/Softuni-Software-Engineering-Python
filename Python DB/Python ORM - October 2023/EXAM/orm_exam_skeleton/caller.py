import os
import django
from django.db.models import Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):
    if search_name is not None and search_email is not None:
        authors = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email).order_by(
            "-full_name")
    elif search_name is not None:
        authors = Author.objects.filter(full_name__icontains=search_name).order_by("-full_name")
    elif search_email is not None:
        authors = Author.objects.filter(email__icontains=search_email).order_by("-full_name")
    else:
        return ""

    result = []

    for author in authors:
        result.append(f"Author: {author.full_name}, email: {author.email}, "
                      f"status: {'Banned' if author.is_banned == True else 'Not Banned'}")

    return "\n".join(result)


def get_top_publisher():
    author = Author.objects.all().annotate(article_count=Count("article")).order_by("-article_count", "email").first()
    if not author or author.article_count == 0:
        return ""
    return f"Top Author: {author.full_name} with {author.article_count} published articles."


def get_top_reviewer():
    author = Author.objects.all().annotate(review_count=Count("review")).order_by("-review_count", "email").first()
    if not author or author.review_count == 0:
        return ""
    return f"Top Reviewer: {author.full_name} with {author.review_count} published reviews."


def get_latest_article():
    # article = Article.objects.all().order_by("-published_on").first()
    # authors = []
    # # for author in article.authors.oder_by('full_name'):
    # #     authors.append(a.full_name)
    # # average_rating = article.aggregate(Avg())
    # reviews = Review.objects.filter(article=article)
    # print(article.authors.all())
    # print(reviews.aggregate(Avg("rating")))
    # print()
    # return article.review_set.all()

    latest_article = Article.objects.order_by('-published_on').first()

    if latest_article:
        authors_names = ', '.join(sorted(author.full_name for author in latest_article.authors.all()))

        num_reviews = Review.objects.filter(article=latest_article).count()

        avg_reviews_rating = Review.objects.filter(article=latest_article).aggregate(avg_rating=Avg('rating'))[
            'avg_rating']
        avg_reviews_rating = avg_reviews_rating if avg_reviews_rating is not None else 0.0

        return (f"The latest article is: {latest_article.title}. Authors: {authors_names}. Reviewed: {num_reviews} "
                f"times. Average Rating: {avg_reviews_rating:.2f}.")
    else:
        return ""


def get_top_rated_article():

    top_rated_article = (
        Review.objects
        .values('article__title')
        .annotate(avg_rating=Avg('rating'), num_reviews=Count('article'))
        .order_by('-avg_rating', 'article__title')
        .first()
    )

    if top_rated_article:
        article_title = top_rated_article['article__title']
        avg_rating = top_rated_article['avg_rating']
        num_reviews = top_rated_article['num_reviews']

        return (f"The top-rated article is: {article_title}, with an average rating of "
                f"{avg_rating:.2f}, reviewed {num_reviews} times.")
    else:
        return ""


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    try:
        author = Author.objects.get(email=email)
        num_reviews = Review.objects.filter(author=author).count()

        author.is_banned = True
        author.save()

        Review.objects.filter(author=author).delete()

        return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."

    except Author.DoesNotExist:
        return "No authors banned."
