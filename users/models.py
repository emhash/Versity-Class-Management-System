from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class MyCustomManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email or Username must be set!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True') 
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True') 
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models. EmailField (unique=True, null=False)
    is_staff = models.BooleanField( 
        gettext_lazy('I am staff'),
        default=False,
    help_text = gettext_lazy('If the user is admin stuff of this site then can see admin panel')
    )
    is_active = models.BooleanField(
        gettext_lazy('account active'),
        default=True,
        help_text=gettext_lazy('A user should be treated as active. Admin can unselect this instead of deleting accounts')
    )
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('cr', 'cr'),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='admin',  
    )

    def is_admin(self):
        return self.role == 'admin'

    def is_student(self):
        return self.role == 'student'
    
    def is_teacher(self):
        return self.role == 'teacher'
    
    def is_cr(self):
        return self.role == 'cr'
    
    USERNAME_FIELD = 'email'
    objects = MyCustomManager()

    def __str__(self): 
        return f"USER - {self.email}"
    def get_full_name(self): 
        return self.email
    def get_short_name(self): 
        return self.email


class CommonBaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(CommonBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_approved = models.BooleanField(default=False)
    details_filled = models.BooleanField(default=False)
    
    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]
        for field_name in fields_names:
            value = getattr(self, field_name) 
            if value is None or value=='':
                return False
        return True
    
    def __str__(self): 
        return f"profile - {self.user}"
    
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs): 
    instance.profile.save()


class Departments(CommonBaseModel):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=50)
    department_chairman_name = models.CharField(max_length=350)
    chairman_room = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.short_name
    

class Sections(CommonBaseModel):
    name = models.CharField(max_length=50)
    section = models.PositiveIntegerField()
    def __str__(self):
        return f"Sec: {self.section}"
    

class Intakes(CommonBaseModel):
    intake = models.PositiveIntegerField()

    def __str__(self):
        return f"Inake: {self.intake}"
    

GENDERS = [
    ('male',"Male"),
    ('female', "Female"),
]

class CommonProfileModel(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    account = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    personal_id = models.CharField(unique=True, max_length=150)
    gender = models.CharField( max_length=50, choices=GENDERS, blank=True,null=True)
    image = models.FileField(upload_to="Profile_Pictures", null=True, blank=True)
        
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        if not self.image:
            if self.gender == "male":
                self.image.name = "avatar-male.svg"
            elif self.gender == "female":
                self.image.name = "avatar-female.svg"
        super().save(*args, **kwargs)

class Student(CommonProfileModel):
    name = models.CharField(max_length=350)
    intake = models.ForeignKey(Intakes, on_delete=models.CASCADE)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    shift = models.CharField(max_length=50, choices= [("Day","day"), ("Evening", "evening")])
    is_class_cr = models.BooleanField(default=False)
    contact_number = models.PositiveIntegerField(null=True, blank=True)
    facebook_profile = models.CharField( max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Teacher(CommonProfileModel):
    name = models.CharField(max_length=350)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    is_intake_incharge = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    