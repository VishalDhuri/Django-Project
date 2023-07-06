from django.db import models

# Create your models here.
class userr(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    useraddress = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class fooditem(models.Model):
    foodname = models.CharField(max_length=100,primary_key=True)
    foodprice = models.IntegerField()

    def __str__(self):
        return self.foodname

class Review(models.Model):
    food = models.ForeignKey(fooditem,on_delete=models.CASCADE)
    reviewername = models.ForeignKey(userr,on_delete=models.CASCADE)
    rating = models.IntegerField(help_text="enter rating between 1 to 5")
