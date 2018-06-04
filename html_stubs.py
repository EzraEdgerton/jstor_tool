import string
import json


page_code_f = open("stubs/barpagestub.html", "r")

bar_page_code = page_code_f.read()


groupAndDimension = """ ***field***Dimension = cs.dimension(function(d){return d.***field***})
  					***field***Group = ***field***Dimension.group()"""

bar_html = '<div id="***field***"></div>'
bar_long_label_html = '<div id="***field***" class="longlabel"></div>'
jsbardeclare = 'var ***field***Chart = dc.barChart("#***field***");'

length_calc = """
				let ***field***width = 1000
				let ***field***length = ***field***Group.all().length
				
				if(***field***length  > 200){
					***field***width = ***field***length * 10
				}
			"""

bar_ordinal = """

    ***field***Chart
    .width(***field***width)
    .height(200)
    .x(d3.scaleBand())
    .xUnits(dc.units.ordinal)
    .yAxisLabel("***field***")
    .dimension(***field***Dimension)
    .group(***field***Group)
    .elasticY(true)
    .controlsUseVisibility(true)
    .on('pretransition', function(chart) {
        ***field***Chart.selectAll("rect.bar").on("click", function (d) {
            ***field***Chart.filter(null)
                .filter(d.data.key)
                .redrawGroup();
              })
      })



"""

bar_linear = """

  ***field***Chart
    .width(1000)
    .height(200)
    .x(d3.scaleLinear().domain(d3.extent(json_data, function(d){
      return d.***field***
    })))
    .brushOn(true)
    .yAxisLabel("***field***")
    .dimension(***field***Dimension)
    .group(***field***Group)
    .elasticY(true)

"""




