from numbers import Number
from django.core.management import BaseCommand
from map.models import Company, Keyword
import csv
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        module_dir = os.path.dirname(__file__)  # get current directory
        company_file_path = os.path.join(module_dir, 'csv_company.csv')
        with open(company_file_path, 'rb') as company_file:
            for row in csv.reader(company_file):
                # Probably would of been easier in development and production to make this more of a `get_or_create`
                # based on assigned_key, which looks like your unique way of identifying the companies.
                company = Company.objects.create(  assigned_key = int(row[0]),
                                                   LICID=int(row[1]),
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
                                                   industry=row[27].lower(),
                                                   ceo=row[28],
                                                   ceo_image=row[29],
                                                   ceo_num_rating=row[30],
                                                   ceo_pct_approve=int(row[31]),
                                                   ceo_pct_disapprove=int(row[32])
                )

                company.geocode(row[8])
                company.save()
                print company

        keyword_file_path = os.path.join(module_dir, 'csv_keyword.csv')
        with open(keyword_file_path, 'rb') as keyword_file:
            for row in csv.reader(keyword_file):
                # since assigned_key is your priamry key field, you should be able to just say pk=row[0]
                company = Company.objects.get(assigned_key=row[0])
                keyword = Keyword.objects.create(company=company,
                                       word=row[1])
                keyword.save()


