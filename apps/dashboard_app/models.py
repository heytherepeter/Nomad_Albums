from django.db import models
from datetime import datetime, timedelta
import re

def logThis(*arg):
	print("="*50)
	print('')
	print(*arg)
	print('')
	print("="*50)


# class form validations
class UserManager(models.Manager):
	def login_validator(self, postData):
		errors = {}
		emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if not emailRegex.match(postData['form_login_email']):
			errors['form_reg_email'] = "Please enter a valid email"
		return errors

	def user_validator(self, postData):
		age_min = datetime.now() - timedelta(days=365*13)
		dateRegex = re.compile("^(1|2)[0-9]{3}-(0|1)[0-9]-[0-3][0-9]$")
		emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors = {}
		if len(postData['form_reg_first_name']) < 2:
			errors["form_reg_first_name"] = "First name should be at least 2 characters"
		if len(postData['form_reg_last_name']) < 2:
			errors["form_reg_last_name"] = "Last name should be at least 2 characters"
		if not emailRegex.match(postData['form_reg_email']):
			errors['form_reg_email'] = "Please enter a valid email"
		if len(postData['form_reg_password']) < 8:
			errors["form_reg_password"] = "Password should be at least 8 characters"
			if postData['form_reg_password'] != postData['form_reg_pass_confirm']:
				errors["form_reg_pass_confirm"] = "Passwords do not match"
		return errors

# class AlbumManager(models.Manager):
# 	def job_validator(self, postData):
# 		errors = {}
# 		if len(postData['form_job_title']) < 3:
# 			errors["form_job_title"] = "Title should be at least 3 characters"
# 		if len(postData['form_job_description']) < 10:
# 			errors["form_job_description"] = "Description should be at least 10 characters"
# 		if len(postData['form_job_location']) < 1:
# 			errors["form_job_location"] = "Location cannot be blank"
# 		return errors

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	password_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	def __str__(self):
		return f"id:{self.id} email:{self.email}"

class Album(models.Model):
	title = models.CharField(max_length=45)
	description = models.TextField()
	location = models.CharField(max_length=255)
	# owner = models.ForeignKey(User, related_name="user_albums")
	users = models.ManyToManyField(User, related_name="albums")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# objects = AlbumManager()
	def __str__(self):
		return f"album id:{self.id}"
