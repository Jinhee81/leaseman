from django.db import models

# Create your models here.
class Users(models.Model) :
    USR_DIV_PS = 'usr_div_ps'
    USR_DIV_PSCORP = 'usr_div_pscorp'
    USR_DIV_CORP = 'usr_div_corp'
    USER_DIV = (
        (USR_DIV_PS, 'usr_div_ps'),
        (USR_DIV_PSCORP, 'usr_div_pscorp'),
        (USR_DIV_CORP, 'usr_div_corp')
    )

    REG_MAIL = 'reg_mail'
    REG_SMS = 'reg_sms'
    REG_PERSON = 'reg_person'
    REG_INTERNET = 'reg_internet'
    REG_ETC = 'reg_etc'
    REG_CHANNEL = (
        (REG_MAIL, 'reg_mail'),
        (REG_SMS, 'reg_sms'),
        (REG_PERSON, 'reg_person'),
        (REG_INTERNET, 'reg_internet'),
        (REG_ETC, 'reg_etc')
        )

    # id = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    cellphone = models.IntegerField()
    content = models.TextField()
    user_div = models.CharField(
        max_length = 3,
        choices = USER_DIV
    )
    reg_channel = models.CharField(
        max_length = 5,
        choices = REG_CHANNEL
    )

    def __str__(self):
        return self.id, self.username

class etc(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
