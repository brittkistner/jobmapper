//Big donut for overall rating
jobmapper.directive('donutChart', function() {
    function link($scope, element, attr){
        $scope.$watch('data', function(data){
          if (data === undefined){
              return false;
          }else{
              console.log("an element within `data` changed!");
              console.log("bottom data " + data);
                var width = 300;
                    height = 300;
                    τ = 2* Math.PI; // http://tauday.com/tau-manifesto
    //            var data = $scope.data;
                var arcValue = ((data/5) * (0.7 * τ)) - 0.35 * τ;
                console.log("arcValue is " + arcValue);

                var arc = d3.svg.arc()
                    .innerRadius(110)
                    .outerRadius(150)
                    .startAngle(-.35 * τ);

                var svg = d3.select(element[0]).append("svg")
                    .attr("width", width)
                    .attr("height", height)
                  .append("g")
                    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

                var icon = svg.append("text")
                  .attr('font-family', 'FontAwesome')
                  .attr('font-size', '18em')
                  .attr("transform", "translate(-108,90)")
                  .text("\uf118");

                var background = svg.append("path")
                    .datum({endAngle:.35 * τ})
                    .style("fill", "#ddd")
                    .attr("d", arc);

                var foreground = svg.append("path")
                    .datum({endAngle: -.35 * τ})
        //            .datum({endAngle: 0})
                    .style("fill", "#D0743C")
                    .attr("d", arc);

                setInterval(function() {
                  foreground.transition()
                      .duration(750)
                      .call(arcTween, arcValue); //i will set
                }, 1500);

                function arcTween(transition, newAngle) {

                  transition.attrTween("d", function(d) {
                    var interpolate = d3.interpolate(d.endAngle, newAngle);
                    return function(t) {
                      d.endAngle = interpolate(t);
                      return arc(d);
                    };
                  });
                }
            }
        }, true);
    }
    return {
        link: link,
        restrict: 'E',
        scope: { data: '=' }
    }
});

//Small donut for rating breakdown
jobmapper.directive('smallDonutChart', function() {
    function link(scope, element, attr){
        scope.$watch('data', function(data){
            if (data[0] === undefined){
              return false;
            }else {
                var width = 150;
                height = 150;
                τ = 2 * Math.PI; // http://tauday.com/tau-manifesto
                var data = scope.data[0];
                var fontIcon = scope.data[1];
                var arcValue = ((data / 5) * (0.7 * τ)) - 0.35 * τ;
                console.log("arcValue is " + arcValue);

                var arc = d3.svg.arc()
                    .innerRadius(50)
                    .outerRadius(75)
                    .startAngle(-.35 * τ);

                var svg = d3.select(element[0]).append("svg")
                    .attr("width", width)
                    .attr("height", height)
                    .append("g")
                    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

                var icon = svg.append("text")
                  .attr('font-family', 'FontAwesome')
                  .attr('font-size', '4em')
                  .attr("transform", "translate(-28,13)")
                  .text(fontIcon);

                var background = svg.append("path")
                    .datum({endAngle: .35 * τ})
                    .style("fill", "#ddd")
                    .attr("d", arc);

                var foreground = svg.append("path")
                    .datum({endAngle: -.35 * τ})
                    .style("fill", "#7b6888")
                    .attr("d", arc);

                setInterval(function () {
                    foreground.transition()
                        .duration(750)
                        .call(arcTween, arcValue); //i will set
                }, 1500);

                function arcTween(transition, newAngle) {

                    transition.attrTween("d", function (d) {
                        var interpolate = d3.interpolate(d.endAngle, newAngle);
                        return function (t) {
                            d.endAngle = interpolate(t);
                            return arc(d);
                        };
                    });
                }
            }

        }, true);
    }
    return {
        link: link,
        restrict: 'E',
        scope: { data: '=' }
    }
});

jobmapper.directive('barChart', function() {
    function link(scope, element, attr){
//        var data = [500, 3000];
        scope.$watch('data', function(data){
            if (typeof(data[0]) === "undefined" && typeof(data[1]) === "number" ||
                typeof(data[0]) === "number" && typeof(data[1]) === "undefined"){
                console.log("data length " + data.length);
              return false;
            }else {
              console.log("data points" + data);
                var width = 420,
                    barHeight = 60;

                var x = d3.scale.linear()
                    .domain([0, d3.max(data)])
                    .range([0, width]);

                var chart = d3.select(element[0]).append("svg")
                    .attr("width", width)
                    .attr("height", barHeight * data.length);

                var bar = chart.selectAll("g")
                    .data(data)
                    .enter().append("g")
                    .attr("transform", function (d, i) {
                        return "translate(0," + i * barHeight + ")";
                    });

                var rect = bar.append("rect");
                rect.attr("width", 0)
                    .transition().duration(1000).attr("width", x)
                    .attr("height", barHeight - 1);

                    bar.append("text")
                        .attr("x", function (d) {
                            console.log('this is d ' + d);
                            return x(d) - 10;
                        })
                        .attr("y", barHeight / 2)
                        .attr("dy", ".35em")
                        .attr('font-size', '2em')
                        .text(function (d) {
                            return name + 'rating: ' + d;
                        });
            }

        }, true);
    }
    return {
        link: link,
        restrict: 'E',
        scope: { data: '=' }
    }
});


//Double Radial Chart for Comparison Rating
//jobmapper.directive('doubleRadius', function() {
//    function link(scope, element, attr){
//    // reference for transition http://jsfiddle.net/Nw62g/1/
//        //original reference http://jsfiddle.net/Qh9X5/154/
//
//        var data = [300,400];
//
//        var width = 460,
//            height = 300,
//            gap = 30;
//
////        var color = d3.scale.category20();
//
////        var pie = d3.layout.pie()
////            .sort(null);
//
//        var arc = d3.svg.arc()
//            .startAngle(-.35 * τ);
////        var arc = d3.svg.arc()
////            .innerRadius(50)
////            .outerRadius(75)
////            .startAngle(-.35 * τ);
//
//        var svg = d3.select(element[0]).append("svg")
//            .attr("width", width)
//            .attr("height", height)
//            .append("g")
//            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");
//
//        var gs = svg.selectAll("g").data(d3.values(dataset)).enter().append("g");
//        var path = gs.selectAll("path")
//            .data(function(d) { return arc(d); })
//          .enter().append("path")
//            .attr("fill", function(d, i) { return color(i); })
//            .attr("d", function(d, i, j) { return arc.innerRadius(10+gap*j).outerRadius(gap*(j+1))(d); });
//
//        setInterval(function() {
//          foreground.transition()
//              .duration(750)
//              .call(arcTween, arcValue); //i will set
//        }, 1500);
//
//        function arcTween(transition, newAngle) {
//
//          transition.attrTween("d", function(d) {
//            var interpolate = d3.interpolate(d.endAngle, newAngle);
//            return function(t) {
//              d.endAngle = interpolate(t);
//              return arc(d);
//            };
//          });
//        }
//
////var width = 150;
////            height = 150;
////            τ = 2* Math.PI; // http://tauday.com/tau-manifesto
////        var data = scope.data;
////        var arcValue = ((data/5) * (0.7 * τ)) - 0.35 * τ;
////        console.log("arcValue is " + arcValue);
////
////        var arc = d3.svg.arc()
////            .innerRadius(50)
////            .outerRadius(75)
////            .startAngle(-.35 * τ);
////
////        var svg = d3.select(element[0]).append("svg")
////            .attr("width", width)
////            .attr("height", height)
////          .append("g")
////            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");
////
////        var background = svg.append("path")
////            .datum({endAngle:.35 * τ})
////            .style("fill", "#ddd")
////            .attr("d", arc);
////
////        var foreground = svg.append("path")
////            .datum({endAngle: -.35 * τ})
////            .style("fill", "#7b6888")
////            .attr("d", arc);
////        setInterval(function() {
////          foreground.transition()
////              .duration(750)
////              .call(arcTween, arcValue); //i will set
////        }, 1500);
////
////        function arcTween(transition, newAngle) {
////
////          transition.attrTween("d", function(d) {
////            var interpolate = d3.interpolate(d.endAngle, newAngle);
////            return function(t) {
////              d.endAngle = interpolate(t);
////              return arc(d);
////            };
////          });
////        }
//
//        scope.$watch('data', function(data){
////          console.log("an element within `data` changed!");
////          console.log("bottom data " + data);
//        }, true);
//    }
//    return {
//        link: link,
//        restrict: 'E',
//        scope: { data: '=' }
//    }
//});