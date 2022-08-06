from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# User Profile Model

class Profile(models.Model):
    userLinked = models.ForeignKey(User,related_name='userProfile',on_delete=models.CASCADE)
    mobile_num_regex  = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!") # Regex Validator to validate user phone number
    mobile_number  = models.CharField(validators=[mobile_num_regex], max_length=13,unique=True)
    userPhoto = models.ImageField(upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.userLinked.username} - profile'
