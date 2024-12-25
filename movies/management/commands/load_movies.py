import json
import os
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Load movies data from JSON file'

    def handle(self, *args, **kwargs):
        json_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'movies.json')
        with open(json_file, 'r', encoding='utf-8') as file:
            movies_data = json.load(file)
            
        for movie_data in movies_data:
            # Remove duplicate 'assets/' path from imgPath if it exists
            if movie_data['imgPath'].startswith('assets/'):
                movie_data['imgPath'] = movie_data['imgPath'][7:]
            Movie.objects.create(**movie_data)
            
        self.stdout.write(self.style.SUCCESS('Successfully loaded movies data'))
