//Big donut for overall rating
jobmapper.directive('donutChart', function() {
    function link($scope, element, attr){
        $scope.$watch('data', function(data){
          if (data === undefined){
              return false;
          }else{
                var width = 300;
                    height = 300;
                    τ = 2* Math.PI; // http://tauday.com/tau-manifesto
                var arcValue = ((data/5) * (0.7 * τ)) - 0.35 * τ;

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
                  .attr('font-size', '12em')
                  .attr("transform", "translate(-72,55)")
                  .text("\uf118");

              var rating = svg.append("text")
                  .attr('font-family', 'Raleway')
                  .attr('font-size', '2.5em')
                  .attr("transform", "translate(-25,140)")
                  .text(data); //insert data

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
                      .call(arcTween, arcValue);
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

                var rating = svg.append("text")
                  .attr('font-family', 'Raleway')
                  .attr('font-size', '2em')
                  .attr("transform", "translate(-15,55)")
                  .text(data); //insert data

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
        scope.$watch('data', function(data){
            if (typeof(data[0].value) === "undefined" && typeof(data[1].value) === "undefined" ||
                typeof(data[0].value) === "undefined" && typeof(data[1].value) === "number" ||
                typeof(data[0].value) === "number" && typeof(data[1].value) === "undefined"){
              return false;
            }else {
              var dValues =[];
              for (var i=0; i < 2; i++){
                  dValues.push(data[i].value);
                }
                var width = 420,
                    barHeight = 60;

                var x = d3.scale.linear()
                    .domain([0, d3.max(dValues)])
                    .range([0, width]);

                var chart = d3.select(element[0]).append("svg")
                    .attr("width", width)
                    .attr("height", barHeight * dValues.length);
                var bar = chart.selectAll("g")
                    .data(dValues)
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
                            return x(d) - 10;
                        })
                        .attr("y", barHeight / 2)
                        .attr("dy", ".35em")
                        .attr('font-size', '1.2em')
                        .text(function (d,i) {
                            return data[i].name + ' : ' + d;
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

//Approval Chart
jobmapper.directive('approvalRating',function(){
    function link(scope, element, attr){
        //watch here
        scope.$watch('data', function(data){
            if (data[0].data[0].percent === undefined && data[1].data[0].percent === undefined){
              return false;
            }else {
                var margins = {
                top: 12,
                left: 48,
                right: 24,
                bottom: 24
            },
            legendPanel = {
                width: 180
            },
            width = 500 - margins.left - margins.right - legendPanel.width,
                height = 100 - margins.top - margins.bottom,
//                    dataset = scope.data;
                dataset = [{
                    data: [{
                        approval: 'approve',
                        count: 87
                    }],
                    name: 'Approve'
                }, {
                    data: [ {
                        approval: 'disapprove',
                        count: 13
                    }],
                    name: 'Disapprove'
                }

                ],
                series = dataset.map(function (d) {
                    return d.name;
                }),
                dataset = dataset.map(function (d) {
                    return d.data.map(function (o, i) {
                        return {
                            y: o.count,
                            x: o.disapprove
                        };
                    });
                }),
                stack = d3.layout.stack();

            stack(dataset);

            var dataset = dataset.map(function (group) {
                return group.map(function (d) {
                    // Invert the x and y values, and y0 becomes x0
                    return {
                        x: d.y,
                        y: d.x,
                        x0: d.y0
                    };
                });
            }),
                svg = d3.select('body')
                    .append('svg')
                    .attr('width', width + margins.left + margins.right + legendPanel.width)
                    .attr('height', height + margins.top + margins.bottom)
                    .append('g')
                    .attr('transform', 'translate(' + margins.left + ',' + margins.top + ')'),
                xMax = d3.max(dataset, function (group) {
                    return d3.max(group, function (d) {
                        return d.x + d.x0;
                    });
                }),
                xScale = d3.scale.linear()
                    .domain([0, xMax])
                    .range([0, width]),
                months = dataset[0].map(function (d) {
                    return d.y;
                }),
                _ = console.log(months),
                yScale = d3.scale.ordinal()
                    .domain(months)
                    .rangeRoundBands([0, height], .1),
                xAxis = d3.svg.axis()
                    .scale(xScale)
                    .orient('bottom'),
                yAxis = d3.svg.axis()
                    .scale(yScale)
                    .orient('left'),
                colours = d3.scale.category20b(),
                groups = svg.selectAll('g')
                    .data(dataset)
                    .enter()
                    .append('g')
                    .style('fill', function (d, i) {
                    return colours(i);
                }),
                rects = groups.selectAll('rect')
                .data(function (d) {
                return d;
                })
                    .enter()
                    .append('rect')
                    .attr('x', function (d) {
                    return xScale(d.x0);
                })
                    .attr('y', function (d, i) {
                    return yScale(d.y);
                })
                    .attr('height', function (d) {
                    return yScale.rangeBand();
                })
                    .attr('width', function (d) {
                    return xScale(d.x);
                });
                series.forEach(function (s, i) {
                    svg.append('text')
                        .attr('fill', 'black')
                        .attr('x', width + margins.left + 8)
                        .attr('y', i * 24 + 24)
                        .text(s);
                    svg.append('rect')
                        .attr('fill', colours(i))
                        .attr('width', 60)
                        .attr('height', 20)
                        .attr('x', width + margins.left + 90)
                        .attr('y', i * 24 + 6);
                })
            } //else statement end
        //end watch here
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