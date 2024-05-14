from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter) # 사용할 필터 백엔드를 정의
    filterset_class = ProductFilter # 사용자 정의 필터 클래스 지정
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']


# 이 ProductViewSet은 Django REST Framework의 ModelViewSet을 상속받고 있습니다. ModelViewSet은 다음과 같은 요청을 처리할 수 있습니다:

# GET 요청: Product 모델의 전체 목록을 조회하거나(list action), 특정 Product 인스턴스의 상세 정보를 조회합니다(retrieve action).

# POST 요청: 새로운 Product 인스턴스를 생성합니다(create action).

# PUT 요청: 특정 Product 인스턴스의 전체 필드를 업데이트합니다(update action).

# PATCH 요청: 특정 Product 인스턴스의 일부 필드만을 업데이트합니다(partial_update action).

# DELETE 요청: 특정 Product 인스턴스를 삭제합니다(destroy action).

# 이러한 요청들은 각각 CRUD(Create, Retrieve, Update, Delete) 연산에 해당하며, ModelViewSet은 이러한 연산을 모두 지원합니다. 

# 따라서 ProductViewSet도 이러한 요청을 모두 처리할 수 있습니다.

from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 3


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination