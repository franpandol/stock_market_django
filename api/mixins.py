import logging

logger = logging.getLogger("stock_market.apicalls")


class RequestLogMiddleware(object):
    def initial(self, request, *args, **kwargs):
        super(RequestLogMiddleware, self).initial(request, *args, **kwargs)
        logger.info(f"[API_REQUEST] {request.method} {request.path} {request.user}")
