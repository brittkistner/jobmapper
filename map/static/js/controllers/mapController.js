function mapController($scope, $http) {
    console.log('mapController');

    $http.get('/companies/get_industries')
        .success(function (industries) {
            console.log(industries);
//            $scope.industries = industries;
        })
        .error(function (error) {
            console.log('error');
            console.log(error);
        });

    $scope.searchCompany = function(placeName, keywords) {
        console.log(placeName);
        console.log(keywords);
        console.log(encodeURIComponent(placeName));
        $http.get('/companies/get_companies_by_location/?location=' + encodeURIComponent(placeName) + '&keywords=' + encodeURIComponent(keywords))
            .success(function(companies) {
                console.log('success');
                console.log(companies);
                $scope.companies = companies;
            })
            .error(function(error) {
                console.log('error');
//                console.log(error);
            })
    };

}