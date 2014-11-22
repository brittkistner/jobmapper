from linkedin import linkedin

# Is this utils file being used? Usually setting global python variables like this is not best practice.
# Some libraries are poorly written though and require you to do this
from linkedin import linkedin
RETURN_URL = 'http://localhost:8000'
CONSUMER_KEY = '75b51aiefo2ejs'
CONSUMER_SECRET = 'UglJ7XHGfDUNQRYO'
USER_TOKEN = 'a04073e0-7f0d-4b76-9fd1-37baa649945b'
USER_SECRET = '2f2c65a2-b28e-4f7d-b204-1515d861b61d'

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,
                                                          USER_TOKEN, USER_SECRET,
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())

application = linkedin.LinkedInApplication(authentication)

# long line that should be split up
li_companies_results = application.search_company(selectors=[{'companies':['name', 'id', 'website-url', 'type']}],params={ 'facets':'location','facet':'location,us:84','keywords':'technology','count':10})
#do a json.dumps to get it into python

#for each of the company ids
