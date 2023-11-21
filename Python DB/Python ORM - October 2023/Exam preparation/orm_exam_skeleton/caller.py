import os
import django
from django.db.models import Count, Avg, Max, F
from django.db import models


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    # Check if both values are not None
    if search_name is not None and search_nationality is not None:
        directors = Director.objects.filter(
            full_name__icontains=search_name,
            nationality__icontains=search_nationality
        )

    # Check if at least one of the values is not None
    elif search_name is not None:
        directors = Director.objects.filter(full_name__icontains=search_name)

    elif search_nationality is not None:
        directors = Director.objects.filter(nationality__icontains=search_nationality)

    # If both arguments are None, return an empty string
    else:
        return ""

    # Order directors by full name, ascending
    directors = directors.order_by('full_name')

    # Format the result as a string
    result_string = []
    for director in directors:
        result_string.append(f"Director: {director.full_name}, nationality: {director.nationality}, experience: "
                          f"{director.years_of_experience}")

    return "\n".join(result_string)


def get_top_director():
    # Use the custom model manager method to get directors by movies count
    top_director = Director.objects.get_directors_by_movies_count().first()

    # If there is no top director, return an empty string
    if not top_director:
        return ""

    # Get the number of movies for the top director
    num_of_movies = top_director.movie_set.count()

    # Format the result string
    result_string = f"Top Director: {top_director.full_name}, movies: {num_of_movies}."

    return result_string


def get_top_actor():
    # Get the starring actor with the greatest number of movies
    top_actor = Actor.objects.annotate(num_movies=Count('starring_movies')).order_by('-num_movies', 'full_name').first()

    # If there is no top actor, return an empty string
    if not top_actor:
        return ""

    # Get the movie titles and calculate the average rating
    movie_titles = top_actor.starring_movies.values_list('title', flat=True)
    movies_avg_rating = top_actor.starring_movies.aggregate(avg_rating=Avg('rating'))['avg_rating']

    # If there are no movies, return an empty string
    if not movie_titles or movies_avg_rating is None:
        return ""

    # Format the result string
    result_string = (f"Top Actor: {top_actor.full_name}, starring in movies: {', '.join(movie_titles)}, "
                     f"movies average rating: {movies_avg_rating:.1f}")

    return result_string


def get_actors_by_movies_count():
    # Get the top three actors ordered by the number of movies they have participated in
    top_actors = Actor.objects.annotate(num_movies=Count('movies')).order_by('-num_movies', 'full_name')[:3]

    # If there are no actors, return an empty string
    if not top_actors:
        return ""

    # Format the result string
    result_string = []
    for actor in top_actors:
        result_string.append(f"{actor.full_name}, participated in {actor.num_movies} movies")

    return "\n".join(result_string)


def get_top_rated_awarded_movie():
    # Get the movie with the highest rating that has been awarded
    top_rated_movie = Movie.objects.filter(is_awarded=True).aggregate(
        max_rating=Max('rating'),
        max_id=Max('id', output_field=models.IntegerField())
    )

    # If there are no awarded movies, return an empty string
    if top_rated_movie['max_rating'] is None:
        return ""

    # Get the top-rated awarded movie
    top_rated_awarded_movie = Movie.objects.filter(
        id=top_rated_movie['max_id'],
        rating=top_rated_movie['max_rating'],
        is_awarded=True
    ).first()

    # Get the starring actor, movie rating, and participating actors
    starring_actor = top_rated_awarded_movie.starring_actor
    movie_rating = top_rated_awarded_movie.rating
    participating_actors = top_rated_awarded_movie.actors.all().order_by('full_name')

    # Format the starring actor and participating actors
    starring_actor_name = starring_actor.full_name if starring_actor else 'N/A'
    participating_actors_names = ', '.join(actor.full_name for actor in participating_actors)

    # Format the result string
    result_string = (
        f"Top rated awarded movie: {top_rated_awarded_movie.title}, "
        f"rating: {movie_rating:.1f}. Starring actor: {starring_actor_name}. "
        f"Cast: {participating_actors_names}."
    )

    return result_string


def increase_rating():
    # Increase the rating for classic movies by 0.1 (zero point one)
    updated_movies = Movie.objects.filter(is_classic=True, rating__lt=10.0).update(rating=F('rating') + 0.1)

    # If no movies were updated, return the corresponding message
    if updated_movies == 0:
        return "No ratings increased."

    # Format the result string
    result_string = f"Rating increased for {updated_movies} movies."

    return result_string


print(increase_rating())