import json
import urllib
from django.db import models



class Company(models.Model):
    assigned_key = models.IntegerField(primary_key=True)
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
    overall_rating = models.FloatField(null=True)
    rating_description = models.CharField(max_length=50, null=True)
    culture_values_rating = models.FloatField(null=True)
    senior_leadership_rating = models.FloatField(null=True)
    compensation_benefits_rating = models.FloatField(null=True)
    career_opportunities_rating = models.FloatField(null=True)
    work_life_balance_rating = models.FloatField(null=True)
    number_ratings = models.IntegerField(null=True)
    industry = models.CharField(max_length=255, null=True)
    # ceo = models.CharField(max_length=255, null=True)
    # ceo_image = models.URLField(null=True),
    # ceo_num_rating = models.IntegerField(null=True),
    # ceo_pct_approve = models.FloatField(null=True),
    # ceo_pct_disapprove = models.FloatField(null=True)


    def __unicode__(self):
            return u"{}".format(self.name)

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


class Keyword(models.Model):
    company = models.ForeignKey(Company, related_name="keywords")
    word = models.CharField(max_length=75)

    def __unicode__(self):
        return u"{}".format(self.word)

