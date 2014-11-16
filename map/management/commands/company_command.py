from numbers import Number
from django.core.management import BaseCommand
from map.models import Company
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        print 'hello'
        with open('/Users/bkistner/Desktop/RocketU/projects/jobmapper/map/management/commands/csv_company.csv', 'rb') as file:
            for row in csv.reader(file):
                company = Company.objects.create(LICID=int(row[1]),
                                                   GDCID=int(row[2]),
                                                   name=row[3],
                                                   street_address=row[4],
                                                   city=row[5],
                                                   state=row[6],
                                                   zip_code=int(row[7]),
                                                   address=row[8],
                                                   twitter=row[9],
                                                   logo_url=row[10],
                                                   description=row[11],
                                                   company_type=row[12],
                                                   tckr=row[13],
                                                   founded_year=int(row[14]),
                                                   website_url=row[15],
                                                   employee_count_range= row[16],
                                                   stock_exchange=row[17],
                                                   num_followers=int(row[18]),
                                                   overall_rating=float(row[19]),
                                                   rating_description=row[20],
                                                   culture_values_rating=float(row[21]),
                                                   senior_leadership_rating=float(row[22]),
                                                   compensation_benefits_rating=float(row[23]),
                                                   career_opportunities_rating=float(row[24]),
                                                   work_life_balance_rating=float(row[25]),
                                                   number_ratings=int(row[26]),
                                                   industry=row[27])
                                                   # ceo=row[28],
                                                   # ceo_image=row[29],
                                                   # ceo_num_rating=row[30],
                                                   # ceo_pct_approve=row[31],
                                                   # ceo_pct_disapprove=row[32])

                company.geocode(row[8])
                company.save()


                # Keyword.objects.create(CID=company__pk=id, word=row[])
