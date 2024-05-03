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
            # print()
            # if days > 1 or days <= 0 :
            #     print("You choose to use single day's routine")

            if current_day < 7 and current_day >=0:
                the_day=self.day_of_week(current_day)

            else:
                print("A week's days count from 0 to 6, 0 = MonDay")
                


        return routines
        


def routine_maker(your_routine):
    days = {
        5:"sat",
        6:"sun",
        0:"mon",
        1:"tue",
        2:"wed",
        3:"thu",
        4:"fri",
        }
    routines = {}
    for i in range(7):
        routines[i] = [
                your_routine.filter(time="08:00AMto09:15AM" , day=days[i]).first(),
                your_routine.filter(time="09:15AMto10:30AM" , day=days[i]).first(),
                your_routine.filter(time="10:30AMto11:45AM" , day=days[i]).first(),
                your_routine.filter(time="11:45AMto01:00PM" , day=days[i]).first(),
                your_routine.filter(time="01:30PMto02:45PM" , day=days[i]).first(),
                your_routine.filter(time="02:45PMto04:00PM" , day=days[i]).first(),
                your_routine.filter(time="04:00PMto05:15PM" , day=days[i]).first(),
                your_routine.filter(time="05:15PMto06:30PM" , day=days[i]).first(),
                    ]

    # routine = {
            
    #         "SAT": [
    #             your_routine.filter(time="08:00AMto09:15AM" , day="sat").first(),
    #             your_routine.filter(time="09:15AMto10:30AM" , day="sat").first(),
    #             your_routine.filter(time="10:30AMto11:45AM" , day="sat").first(),
    #             your_routine.filter(time="11:45AMto01:00PM" , day="sat").first(),
    #             your_routine.filter(time="01:30PMto02:45PM" , day="sat").first(),
    #             your_routine.filter(time="02:45PMto04:00PM" , day="sat").first(),
    #             your_routine.filter(time="04:00PMto05:15PM" , day="sat").first(),
    #             your_routine.filter(time="05:15PMto06:30PM" , day="sat").first(),
    #                 ],
    #         "SUN": [
    #             your_routine.filter(time="08:00AMto09:15AM" , day="sun").first(),
    #             your_routine.filter(time="09:15AMto10:30AM" , day="sun").first(),
    #             your_routine.filter(time="10:30AMto11:45AM" , day="sun").first(),
    #             your_routine.filter(time="11:45AMto01:00PM" , day="sun").first(),
    #             your_routine.filter(time="01:30PMto02:45PM" , day="sun").first(),
    #             your_routine.filter(time="02:45PMto04:00PM" , day="sun").first(),
    #             your_routine.filter(time="04:00PMto05:15PM" , day="sun").first(),
    #             your_routine.filter(time="05:15PMto06:30PM" , day="sun").first(),
    #                 ],
    #         "MON": [
    #             your_routine.filter(time="08:00AMto09:15AM" , day="mon").first(),
    #             your_routine.filter(time="09:15AMto10:30AM" , day="mon").first(),
    #             your_routine.filter(time="10:30AMto11:45AM" , day="mon").first(),
    #             your_routine.filter(time="11:45AMto01:00PM" , day="mon").first(),
    #             your_routine.filter(time="01:30PMto02:45PM" , day="mon").first(),
    #             your_routine.filter(time="02:45PMto04:00PM" , day="mon").first(),
    #             your_routine.filter(time="04:00PMto05:15PM" , day="mon").first(),
    #             your_routine.filter(time="05:15PMto06:30PM" , day="mon").first(),
    #                 ],
    #         "TUE": [
    #             your_routine.filter(time="08:00AMto09:15AM" , day="tue").first(),
    #             your_routine.filter(time="09:15AMto10:30AM" , day="tue").first(),
    #             your_routine.filter(time="10:30AMto11:45AM" , day="tue").first(),
    #             your_routine.filter(time="11:45AMto01:00PM" , day="tue").first(),
    #             your_routine.filter(time="01:30PMto02:45PM" , day="tue").first(),
    #             your_routine.filter(time="02:45PMto04:00PM" , day="tue").first(),
    #             your_routine.filter(time="04:00PMto05:15PM" , day="tue").first(),
    #             your_routine.filter(time="05:15PMto06:30PM" , day="tue").first(),
    #                 ],
    #         "WED": [
    #             your_routine.filter(time="08:00AMto09:15AM" , day="wed").first(),
    #             your_routine.filter(time="09:15AMto10:30AM" , day="wed").first(),
    #             your_routine.filter(time="10:30AMto11:45AM" , day="wed").first(),
    #             your_routine.filter(time="11:45AMto01:00PM" , day="wed").first(),
    #             your_routine.filter(time="01:30PMto02:45PM" , day="wed").first(),
    #             your_routine.filter(time="02:45PMto04:00PM" , day="wed").first(),
    #             your_routine.filter(time="04:00PMto05:15PM" , day="wed").first(),
    #             your_routine.filter(time="05:15PMto06:30PM" , day="wed").first(),
    #                 ],
    #         "THU": [
    #             your_routine.filter(time="08:00AMto09:15AM" , day="thu").first(),
    #             your_routine.filter(time="09:15AMto10:30AM" , day="thu").first(),
    #             your_routine.filter(time="10:30AMto11:45AM" , day="thu").first(),
    #             your_routine.filter(time="11:45AMto01:00PM" , day="thu").first(),
    #             your_routine.filter(time="01:30PMto02:45PM" , day="thu").first(),
    #             your_routine.filter(time="02:45PMto04:00PM" , day="thu").first(),
    #             your_routine.filter(time="04:00PMto05:15PM" , day="thu").first(),
    #             your_routine.filter(time="05:15PMto06:30PM" , day="thu").first(),
    #                 ],
    #         "FRI": [
    #             your_routine.filter(time="08:00AMto09:15AM" , day="fri").first(),
    #             your_routine.filter(time="09:15AMto10:30AM" , day="fri").first(),
    #             your_routine.filter(time="10:30AMto11:45AM" , day="fri").first(),
    #             your_routine.filter(time="11:45AMto01:00PM" , day="fri").first(),
    #             your_routine.filter(time="01:30PMto02:45PM" , day="fri").first(),
    #             your_routine.filter(time="02:45PMto04:00PM" , day="fri").first(),
    #             your_routine.filter(time="04:00PMto05:15PM" , day="fri").first(),
    #             your_routine.filter(time="05:15PMto06:30PM" , day="fri").first(),
    #                 ],
    #     }
    return routines
    