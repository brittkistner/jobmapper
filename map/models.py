import json
import urllib
from django.db import models



class Company(models.Model):
    LICID = models.CharField(max_length=10, null=True)
    GDCID = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True) #change this to state field?
    zip_code = models.IntegerField(null=True)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    twitter = models.CharField(max_length=50, null=True)
    logo_url = models.URLField(null=True)
    description = models.TextField(null=True)
    company_type = models.CharField(max_length=75, null=True)
    tckr = models.CharField(max_length=10)
    founded_year = models.IntegerField()
    website_url = models.URLField(null=True)
    employee_count_range = models.CharField(max_length=255, null=True) #think about range here
    stock_exchange = models.CharField(max_length=4, null=True)
    num_followers = models.IntegerField(null=True)
    overall_rating = models.FloatField(null=True) #make sure to change these from string to float
    rating_description = models.CharField(max_length=50, null=True)
    culture_values_rating = models.FloatField(null=True)
    senior_leadership_rating = models.FloatField(null=True)
    compensation_benefits_rating = models.FloatField(null=True)
    career_opportunities_rating = models.FloatField(null=True)
    work_life_balance_rating = models.FloatField(null=True)
    number_ratings = models.IntegerField(null=True)
    industry = models.CharField(max_length=255, null=True) #there can be more than one
    # ceo = models.ForeignKey(CEO, related_name="company") #think about this

    def __unicode__(self):
            return u"{}".format(self.name)

#REVIEW THIS
    def geocode(self, location):
        location = urllib.quote_plus(location)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        data = json.loads(urllib.urlopen(request).read())

        if data['status'] == 'OK':
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            self.latitude = latitude
            self.longitude = longitude
            self.save()


# class Keyword(models.Model):
#     word = models.CharField(max_length=75)
#     companies = models.ManyToManyField(Company, related_name="keywords")
#
#     def __unicode__(self):
#         return u"{}".format(self.word)




#EXAMPLES

# class CEO(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.URLField()
#     number_ratings = models.IntegerField()
#     pct_approve = models.FloatField()
#     pct_disapprove = models.FloatField
#
#     def __unicode__(self):
#         return u"{}".format(self.name)

# class LinkedIn(models.Model):
#     LICID = models.CharField(max_length=10, primary_key=True)
#     name = models.CharField(max_length=255)
#     street_address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     zip_code = models.IntegerField()
#     latitude = models.DecimalField(max_digits=18, null=True, blank=True)
#     longitude = models.DecimalField(max_digits=18, null=True, blank=True)
#     twitter = models.CharField(max_length=15)
#     logo_url = models.URLField()
#     description = models.TextField()
#     company_type = models.CharField(max_length=75)
#     industry = models.CharField(max_length=255) #there can be more than one
#     #specialties (go in keywords, think about the keywords)
#     company_size = models.IntegerField()
#     tckr = models.CharField(max_length=10)
#     founded_year = models.IntegerField()
#     website_url = models.URLField()
#     employee_count_range = models.IntegerField()
#     stock_excahnge = models.CharField(max_length=4, null=True)
#
#     def __unicode__(self):
#         return u"LinkedIn: {}".format(self.name)
#

#

#
# class GlassDoor(models.Model):
#     GDCID = models.CharField(max_length=10, primary_key=True)
#     name = models.CharField(max_length=255)
#     overall_rating = models.FloatField() #make sure to change these from string to float
#     rating_description = models.CharField(max_length=50)
#     culture_values_rating = models.FloatField()
#     senior_leadership_rating = models.FloatField()
#     compensation_benefits_rating = models.FloatField()
#     career_opportunities_rating = models.FloatField()
#     work_life_balance_rating = models.FloatField()
#     website_url = models.URLField()
#     number_ratings = models.IntegerField()
#     logo_url = models.URLField()
#     ceo = models.ForeignKey(GlassDoorCEO, related_name="company")

#
#     def __unicode__(self):
#         return u"Glassdoor: {}".format(self.name)
# # through table?? for the Mapping Table
#