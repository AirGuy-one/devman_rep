from django.core.management.base import BaseCommand
import os
from pathlib import Path

class Command(BaseCommand):
    help = 'Display the args'

    def handle(self, *args, **kwargs):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        os.chdir(BASE_DIR)
        os.mkdir('static')
        os.mkdir('media')
        os.chdir(os.path.join(BASE_DIR, 'media'))
        os.mkdir('images')
        os.chdir(os.path.join(BASE_DIR, 'load_static'))
        os.mkdir('places')
