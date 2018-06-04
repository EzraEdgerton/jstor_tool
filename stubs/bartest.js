var chart = dc.barChart("#test");

var chart = dc.barChart("#test");
d3.json("data.json").then(function(experiments) {

  var ndx                 = crossfilter(experiments),
      runDimension        = ndx.dimension(function(d) {return +d.year;}),
      speedSumGroup       = runDimension.group().reduceSum(function(d) {return d.Speed * d.Run / 1000;});
  chart
    .width(768)
    .height(480)
    .x(d3.scaleLinear().domain([6,20]))
    .brushOn(false)
    .yAxisLabel("This is the Y Axis!")
    .dimension(runDimension)
    .group(speedSumGroup)
    .on('renderlet', function(chart) {
        chart.selectAll('rect').on("click", function(d) {
            console.log("click!", d);
        });
    });
    chart.render();
});