from .base import *
SECRET_KEY = env('DJANGO_SECRET_KEY', default='+@azwf*b(c6_(s$#ifdrfya(n35(h+rs9h*h6m0n=ixmst56r=')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
