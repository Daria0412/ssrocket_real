from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.CharField(db_column='id',primary_key=True,max_length=200,blank=False)
    name = models.CharField(db_column='name',max_length=200,blank=False)
    pwd = models.CharField(db_column='pwd',max_length=200,blank=False)
    info = models.IntegerField(db_column='info',blank=False)

    class Meta:
        managed = False
        db_table = 'user'

    def publish(self):
        self.save()

    def __str__(self):
        return self.id


class History(models.Model):
    history_num = models.AutoField(db_column='history_num',primary_key=True,blank=False)
    company_num = models.IntegerField(db_column='company_num',blank=False)
    member_id = models.CharField(db_column='member_id',max_length=200,blank=False)
    r_btime = models.DateTimeField(db_column='r_btime',blank=False)
    btime = models.DateTimeField(db_column='btime')
    r_rtime = models.DateTimeField(db_column='r_rtime',blank=False)
    rtime = models.DateTimeField(db_column='rtime')
    reserved_At = models.DateTimeField(db_column='reserved_At',blank=False)
    barcode = models.CharField(db_column='barcode',max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'history'

    def publish(self):
        self.save()

    def __str__(self):
        return self.member_id

class Course(models.Model):
    c_num = models.AutoField(db_column='c_num',primary_key=True,blank=False)
    c_name = models.CharField(db_column='c_name',max_length=200,blank=False)
    c_info = models.TextField(db_column='c_info',max_length=1000,blank=False)
    c_loc = models.CharField(db_column='c_loc',max_length=200,blank=False)
    c_theme = models.CharField(db_column='c_theme',max_length=200,blank=False)
    c_time = models.IntegerField(db_column='c_time')

    class Meta:
        managed = False
        db_table = 'course'

    def publish(self):
        self.save()

    def __str__(self):
        return self.c_name


class Company(models.Model):
    company_num = models.AutoField(db_column='company_num',primary_key=True)
    member_name = models.CharField(db_column='member_name',max_length=200)
    company_addr = models.CharField(db_column='company_addr',max_length=200)
    company_phone = models.CharField(db_column='company_phone',max_length=200)
    bicycle_num = models.IntegerField(db_column='bicycle_num')
    member_id = models.CharField(db_column='member_id',max_length=200)
    s_business = models.DateTimeField(db_column='s_business')
    e_business = models.DateTimeField(db_column='e_business')
    company_info = models.CharField(db_column='company_info',max_length=1000)
    company_loc = models.CharField(db_column='company_loc',max_length=200)
    rent_num = models.IntegerField(db_column='rent_num')

    class Meta:
        managed = False
        db_table = 'company'

    def publish(self):
        self.save()

    def __str__(self):
        return self.member_name

class Notice(models.Model):
    num = models.AutoField(db_column='num',primary_key=True)
    writer = models.CharField(db_column='writer',max_length=50)
    regdate = models.DateTimeField(db_column='regdate')
    subject = models.CharField(db_column='subject',max_length=200)
    content = models.CharField(db_column='content',max_length=1000)

    class Meta:
        managed = False
        db_table = 'notice_board'

    def publish(self):
        self.save()

    def __str__(self):
        return self.writer

class Counsel(models.Model):
    counsel_num = models.AutoField(db_column='counsel_num',primary_key=True,blank=False)
    member_id = models.CharField(db_column='member_id',max_length=50)
    regdate = models.DateTimeField(db_column='regdate')
    subject = models.CharField(db_column='subject',max_length=200)
    content = models.CharField(db_column='content',max_length=1000)
    category = models.IntegerField(db_column='category')

    class Meta:
        managed = False
        db_table = 'counsel'

    def publish(self):
        self.save()

    def __str__(self):
        return self.member_id

    
class Refer(models.Model):
    counsel_num = models.IntegerField(db_column='counsel_num',primary_key=True)
    regdate = models.DateTimeField(db_column='regdate')
    content = models.CharField(db_column='content',max_length=1000)
    refer_admin = models.CharField(db_column='refer_admin',max_length=50)  

    class Meta:
        managed = False
        db_table = 'refer'

    def publish(self):
        self.save()

    def __str__(self):
        return self.writer