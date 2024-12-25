from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Movie
from django.templatetags.static import static

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def search_movies(request):
    query = request.GET.get('query', '')
    movies = Movie.objects.filter(name__icontains=query)
    data = [{
        'id': movie.id,
        'name': movie.name,
        'imgPath': static(movie.imgPath),
        'duration': movie.duration,
        'userRating': movie.userRating
    } for movie in movies]
    return JsonResponse({'movies': data})
    
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
