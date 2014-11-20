var jobmapper = angular.module('jobmapper', ['ngRoute','ngResource', 'ui.bootstrap','highcharts-ng']);

jobmapper.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/companies/:companyId', {
            templateUrl: '/static/js/views/company.html',
            controller: companyController
        }).
        when('/', {
            templateUrl: '/static/js/views/map.html',
            controller: mapController
        }).
        otherwise({redirectTo:'/'});
}]);