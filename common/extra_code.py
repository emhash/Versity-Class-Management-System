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


class RouniteCreator():
    def __init__(self, your_routine):
        self.your_routine = your_routine
        
    def day_of_week(self, number_of_day):
        # number_of_day must be an integer.
        days = {
            5:"sat",
            6:"sun",
            0:"mon",
            1:"tue",
            2:"wed",
            3:"thu",
            4:"fri",
            }
        if number_of_day >= 0 and number_of_day <=6:
            return days[number_of_day]
        else:
            return None
        
    def routine_genarator(self, days=1,is_for_multiple_days=True,current_day=0): 
        routines = {}
        if is_for_multiple_days:
            for i in range(days):
                the_day = self.day_of_week(i)
                routines[i] = [
                    self.your_routine.filter(time="08:00AMto09:15AM" , day=the_day).first(),
                    self.your_routine.filter(time="09:15AMto10:30AM" , day=the_day).first(),
                    self.your_routine.filter(time="10:30AMto11:45AM" , day=the_day).first(),
                    self.your_routine.filter(time="11:45AMto01:00PM" , day=the_day).first(),
                    self.your_routine.filter(time="01:30PMto02:45PM" , day=the_day).first(),
                    self.your_routine.filter(time="02:45PMto04:00PM" , day=the_day).first(),
                    self.your_routine.filter(time="04:00PMto05:15PM" , day=the_day).first(),
                    self.your_routine.filter(time="05:15PMto06:30PM" , day=the_day).first(),
                        ]
        else:
            # print("Else BLOCK")
            # if days > 1 or days <= 0 :
            #     print("You choose to use single day's routine")

            if current_day < 7 and current_day >=0:
                the_day=self.day_of_week(current_day)
                routines[current_day] = [
                    self.your_routine.filter(time="08:00AMto09:15AM" , day=the_day).first(),
                    self.your_routine.filter(time="09:15AMto10:30AM" , day=the_day).first(),
                    self.your_routine.filter(time="10:30AMto11:45AM" , day=the_day).first(),
                    self.your_routine.filter(time="11:45AMto01:00PM" , day=the_day).first(),
                    self.your_routine.filter(time="01:30PMto02:45PM" , day=the_day).first(),
                    self.your_routine.filter(time="02:45PMto04:00PM" , day=the_day).first(),
                    self.your_routine.filter(time="04:00PMto05:15PM" , day=the_day).first(),
                    self.your_routine.filter(time="05:15PMto06:30PM" , day=the_day).first(),
                        ]
            else:
                print("A week's days count from 0 to 6, 0 = MonDay")
                


        return routines
    