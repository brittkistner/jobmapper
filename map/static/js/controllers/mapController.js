function mapController($scope, $http) {
    console.log('mapController');
    $http.get('/api/companies/get_industries')
        .success(function (industries) {
            $scope.industries = JSON.parse(industries);
        })
        .error(function (error) {
            console.log('error');
            console.log(error);
        });

    $scope.searchCompany = function(placeName, keywords, industry) {
        console.log(placeName);
        console.log(keywords);
        console.log(industry.name);
        console.log(encodeURIComponent(placeName));
        $http.get('/api/companies/get_companies_by_location/?location=' + encodeURIComponent(placeName) + '&keywords=' + encodeURIComponent(keywords) + '&industry=' + encodeURIComponent(industry.name))
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