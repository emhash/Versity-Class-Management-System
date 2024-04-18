import django_filters as df
from users.models import Student


class StudentFilter(df.FilterSet):
    name = df.CharFilter(label="Name",lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['name', 'intake','section' ,'department', 'shift']
