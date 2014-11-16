function mapController($scope, $http) {
    console.log('mapController');

    $scope.searchCompany = function(placeName) {
        console.log(placeName);
        console.log(encodeURIComponent(placeName));
        $http.get('/companies?location=' + encodeURIComponent(placeName))
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