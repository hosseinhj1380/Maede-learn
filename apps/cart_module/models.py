from django.db import models
from apps.course_module.models import Course
from apps.user_module.models import User

class Cart (models.Model):
    user = models.ForeignKey(User,default=0,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,default=0, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.course.name} added to cart by {self.user.email}"

    def get_total_price(self):
        return self.quantity * self.course.price
