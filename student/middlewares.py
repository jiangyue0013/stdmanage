import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 这是请求到middleware 中时进入的第一个方法。
        # 一般情况下，我们可以在这里做一些校验。

        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse("index"):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view: {:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('request to response cose: {:.2f}s'.format(costed))
        return response