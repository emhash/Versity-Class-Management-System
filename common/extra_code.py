from django.shortcuts import HttpResponse,redirect,render

def allowed_users(allowed_role = []):
    def normal_function(view_function):
        def warper_function(request, *args, **kwargs):
            # print("Successfully custom decorator working")
            # print("ROLE --->> ", allowed_role)
            profile = request.user.profile 
            if profile.details_filled:
                if profile.is_approved:
                    if request.user.role in allowed_role:
                        return view_function(request, *args, **kwargs)
            
                    else:
                        return HttpResponse("WHO ARE YOU ? Not authorized person.")
                else:
                    return render(request,"pages/waiting.html")
            else:
                return redirect("last_step_of_register")                    

        return warper_function
    return normal_function



def routine_maker(your_routine):
    routine = {
            
            "SAT": [
                your_routine.filter(time="08:00AMto09:15AM" , day="sat").first(),
                your_routine.filter(time="09:15AMto10:30AM" , day="sat").first(),
                your_routine.filter(time="10:30AMto11:45AM" , day="sat").first(),
                your_routine.filter(time="11:45AMto01:00PM" , day="sat").first(),
                your_routine.filter(time="01:30PMto02:45PM" , day="sat").first(),
                your_routine.filter(time="02:45PMto04:00PM" , day="sat").first(),
                your_routine.filter(time="04:00PMto05:15PM" , day="sat").first(),
                your_routine.filter(time="05:15PMto06:30PM" , day="sat").first(),
                    ],
            "SUN": [
                your_routine.filter(time="08:00AMto09:15AM" , day="sun").first(),
                your_routine.filter(time="09:15AMto10:30AM" , day="sun").first(),
                your_routine.filter(time="10:30AMto11:45AM" , day="sun").first(),
                your_routine.filter(time="11:45AMto01:00PM" , day="sun").first(),
                your_routine.filter(time="01:30PMto02:45PM" , day="sun").first(),
                your_routine.filter(time="02:45PMto04:00PM" , day="sun").first(),
                your_routine.filter(time="04:00PMto05:15PM" , day="sun").first(),
                your_routine.filter(time="05:15PMto06:30PM" , day="sun").first(),
                    ],
            "MON": [
                your_routine.filter(time="08:00AMto09:15AM" , day="mon").first(),
                your_routine.filter(time="09:15AMto10:30AM" , day="mon").first(),
                your_routine.filter(time="10:30AMto11:45AM" , day="mon").first(),
                your_routine.filter(time="11:45AMto01:00PM" , day="mon").first(),
                your_routine.filter(time="01:30PMto02:45PM" , day="mon").first(),
                your_routine.filter(time="02:45PMto04:00PM" , day="mon").first(),
                your_routine.filter(time="04:00PMto05:15PM" , day="mon").first(),
                your_routine.filter(time="05:15PMto06:30PM" , day="mon").first(),
                    ],
            "TUE": [
                your_routine.filter(time="08:00AMto09:15AM" , day="tue").first(),
                your_routine.filter(time="09:15AMto10:30AM" , day="tue").first(),
                your_routine.filter(time="10:30AMto11:45AM" , day="tue").first(),
                your_routine.filter(time="11:45AMto01:00PM" , day="tue").first(),
                your_routine.filter(time="01:30PMto02:45PM" , day="tue").first(),
                your_routine.filter(time="02:45PMto04:00PM" , day="tue").first(),
                your_routine.filter(time="04:00PMto05:15PM" , day="tue").first(),
                your_routine.filter(time="05:15PMto06:30PM" , day="tue").first(),
                    ],
            "WED": [
                your_routine.filter(time="08:00AMto09:15AM" , day="wed").first(),
                your_routine.filter(time="09:15AMto10:30AM" , day="wed").first(),
                your_routine.filter(time="10:30AMto11:45AM" , day="wed").first(),
                your_routine.filter(time="11:45AMto01:00PM" , day="wed").first(),
                your_routine.filter(time="01:30PMto02:45PM" , day="wed").first(),
                your_routine.filter(time="02:45PMto04:00PM" , day="wed").first(),
                your_routine.filter(time="04:00PMto05:15PM" , day="wed").first(),
                your_routine.filter(time="05:15PMto06:30PM" , day="wed").first(),
                    ],
            "THU": [
                your_routine.filter(time="08:00AMto09:15AM" , day="thu").first(),
                your_routine.filter(time="09:15AMto10:30AM" , day="thu").first(),
                your_routine.filter(time="10:30AMto11:45AM" , day="thu").first(),
                your_routine.filter(time="11:45AMto01:00PM" , day="thu").first(),
                your_routine.filter(time="01:30PMto02:45PM" , day="thu").first(),
                your_routine.filter(time="02:45PMto04:00PM" , day="thu").first(),
                your_routine.filter(time="04:00PMto05:15PM" , day="thu").first(),
                your_routine.filter(time="05:15PMto06:30PM" , day="thu").first(),
                    ],
            "FRI": [
                your_routine.filter(time="08:00AMto09:15AM" , day="fri").first(),
                your_routine.filter(time="09:15AMto10:30AM" , day="fri").first(),
                your_routine.filter(time="10:30AMto11:45AM" , day="fri").first(),
                your_routine.filter(time="11:45AMto01:00PM" , day="fri").first(),
                your_routine.filter(time="01:30PMto02:45PM" , day="fri").first(),
                your_routine.filter(time="02:45PMto04:00PM" , day="fri").first(),
                your_routine.filter(time="04:00PMto05:15PM" , day="fri").first(),
                your_routine.filter(time="05:15PMto06:30PM" , day="fri").first(),
                    ],
        }
    return routine
    