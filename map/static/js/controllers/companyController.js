function companyController($scope, $http, $routeParams ) {
    console.log('companyController');
    $scope.companyId = $routeParams.companyId;
//    console.log($scope.companyId);

    $http.get('/api/companies/' + $scope.companyId)
        .success(function (company) {
            console.log(company);
            $scope.company = company;
            $scope.overallRating = Math.floor(100 * (company.overall_rating/5.0)) + "%";
            if($scope.company.tckr){
                //Call Quandl api for stock data
                getStockData($scope.company.tckr);
                console.log('tckr ' + $scope.company.tckr);
            }else{
                console.log('no tckr')
            }

        })
        .error(function (error) {
            console.log('error');
            console.log(error);
        });

    $http.get('/api/companies/get_average_num_followers')
        .success(function (avg_num_followers) {
            console.log(avg_num_followers);
            $scope.avg_num_followers = JSON.parse(avg_num_followers);
        })
        .error(function (error) {
            console.log('error');
            console.log(error);
        });

    //STOCK DATA
    var getStockData = function(tckr) {
//        $.getJSON('https://www.quandl.com/api/v1/datasets/WIKI/' + $scope.company.tckr + '.json')
        $.getJSON('https://www.quandl.com/api/v1/datasets/WIKI/TWTR.json')
            .done(function(stockData) {
                console.log('retrieving stock data');
                console.log(stockData.data);
    //            stockData returned as this:
    //                "column_names": [
    //                "Date",
    //                "Open",
    //                "High",
    //                "Low",
    //                "Close",
    //                "Volume",
    //                "Ex-Dividend",
    //                "Split Ratio",
    //                "Adj. Open",
    //                "Adj. High",
    //                "Adj. Low",
    //                "Adj. Close",
    //                "Adj. Volume"
    //                ],
                var dataset = [];
                for (var i=0; i < stockData.data.length; i++ ){
                    //convert data to milliseconds
                    var dashdates = stockData.data[i][0]; //2013-07-01
                    var milliseconds = Date.parse(dashdates);
                    var open = stockData.data[i][1];
                    dataArray = [milliseconds,open];
                    dataset.push(dataArray);
                    event.preventDefault();
                }
                console.log('dataset');
                console.log(dataset[0]);
              //create chart
//                chart_maker(dataset);
//                console.log($scope.chartSeries);
            })
            .error(function(error) {
                console.log('error');
                console.log(error);
            });
    };


    //HIGHSTOCK BELOW

//    var chart_maker = function(data){
//        console.log('data now in chart maker');
//        console.log(data);
//        console.log(data[0]);
        $scope.chartTypes = [
            {"id": "line", "title": "Line"},
            {"id": "spline", "title": "Smooth line"},
            {"id": "area", "title": "Area"},
            {"id": "areaspline", "title": "Smooth area"},
            {"id": "column", "title": "Column"},
            {"id": "bar", "title": "Bar"},
            {"id": "pie", "title": "Pie"},
            {"id": "scatter", "title": "Scatter"}
        ];

        $scope.dashStyles = [
        {"id": "Solid", "title": "Solid"},
        {"id": "ShortDash", "title": "ShortDash"},
        {"id": "ShortDot", "title": "ShortDot"},
        {"id": "ShortDashDot", "title": "ShortDashDot"},
        {"id": "ShortDashDotDot", "title": "ShortDashDotDot"},
        {"id": "Dot", "title": "Dot"},
        {"id": "Dash", "title": "Dash"},
        {"id": "LongDash", "title": "LongDash"},
        {"id": "DashDot", "title": "DashDot"},
        {"id": "LongDashDot", "title": "LongDashDot"},
        {"id": "LongDashDotDot", "title": "LongDashDotDot"}
        ];

        $scope.chartSeries = [
      {"name": "TCKR",
       "data": [[1143072000000,60.16],
                [1143158400000,59.96],
                [1143417600000,59.51]],
       tooltip: {
          valueDecimals: 4}
      }];
//        $scope.updateChartData = function() {
//            var updatedData  = $scope.chartSeries[0].data;
//            console.log('update data ' + data);
//            $scope.chartConfig.series[0].data = updatedData.concat(data);
//        };
        $scope.chartStack = [
        {"id": '', "title": "No"},
        {"id": "normal", "title": "Normal"},
        {"id": "percent", "title": "Percent"}
        ];


        $scope.chartConfig = {
            options: {
              chart: {
                type: 'line'
              },
              plotOptions: {
                series: {
                  stacking: ''
                }
              }
            },
            title: {
              text: 'Stock Price'
            },
            series: $scope.chartSeries,
            credits: {
              enabled: false
            },
            loading: false,
            size: {}
        };
//        $scope.updateChartData();



        $scope.reflow = function () {
            $scope.$broadcast('highchartsng.reflow');
        };
//    }


}