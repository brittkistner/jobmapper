function mapController($scope, $http) {
    console.log('mapController');

    $scope.searchCompany = function(placeName) {
        console.log(placeName);
        console.log(encodeURIComponent(placeName));
//        http://127.0.0.1:8000/companies/get_companies_by_location/?location=94104
        $http.get('/companies/get_companies_by_location/?location=' + encodeURIComponent(placeName))
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