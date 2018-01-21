from django.db import models
from django.conf import settings


class Feature(models.Model):
    """
    define Feature
    """
    name = models.CharField('FeatureName', max_length=500)
    # author = models.ManytoManyField(User)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=' FeatureAuthor', on_delete=models.CASCADE)
    content = models.TextField('FeatureContent', default='')
    create_time = models.DateTimeField('FeatureCreateTime', auto_now_add=True)
    last_modified_time = models.DateTimeField('FeatureLastModify', auto_now_add=True)
    time_box = models.FloatField('FeatureTimeBox', default=0)
    material = models.FileField('FeatureMaterial', upload_to='Features/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    define Item
    """
    name = models.CharField('ItemName', max_length=500)
    content = models.TextField('ItemContent', default='')
    create_time = models.DateTimeField('ItemCreateTime', auto_now_add=True)
    last_modified_time = models.DateTimeField('ItemLastModify', auto_now_add=True)
    time_box = models.FloatField('ItemTimeBox', default=0)
    feature = models.ForeignKey(Feature, blank=True, null=True, verbose_name='Feature', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Grooming(models.Model):
    """
    Grooming modes
    """

    title = models.CharField('Title', max_length=200)
    # content = models.TextField('ATDD Case',default = '')
    sprint = models.CharField('Sprint', max_length=200, default='Sprint-')
    scope = models.TextField('Scope', default='')
    question = models.TextField('Question', default='')
    assumption = models.TextField('Assumption', default='')
    create_time = models.DateTimeField('CreateTime', auto_now_add=True)
    last_modified_time = models.DateTimeField('ModifyTime', auto_now_add=True)
    attend_person = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='AttednPerson')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='GroomingAuthor', on_delete = models.CASCADE)
    sw_cost_time = models.FloatField('SWCostTime', default=0)
    iv_cost_time = models.FloatField('I&VCostTime', default=0)
    item = models.ForeignKey(Item, verbose_name='Item', null=True, blank=True, on_delete=models.CASCADE)
    phase = models.IntegerField('GroomingPhase', default=1)

    def __str__(self):
        return self.title


class ATDDCase(models.Model):
    """
    ATDDCase models
    """
    suitename = models.CharField('Suitename', max_length=200, default='')
    grooming = models.ForeignKey(Grooming, null=True, verbose_name='Grooming', blank=True, on_delete=models.CASCADE)
    case_file = models.FilePathField('CaseFile', default='')
    case_content = models.TextField('CaseContent', default='')
    #testname = models.TextField('Testname', default='')
    #precondition = models.TextField('Precondition', default='')
    #operation = models.TextField('Operation', default='')
    #expectresult = models.TextField('Expect Result', default='')
    #checkpoint = models.TextField('Check Point', default='')
    #grooming_belong_to = models.ForeignKey('Grooming', blank=True, null=True)

    def __str__(self):
        return self.suitename


# class User(models.Model):
#   """
#    define users
#    """
#    name = models.CharField('UserName', max_length=200)
#    user_group = models.ForignKey(UserGroup)
#    email = models.EmailField('UserEmail',max_length=254)
#    password = models.CharField('UserPasswd', max_length=200)


# class UserGroup(models.Model):
#   """
#    define the user group
#    """
#    name = models.CharField('UserGroupName', max_length=300)



# class Tag(models.Model):
#    """
#    """
#
#    name = models.CharField('TagName', max_length = 50)
#    create_time = models.DateTimeField('Tagcreatetime', auto_now_add = True)
#    last_modified_time = models.DateTimeField('Tagmodifytime', auto_now_add = True)

#    def __str__(self):
#        return self.name

#    class Meta:
#        ordering = ['name']
#        verbose_name = "Tag"
#        verbose_name_plural = verbose_name
