from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, UserSerializer
from .models import Expense

@api_view(["POST"]) 
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        data = UserSerializer(user).data
        return Response({"message": "User registered successfully", "user": data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"]) 
def get_users(request):
    users = User.objects.all().order_by("id")
    data = UserSerializer(users, many=True).data
    return Response(data)


@api_view(["GET", "DELETE"]) 
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(UserSerializer(user).data)

    if request.method == "DELETE":
        user.delete()
        return Response({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"]) 
def expenses_summary(request):
    totals = (
        Expense.objects.values("category__name")
        .annotate(total=Sum("amount"))
        .order_by("category__name")
    )
    result = {item["category__name"]: float(item["total"]) for item in totals}
    return Response(result)


def ui_home(request):
    return render(request, "project/index.html")


def ui_register(request):
    return render(request, "project/register.html")


def ui_users(request):
    return render(request, "project/users.html")


def ui_expenses_summary(request):
    return render(request, "project/expenses_summary.html")
