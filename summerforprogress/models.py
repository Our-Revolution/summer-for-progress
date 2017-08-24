from django.db import models
from localflavor.us.models import USStateField

class Representative(models.Model):
    ''' Model representing a U.S. Representative '''

    first = models.CharField(default='', max_length=64, null=False, blank=False)
    last = models.CharField(default='', max_length=64, null=False, blank=False)
    state = USStateField(default='',null=False, blank=False)
    district = models.CharField(default='', max_length=64,null=False, blank=False)
    party = models.CharField(default='', max_length=1, blank=True)
    healthcare = models.NullBooleanField(null=True,blank=True)
    college_tuition = models.NullBooleanField(null=True,blank=True)
    minimum_wage = models.NullBooleanField(null=True,blank=True)
    wall_street = models.NullBooleanField(null=True,blank=True)
    womens_rights = models.NullBooleanField(null=True,blank=True)
    voting_rights = models.NullBooleanField(null=True,blank=True)
    justice = models.NullBooleanField(null=True,blank=True)
    climate = models.NullBooleanField(null=True,blank=True)
    score = models.FloatField(default=0,null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
        
    def save(self, *args, **kwargs):   
        NUM_BILLS = 8 
        score = 0        
        
        if self.healthcare:
            score += 1
            
        if self.college_tuition:
            score += 1
            
        if self.minimum_wage:
            score += 1
            
        if self.wall_street:
            score += 1
            
        if self.womens_rights:
            score += 1
            
        if self.voting_rights:
            score += 1
            
        if self.justice:
            score += 1
        
        if self.climate:
            score += 1
            
        score = (float(score) / NUM_BILLS) * 100

        self.score = score
        
        super(Representative, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.first + ' ' + self.last + ' - ' + self.state + ' ' + self.district 
