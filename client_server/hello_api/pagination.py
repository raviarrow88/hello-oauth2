from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination


class BookPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10