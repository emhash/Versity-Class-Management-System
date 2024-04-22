from django.shortcuts import render, redirect, get_list_or_404, HttpResponse
from django.contrib.auth.decorators import login_required

from common.extra_code import allowed_users
from common.models import Student

# 22-04-2024 -- DONE
@login_required()
@allowed_users(allowed_role=['student', 'cr'])
def chat_view(request):

    return render(request, "chat/chat.html")

# 23-04-2024 -- DONE
@login_required()
@allowed_users(allowed_role=['student', 'cr'])
def chat_with(request, who):
    context = {}
    if who == "crs":
        context["chat_mate"] = Student.objects.filter(is_class_cr = True)
    elif who == "mates":
        context["chat_mate"] = Student.objects.filter(is_class_cr = True)
        
    else:
        HttpResponse("Something wrong can't accessable!")

    return render(request, "chat/chatwith.html", context)
