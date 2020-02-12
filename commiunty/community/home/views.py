from django.shortcuts import render, redirect


def home(request):
    """
    主页
    """
    return redirect('questions:question_list')