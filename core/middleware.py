import time

from django.utils.deprecation import MiddlewareMixin


class DurationRequestProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Process Request in DurationRequestProcessMiddleware')
        start = time.time()

        response = self.get_response(request)

        print('Process Response in DurationRequestProcessMiddleware')
        duration = time.time() - start
        print(f'Duration for track {request.path}: {round(duration, 2)} sec.')

        return response


class MyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('Process Request in MyMiddleware')

    def process_response(self, request, response):
        print('Process Response in MyMiddleware')
        return response

