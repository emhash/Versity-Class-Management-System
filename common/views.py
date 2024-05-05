from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv
from datetime import datetime, timedelta

from .forms import *
from .models import UpcomingExams, ClassRoutine
from .filters import StudentFilter
from .extra_code import routine_maker, allowed_users, RouniteCreator

import os
load_dotenv()

# 06-03-2024 Wrorking here (Done)
@login_required()
@allowed_users(allowed_role=['student', 'cr'])
def homepage(request):
    now = timezone.now()
    student = get_object_or_404(Student, account = request.user.profile)
    his_intake = student.intake    
    his_department = student.department
    his_section = student.section
    # his_shift = ------
    # ------ Retrive all Upcomming exams -----
    all_exams = UpcomingExams.objects.filter(
        intake= his_intake,
        department= his_department,
        section= his_section,
        date__gte=now
    ).order_by("date")

    announcements = Announcements.objects.filter(
        intake = his_intake,
        department = his_department,
        section = his_section,
    ).order_by("-created_at")

    assignments = Assignments.objects.filter(
        intake = his_intake,
        department = his_department,
        section = his_section,
        date__gte=now,
    ).order_by("date")

    students = Student.objects.filter(
        intake = his_intake,
        department = his_department,
        section = his_section,
        account__is_approved = True,
    ).order_by("personal_id")[:8]

    timeline = []
    # counter = max(assignments.count(), all_exams.count())
    for data in assignments:
        timeline.append(data)
    for data in all_exams:
        timeline.append(data)
    
    # for d in timeline:
    #     print(d)


    # ------ Retrive class routine for specific intake , section ------
    class_routine = ClassRoutine.objects.filter(intake = his_intake, 
                                                section = his_section, 
                                                department = his_department
                                                )
    cls_routine = routine_maker(class_routine)

    times = {
    "08:00:00":"08:00AMto09:15AM",
    "09:15:00":"09:15AMto10:30AM",
    "10:30:00":"10:30AMto11:45AM",
    "11:45:00":"11:45AMto01:00PM",
    "13:30:00":"01:30PMto02:45PM",
    "14:45:00":"02:45PMto04:00PM",
    "15:00:00":"04:00PMto05:15PM",
    "16:15:00":"05:15PMto06:30PM",
    }
    todays_classes = {

    }
    time_now = datetime.now()
    today_is = datetime.weekday(time_now)
    print("Today is ======>>>  ",datetime.weekday(time_now))
    time_early = time_now - timedelta(hours=1, minutes=15)
    # time_advance = time_now + timedelta(hours=1, minutes=15)
    
    present_time = time_now.strftime('%H:%M') 
    one_hr_15_min_early = time_early.strftime('%H:%M:%S') 
    # one_hr_15_min_ahead = time_advance.strftime('%H:%M:%S') 

    one_hr_15_min_early = "15:50:35"
    present_time = "16:50:35"

    running_class = None
    coming_class = None
    for keys in times:
        if one_hr_15_min_early <= keys and keys < present_time:
            running_class = times[keys]
        elif keys >= present_time:
            coming_class = times[keys]
            break

    # print("Running Class:", running_class)
    # print("Coming Class:", coming_class)

    
    # for keyy,vall in cls_routine.items():
    #     print(keyy)
    #     print(vall)

    rtn_obj = RouniteCreator(your_routine=class_routine)
    # routine = rtn_obj.routine_genarator()
    # print(routine)

    print("====>>>> <<<<====","\n",rtn_obj.routine_genarator(class_routine, 
                                    is_for_multiple_days=False, 
                                    current_day=1
                                    ))
    


    # print("TIME NOW ====> ",time_now)
    # print("PRESENT TIME NOW ====> ",present_time)
    # print("15 min EARLY ==> ",one_hr_15_min_early)

    context = {
        "exams":all_exams,
        "routine":cls_routine,
        "announcements":announcements,
        "students":students,
        "remain_task":assignments,
        "running_class":running_class,
        "coming_class":coming_class,
        "timeline":timeline,
        
    }            
    return render(request, "pages/index.html", context)
    
# -========== LOGIN AND REGISTER PART STARTS +============-------

# 15-02-2024 Wrorking here (Done)
@login_required()
def last_step_of_register(request):
    profile = request.user.profile
    role = request.user.role
    if profile.details_filled:
        return redirect("homepage")
    else:
        if role == 'cr' or role == 'student':
            if request.method == "POST":
                form = StudentForm(request.POST, request.FILES)
                if form.is_valid():
                    the_form = form.save(commit=False)
                    the_form.account = profile
                    the_form.save()

                    profile.details_filled = True
                    profile.save()
                    messages.success(request,"Registration and Profile setup successfull.")
                    return redirect(request.path)
            else:
                form = StudentForm()

            context = {"form":form}
            return render(request, "auths/register.html", context)
    
        elif role == 'admin':
            return HttpResponse("Oops! By choosing wrong role your account suspended. Contact with admin. Or create another account. click '''/logout/''' to LogOut From the site. ")
        elif role == 'teacher':
            return HttpResponse("Sorry!. Teacher section is uder construction. click '''/logout/''' to LogOut From the site. ")
        else:
            return HttpResponse("Wait a minute! WHO ARE YOU??")
    



# 01-02-2024 Wrorking here (Done)
def register(request):
    if request.method == "POST":
        form = CommonRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = form.instance
            login(request, user)
            messages.success(request, "You have successfully created an account!")
            return redirect("homepage")
        
    else:
        form = CommonRegistrationForm()

    context = {
        "form":form,
    }
    return render(request, "auths/registration.html", context)


# 15-02-2024 Wrorking here (Done)
def user_login(request):
    if request.user.is_authenticated:
        messages.info(request,"Sorry! you are already logged in.")
        return redirect("homepage")
    else:
        if request.method == "POST":
            email = request.POST.get('useremail')
            password = request.POST.get('userpassword')

            try:
                user = authenticate(email=email, password=password)
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect("homepage")
            except Exception as e:
                # print(e)
                messages.error(request, "Invalid credentials or wrong information! Try again.")
                return redirect(request.path)

        return render(request, "auths/login.html")




# +=======--------- LOGIN and REGISTER PART DONE --------=============

# 01-02-2024 Wrorking here (Done)
@login_required()
def do_logout(request):
    if request.user.is_authenticated:
        try:
            logout(request)
            return redirect("homepage")
        except Exception as e:
            print(e)
            messages.error(request, "Error when try to log out!")
            return redirect("homepage")
    else:
        messages.warning(request,"You can not perform this operation now.")
        return redirect("homepage")
    

# 08-03-2024 Wrorking here (Done)
@login_required()
def exams(request):
    if request.user.role == "cr" or request.user.role == "student": 
        the_student = get_object_or_404(Student, account = request.user.profile)
        his_intake = the_student.intake    
        his_department = the_student.department
        his_section = the_student.section

        all_exams = UpcomingExams.objects.filter(
                    intake= his_intake,
                    department= his_department,
                    section= his_section,
        ).order_by("-date")
        if request.method == "POST":
            form = UpcomingExamsForm(request.POST)
            if form.is_valid():
                the_form = form.save(commit=False)
                the_form.intake = his_intake 
                the_form.department = his_department 
                the_form.section = his_section 
                the_form.save()
                messages.success(request,"Exam schedule added!")
                return redirect(request.path)
        else:
            form = UpcomingExamsForm()

    elif request.user.role == "admin":
        all_exams = UpcomingExams.objects.all()
        form = None

   # Handle other role who are not the student 
    else:
        all_exams = None
        form = None

    context = {
        "all_exam":all_exams,
        "form":form,
    }
    return render(request, 'pages/exams.html', context)


# 08-03-2024 Wrorking here (Done)
@login_required()
def pendigs(request):
    context = {
        "page":"/Pendeng/"
               }
    
    # admin or Intake Incharge can see the all non approved profiles
    if request.user.role == "admin":
        non_approved_profile = Student.objects.filter(account__is_approved = False)
        context["pending_student" ] = non_approved_profile
        if request.method == "POST":
            try:
                if "approve" in request.POST:
                    s_uid = request.POST['approve']
                    target = non_approved_profile.get(uid = s_uid)
                    targets_profile = target.account
                    targets_profile.is_approved = True
                    targets_profile.save()
                    messages.success(request,"Approved confirmed!")
                    return redirect(request.path)
            except Exception:
                messages.warning(request,"Sorry! Can not proceed!")
                return redirect(request.path)
            
    # CR can aprove only based on his intake and section and so on
    elif request.user.role == "cr":
        the_cr = get_object_or_404(Student, account = request.user.profile)
        his_intake = the_cr.intake
        his_section = the_cr.section
        his_department = the_cr.department
        his_shift = the_cr.shift

        if the_cr.is_class_cr:
            specific_intake_and_section_profile = Student.objects.filter(
                account__is_approved = False,
                intake = his_intake,
                department = his_department,
                shift = his_shift,
                section = his_section
                )
            
            context["pending_student"] = specific_intake_and_section_profile

            if request.method == "POST":
                if "approve" in request.POST:
                    s_uid = request.POST['approve']
                    target = specific_intake_and_section_profile.get(uid = s_uid)
                    targets_profile = target.account
                    targets_profile.is_approved = True
                    targets_profile.save()
                    messages.success(request,"Approved confirmed!")
                    return redirect(request.path)

        else:
            messages.warning(request,"You are not meant for approve students! I'm gently redirecting you now, Don't try to mess with anything!")
            # INSTEAD OF REDIRECT LATER WRLL THROW 404 Page
            return redirect("homepage")
    else:
        messages.info(request,"You are not meant for approve students!")
        # INSTEAD OF REDIRECT LATER WRLL THROW 404 Page
        return redirect("homepage")
    
    return render(request, "pages/student_approval.html", context)


# 9-3-2024 -->> WORK (Done)
@login_required()
@allowed_users(allowed_role=['student', 'cr','admin','teacher'])
def all_cr(request):
    cr_students = Student.objects.filter(is_class_cr = True, account__user__role = 'cr')

    # -----=== ADDING FILTERING ==== -----
    # S-1:
    enable_filtering = StudentFilter(request.GET, queryset=cr_students)
    # S-2:
    returning_object_with_filter = enable_filtering.qs
    # ====================================

    context={
        "crs":returning_object_with_filter,
        "search_option":enable_filtering,
             }
    return render(request, "pages/all_cr.html",context)



# 10-03-2024 -- WORING with routine HERE (DONE)
# (Need to fix the duplicate day routine by dictionary) --> DONE

@login_required()
@allowed_users(allowed_role=['student', 'cr'])
def add_routine(request):
    student = request.user.profile.student
    if request.user.role == 'cr':
        if request.method == "POST":
            form = ClassRoutineForm(request.POST)
            if form.is_valid():
                try:
                    the_form = form.save(commit=False)
                    the_form.intake = student.intake
                    the_form.section = student.section
                    the_form.department = student.department
                    the_form.save()
                    messages.success(request, "Added a routine successfully!")
                    return redirect(request.path)
                except Exception as e:
                    messages.warning(request, f"Error: {e}")
                    return redirect(request.path)
            # else:
            #     messages.warning(request, "Sorry, Failed to submit form!")
            #     return redirect(request.path)
        else:
            form = ClassRoutineForm()
    else:
        form = None
    
    # ------ Retrive class routine for specific intake , section ------
    your_routine = ClassRoutine.objects.filter(intake = student.intake, 
                                                section = student.section, 
                                                department = student.department
                                                ).order_by('time')
    
    routine = routine_maker(your_routine)

    context = {
        "routine":routine,
        "form":form,
    }
    return render(request, "pages/add_routine.html", context)


# 10-03-2024 Wrorked bit | 16-04-2024 (DONE)<<<-======
# [*Future update -- Here the upcomming assignments will show no doubt,
# But as it is showing upcomming assignments accourding to the current date
# the previous expire assignments will no longer visible in the timeline
# so there will need a display of history of all the expired assignments 
# *]
@login_required()
@allowed_users(allowed_role=['student', 'cr'])
def assignments(request):
    student = request.user.profile.student
    intake = student.intake
    section = student.section
    depart = student.department
    all_assignments = Assignments.objects.filter(
        intake = intake,
        department = depart,
        section = section,
        date__gte = timezone.now()
    ).order_by("date")[:5]
    context = {
        "assignments":all_assignments,
    }
    return render(request, "pages/assignments.html", context)

# 10-03-2024 Wrorking here (DONE)
@login_required()
@allowed_users(allowed_role=['cr'])
def add_assignments(request):
    student = request.user.profile.student
    if request.method == "POST":
        form = AssignmentsForm(request.POST)
        if form.is_valid():
            try:
                the_form = form.save(commit=False)
                the_form.intake = student.intake
                the_form.section = student.section
                the_form.department = student.department
                the_form.save()
                messages.success(request, "Added successfully!")
                return redirect(request.path)
            except Exception as e:
                messages.warning(request, f"Error: {e}")
                return redirect("assignments")   
    else:
        form = AssignmentsForm()
    context = {
        "form":form,

    }
    return render(request, "pages/add_assignments.html", context)

# 12-03-2024 -- DONE 
@login_required()
@allowed_users(allowed_role=['student','cr'])
def calender(request):
    context = {
        "calenderAPI": os.getenv('API_CALENDER')
    }
    return render(request, "pages/calender.html", context)


# 16-04-2024 ---<<==DONE
@login_required()
@allowed_users(allowed_role=['student', 'cr'])
def view_assignment(request, the_id):
    context = {
        "task":get_object_or_404(Assignments, uid = the_id.strip())

    }
    return render(request, "pages/view_assignment.html", context)

# 17-04-2024 --- WORKING HERE  - DONE
@login_required()
@allowed_users(allowed_role=['student', 'cr'])
def all_announcement(request):
    student = request.user.profile.student

    intake = student.intake
    section = student.section
    depart = student.department
    announcements = Announcements.objects.filter(
        intake = intake,
        department = depart,
        section = section,
    ).order_by("-created_at")
    context = {
        "announcements":announcements,
    }

    return render(request, "pages/all_announcement.html",context)

# 21-04-2024 -- DONE
@login_required()
@allowed_users(allowed_role=['student', 'cr'])
def add_announcement(request):
    student = request.user.profile.student
    if request.method == "POST":
        form = AnnouncementsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                the_form = form.save(commit=False)
                the_form.who_posted = student
                the_form.intake = student.intake
                the_form.section = student.section
                the_form.department = student.department
                the_form.save()
                messages.success(request, "Added successfully!")
                return redirect(request.path)
            except Exception as e:
                messages.warning(request, f"Error: {e}")
                return redirect("all_announcement") 
    else:
        form = AnnouncementsForm()
    
    context = {"form":form}
    return render(request, "pages/add_announcement.html", context)

#  ------ UPCOMING CHANGES NEED -----------

#1 USE TIMELINE OF NEXT ONE WEEK.
#2 USE Chat App 
#3 FIX - calender API need to hide, 
#4 Assignment and exam edit option
#5 Other sections or intakes student who took improvement - handle them
#6 After section modification - means new registration of new semester 
#  there could be a chance to change in mates of a section of a intake 
#  so have to add a session or semester option to re-apply and re-pending.
#7 Let the Admin Register and add one admin to approve another admin or studentCR .
#8 Admin will only see the pending section , Not the entire panel. Make sure to permission fixed
#9 Edit the routine -- clicking the course at the routine that perticular class of that day 
#  can be edit by CR.

# ---------------------------------------------------------

# Temprorary view function below -->
def test_function(request):
    for p in Student.objects.raw("SELECT * FROM common_student"):
        print(p)

    context = {
        "students": None
    }
    return render(request, "pages/temp.html", context)