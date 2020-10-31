from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
# class Student_profile(models.Model):
#      name = models.CharField('Name',max_length=20)
#      s_class = models.IntegerField('Class',help_text='Enter which class you are in ( ex:10 )')
#      choices_lang = (
#          ('H', 'Hindi'),
#          ('E', 'English'),
#          ('T', 'Telugu'),)
#      lang = models.CharField('Language',max_length=1, choices=choices_lang, blank=True, default='E',help_text='Enter the language')
#
#      def __str__ (self):
#          return self.name

# Create your models here.
class teach_prof(models.Model):
    name = models.CharField('Name',max_length=20)
    teach_class = models.IntegerField('Teach Upto',help_text='Enter upto which class you can teach ( ex:10 )')
    choices_lang = (
        ('H', 'Hindi'),
        ('E', 'English'),
        ('T', 'Telugu'),)
    lang = models.CharField('Language',max_length=1, choices=choices_lang, blank=True, default='E',help_text='Enter the language')
    Qualify = models.CharField('Qualification',max_length=50, help_text='Enter your highest qualification')
    Subj = models.CharField('Subject',max_length=20, null=True)
    city = models.CharField('City',max_length=20)
    state = models.CharField('State',max_length=20)
    Email = models.EmailField(max_length = 200, default='null')
    contact = models.DecimalField('Contact', max_digits=10, decimal_places=0)

    user = models.ForeignKey(get_user_model(),null=True, on_delete=models.CASCADE)

    def __str__ (self):
        return f'{self.name} {self.Subj} {self.city} {self.state}'
#
# class notifications(models.Model):
#     teacher = models.ForeignKey(teach_prof, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student_profile, on_delete=models.CASCADE)
#     message = models.CharField(max_length=50)
