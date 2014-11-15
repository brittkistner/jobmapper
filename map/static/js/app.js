var jobmapper = angular.module('jobmapper', ['ngRoute','ngResource', 'ui.bootstrap']);

jobmapper.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        }).
        when('/companies/:companyId', {
            templateUrl: '/static/js/views/company.html',
            controller: companyController
        }).
        when('/map', {
            templateUrl: '/static/js/views/map.html',
            controller: mapController
        }).
        otherwise({redirectTo:'/'});
}]);