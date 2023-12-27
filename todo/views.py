from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from .serializer import TODOSerializer, RegisterSerializer
from .models import TODO
from django.contrib.auth.models import User
from rest_framework import views


class TODOViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ("title", "memo", "is_important", 'status')
    search_filter = ("title",)
    ordering_fields = ("is_important", "created_at", "updated_at")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(data={"success": True}, status=201)


class RegisterAPI(views.APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        if User.objects.filter(username=username).exists():
            raise ValidationError({'msg': 'Bu foydalanuvchi allaqachon mavjud'})
        user = User.objects.create_user(username=username, password=password)
        return Response({'user': user.id}, status=status.HTTP_200_OK)


class LoginAPI(views.APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username)
        if not user.exists():
            raise ValidationError({'msg': f"Ushbu {username} mavjud emas"})
        if not user.last().check_password(password):
            raise ValidationError({'msg': f"Ushbu password xato kiritilgan"})
        return Response({'msg': "Saytga muvafaqiyatli kitrdingiz"})

