function companyController($scope, $http, $routeParams) {
    console.log('companyController');
    $scope.companyId = $routeParams.companyId;
    console.log($scope.companyId);

    $http.get('/companies/' + $scope.companyId)
        .success(function (company) {
            console.log(company);
            $scope.company = company;
            $scope.overallRating = Math.floor(100 * (company.overall_rating/5.0)) + "%";
        })
        .error(function (error) {
            console.log('error');
            console.log(error);
        });


}