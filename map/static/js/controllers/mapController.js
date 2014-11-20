function mapController($scope, $http) {
    console.log('mapController');

    //Populates search form, industry input based on api query
    $http.get('/api/companies/get_industries')
        .success(function (industries) {
            $scope.industries = JSON.parse(industries);
        })
        .error(function (error) {
            console.log('error');
            console.log(error);
        });

    //Once the search form is submitted the data is queried DRF
    //Returns company queryset information given location (required) and keywords/industry
    $scope.searchCompany = function(placeName, keywords, industry) {
        console.log(encodeURIComponent(placeName));
        $http.get('/api/companies/get_companies_by_location/?location=' + encodeURIComponent(placeName) + (keywords ? '&keywords=' + encodeURIComponent(keywords) : '') + (industry ? '&industry=' + encodeURIComponent(industry.name) : ''))
            .success(function(combinedObject) {
                console.log('success');
                combinedObject = JSON.parse(combinedObject);
                var location = JSON.parse(combinedObject.location);
                var companies = combinedObject.companies;
                console.log(location);
                console.log(companies);
                $scope.companies = companies;
                $scope.location = location;
            })
            .error(function(error) {
                console.log('error');
            })
    };

}