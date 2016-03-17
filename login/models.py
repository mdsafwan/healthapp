from __future__ import unicode_literals

from django.db import models

class patient_details(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Email = models.CharField(max_length=20, null=True, blank=True)
    Password = models.CharField(max_length=16, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        managed = True
        db_table = "patient_details"
        ordering = ['pk']
        verbose_name_plural = "patient_details"
        
class doctor_details(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Email = models.CharField(max_length=20, null=True, blank=True)
    Password = models.CharField(max_length=16, null=True, blank=True)
   
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        managed = True
        db_table = "doctor_details"
        ordering = ['pk']
        verbose_name_plural = "doctor_details"

class doc_prescription(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Age = models.CharField(max_length=20, null=True, blank=True)
    Email = models.CharField(max_length=20, null=True, blank=True)
    Number = models.IntegerField(null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Diagnosis = models.CharField(max_length=100, blank=True, null=True)
    Remedies = models.CharField(max_length=100, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % (self.Name)

    class Meta:
        managed = True
        db_table = "doc_prescription"
        ordering = ['pk']
        verbose_name_plural = "doc_prescriptions"
    
    