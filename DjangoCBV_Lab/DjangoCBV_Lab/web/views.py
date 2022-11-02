import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index():
    pass


class IndexView:
    def __init__(self, ):
        self.values = [random.randint(1, 15), ]

    @classmethod
    def get_view(cls):
        return cls().view

    def view(self, request):
        return HttpResponse(f'It Works: {self.values}')



class Index2View(IndexView):
    def __init__(self):
        super().__init__()
        self.values.append(random.randint(15, 30))
