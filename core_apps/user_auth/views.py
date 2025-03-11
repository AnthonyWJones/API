from django.http import JsonResponse
from django.views import View
from loguru import logger


class TestLoginView(View):
    def get(self, request):
        logger.debug('TestLoginView debug called')
        logger.info('TestLoginView info called')
        logger.warning('TestLoginView warning called')
        logger.critical('TestLoginView critical called')
        logger.debug('TestLoginView called')
        return JsonResponse({"message": "We are testing loguru" })