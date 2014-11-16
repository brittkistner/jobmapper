function mapController($scope, $http) {
    console.log('mapController');

    $scope.searchCompany = function(placeName) {
        console.log(placeName);
        console.log(encodeURIComponent(placeName));
        $http.get('/companies?location=' + encodeURIComponent(placeName))
            .success(function(response) {
                console.log('success');
                console.log(response);
            })
            .error(function(error) {
                console.log('error');
//                console.log(error);
            })
    };

}