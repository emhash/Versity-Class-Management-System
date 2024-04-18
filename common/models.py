from django.db import models
import uuid
from django.core.exceptions import ValidationError

from users.models import Intakes, Sections, Departments,Student


class CommonBaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UpcomingExams(CommonBaseModel):
    intake = models.ForeignKey(Intakes, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=10, choices=[('Class Test', 'Class Test'),('Quiz Test', 'Quiz Test'),('Mid Term', 'Mid Term'),('Final Test', 'Final Test')])
    course_name = models.CharField( max_length=50)
    course_code = models.CharField( max_length=7)
    date = models.DateField(auto_now=False, auto_now_add=False)
    topic = models.CharField(max_length=150)
    detail = models.TextField()

    def __str__(self) -> str:
        return f"{self.course_code} - {self.exam_name}"
    
DAYS = [
    ('sat','SAT'),
    ('sun','SUN'),
    ('mon','MON'),
    ('tue','TUE'),
    ('wed','WED'),
    ('thu','THU'),
    ('fri','FRI'),
]

TIMES = [
("08:00AMto09:15AM","08:00 AM to 09:15 AM"),
("09:15AMto10:30AM","09:15 AM to 10:30 AM"),
("10:30AMto11:45AM","10:30 AM to 11:45 AM"),
("11:45AMto01:00PM","11:45 AM to 01:00 PM"),
("01:30PMto02:45PM","01:30 PM to 02:45 PM"),
("02:45PMto04:00PM","02:45 PM to 04:00 PM"),
("04:00PMto05:15PM","04:00 PM to 05:15 PM"),
("05:15PMto06:30PM","05:15 PM to 06:30 PM"),
]

class ClassRoutine(CommonBaseModel):
    day = models.CharField( max_length=5, choices=DAYS)
    time = models.CharField( max_length=100, choices=TIMES)
    course_code = models.CharField( max_length=8)
    faculty_short_name = models.CharField(max_length=5)
    building = models.PositiveIntegerField()
    room = models.PositiveIntegerField()

    intake = models.ForeignKey(Intakes, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_code
    # METHOD - 01 -->>
    class Meta:
        unique_together = (('day', 'time', 'intake', 'department', 'section'),)


    # METHOD - 02 -->>
    # def save(self, *args, **kwargs):
    #     # Check if there's an existing routine with the same day, time, intake, department, and section
    #     existing_routine = ClassRoutine.objects.filter(
    #         day=self.day,
    #         time=self.time,
    #         intake=self.intake,
    #         department=self.department,
    #         section=self.section
    #     ).exists()
        
    #     if existing_routine:
    #         raise ValidationError("A routine with the same day and time already exists for this intake, department, and section.")
        
        # super().save(*args, **kwargs)


TYPES = [
    ('assignment', 'Assignment'),
    ('lab_report', 'Lab Report'),
    ('presentation', 'Peresentation'),

]

class Assignments(CommonBaseModel):
    types = models.CharField(max_length=50, choices=TYPES, default='assignment')
    course_code = models.CharField( max_length=8)
    course_title = models.CharField( max_length=100)
    assignment_title = models.CharField(max_length=150)
    detail = models.TextField()
    date = models.DateField( auto_now=False, auto_now_add=False, null=True, blank=True)

    intake = models.ForeignKey(Intakes, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.assignment_title
    
class Announcements(CommonBaseModel):
    announcement = models.CharField(max_length=500)
    image = models.ImageField(upload_to="Announcements", null=True, blank=True)
    file = models.FileField(upload_to="Announcements", null=True, blank=True)

    who_posted = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    intake = models.ForeignKey(Intakes, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.announcement}"