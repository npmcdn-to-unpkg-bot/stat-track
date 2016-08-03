// The function used to get data from python
function viz(pydata) {
    var dataset = pydata;
    var w = 200;
    var h = 130;

    var bar_w = h / dataset.length;

    var svg = d3.select('div.viz').append('svg');

    svg.attr({
            width: w,
            height: h
        });


    svg.selectAll('rect')
        .data(dataset)
        .enter()
        .append('rect')
        .attr("height", bar_w)
        .attr("width", function(d) { return d; } )
        .attr("x", 0)
        .attr("y", function(d, i) { return h + i * -(bar_w + 1) } );
}

