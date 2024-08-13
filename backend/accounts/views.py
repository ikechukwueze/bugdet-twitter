from django.shortcuts import render
from rest_framework import views
from rest_framework import response
from rest_framework import status
from rest_framework import generics
from .models import Account
from .serializers import AccountSignUpSerializer, LoginSerializer, AccountSerializer

# Create your views here.



class AccountSignUpView(views.APIView):
    authentication_classes = []

    def post(self, request):
        serializer = AccountSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        account_details = {
            "first_name": account.first_name,
            "last_name": account.last_name,
            "email": account.email,
            "username": account.username
        }
        return response.Response(account_details, status=status.HTTP_201_CREATED)



class AccountLoginView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # account = serializer.validated_data["account"]
        # serializer.save()
        # print(serializer.data)
        # account_details = {
        #     "email": account.email,
        #     "username": account.username,
        #     "display_name": account.display_name,
        #     "profile_pic": account.profile_pic.url,
        #     "token": account.get_token(),
        # }

        return response.Response(serializer.data, status=status.HTTP_200_OK)



class RetrieveUserDetailView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_field = 'username'
    lookup_url_kwarg = 'username'