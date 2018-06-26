from django.db import models
from django.utils import timezone

# Create your models here.
class Friend(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    phon_number_1= models.CharField(max_length=20)
    phon_number_2= models.CharField(max_length=20, blank=True, null=True)
    e_mail = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now())
    approved_friend = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def approve(self):
        self.approved_friend = True
        self.save()

    class Meta:
        ordering = ('name',)




class Memo(models.Model):
    Friend = models.ForeignKey('addr.Friend', related_name='memo')
    text = models.TextField()
    approved_memo = models.BooleanField(default=False)


    def approve(self):
        self.approved_memo = True
        self.save()

    def __str__(self):
        return self.text