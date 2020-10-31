from django.forms import ModelForm
from manager.models import Person


class RegisterForm(ModelForm):
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

    class Meta:
        model = Person
        fields = ['name', 'teach_class', 'lang', 'Subj', 'city', 'state','Email','contact']
