import os.path
import uuid

from django.db import models


# Create your models here.
def generate_unique_name(instance, filename):
    name = uuid.uuid4()  # universally unique id  pic.kenya.png ["kenya", "png"]
    ext = filename.split(".")[-1]
    full_filename = f"{name}.{ext}"
    # full_filename = "%s.%s" % (name, ext)
    return os.path.join("students", full_filename)  # students/100/xyz.png


class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # 100.500
    is_sporty = models.BooleanField(default=False)
    kcpe_score = models.IntegerField()
    profile_pic = models.ImageField(upload_to=generate_unique_name, null=True, default="students/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

# pip install Pillow
# pip install mysqlclient  --- refuses
# pip install pymysql  --> pymysql.install_as_MySQLdb()
