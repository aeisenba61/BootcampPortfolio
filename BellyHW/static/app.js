// DROPDOWN

var selectDiv = document.getElementById("selDataset");

Plotly.d3.json("/names", function(error, response) {
    if(error) return console.warn(error);
    var bb_ids = response;
    for (var i = 0; i < bb_ids.length; i++) {
        var option = document.createElement("option");
        option.value = bb_ids[i];
        option.text = bb_ids[i];
        selectDiv.appendChild(option)
    }
})

// Pie
Plotly.d3.json("/samples/BB_940", function(error, response) {
    if (error) return console.warn(error);
  	var data = [{ values: response.sample_values.slice(0,9),
                  labels: response.otu_ids.slice(0,9),
                  type: 'pie',
                  text: "OTU: " + response.otu_ids,
                  textposition: 'inside',
                  hole: .5,
                  hoverinfo: "labels"}];

  	var layout = {height: 400, 
  		            width: 500,
                  margin: {
                    l: 50, r: 50, b: 50, t: 50
                  },
  		            title: "Top 10 Sample Values",
  		            annotations: [{
              			font: {
  				            size: 20
  			           },
  			          showarrow: false,
  			          text: 'BBs'}]
  	};

  	Plotly.plot("pie", data, layout)

})

//bubbles
Plotly.d3.json("/samples/BB_940", function(error, response){
    if (error) return console.warn(error);
    var data = [{
        x: response.otu_ids,
        y: response.sample_values,
        mode: 'markers',
        hoverinfo: "x+y",
        marker: {
            color: ['E7641D',
                       'D46E19',
                       'C17816',
                       'AF8213',
                       '9C8C10'],
            size: response.sample_values
        }
    }];
    var layout = {
        height: 600,
        width: 900,
        title: "Belly Button Bubble Chart",
        xaxis: {title: "OTU IDs"},
        yaxis: {title: "Sample values"}
    };
    Plotly.plot("bubble", data, layout);
})


//metatable
var metatable = document.getElementById("metatable");
Plotly.d3.json("/metadata/BB_940", function(error, response){
    if (error) return console.warn(error);
    htmltable = ""
    for (key in response) {
    	htmltable += "<b>" + key + " </b>"+ response[key] + "<br>";
    }
    metatable.innerHTML = htmltable
})


//Gauge
Plotly.d3.json("/wfreq/BB_940", function(error, response){
    if (error) return console.warn(error);
    var level = response;
    var degrees = 9 - level,
    	radius = .5;
    var radians = degrees * Math.PI / 180;
    var x = radius * Math.cos(radians);
    var y = radius * Math.sin(radians);
	var mainPath = 'M -.0 -0.05 L .0 0.05 L ',
		pathX = String(x),
     	space = ' ',
	 	pathY = String(y),
     	pathEnd = ' Z';
	var path = mainPath.concat(pathX,space,pathY,pathEnd);
	var data = [{ type: 'scatter',
   		x: [0], y:[0],
    	marker: {size: 28, color:'850000'},
    	showlegend: false,
    	name: 'frequency',
    	text: level,
      direction: "counter-clockwise",
    	hoverinfo: 'text+name'},
  		{ values: [50/9,50/9,50/9,50/9,50/9,50/9,50/9,50/9,50/9,50],
  		rotation: 90,
  		text: ['8-9', '7-8', '6-7', '5-6',
            '4-5', '3-4', '2-3', '1-2', '0-1'],
  		textinfo: 'text',
  		textposition:'inside',      
  		marker: {colors:['#008000','#228d1b','#359a2d','#46a83e','#55b54e','#64c35f','#73d26f','#81e07f','#90ee90','FFFFFF']},
  		// labels: ['8-9', '7-8', '6-7', '5-6',
    //         '4-5', '3-4', '2-3', '1-2', '0-1'],
  		hoverinfo: 'text',
  		hole: .5,
  		type: 'pie',
  		showlegend: false
		}];

	var layout = {
		shapes:[{
	    	type: 'path',
      		path: path,
	     	fillcolor: '850000',
	     	line: {
	        color: '850000'
	      }
	    }],
		title: '<b>Gauge</b> <br> Speed 0-9',
		height: 500,
		width: 700,
    margin: {
                    l: 50, r: 50, b: 50, t: 50
                  },
		xaxis: {zeroline:false, showticklabels:false, showgrid: false, range: [-1, 1]},
		yaxis: {zeroline:false, showticklabels:false, showgrid: false, range: [-1, 1]}
	};
	Plotly.plot("gauge", data, layout);
});


// Pie
function updatePie(newdata) {
	var Pie = document.getElementById("pie");
	Plotly.restyle(Pie, "labels", [newdata.otu_ids.slice(0,10)]);
	Plotly.restyle(Pie, "values", [newdata.sample_values.slice(0,10)]);
}

// Bubble
function updateBubble(newdata) {
	var Bubble = document.getElementById('bubble');
	Plotly.restyle(Bubble, "x", [newdata.otu_ids]);
	Plotly.restyle(Bubble, "y", [newdata.sample_values]);
}

// Gauge
function updateGauge(newdata) {
	var Gauge = document.getElementById('gauge');
	Plotly.restyle(Gauge, "level", [newdata.value]);
}

function optionChanged(sample) {
    var sampURL = `/samples/${sample}`
    var metaURL = `/metadata/${sample}`
    var wfreqURL = `/wfreq/${sample}`

    // New data
    Plotly.d3.json(sampURL, function(error, response) {
      if (error) return console.warn(error);
      var vals = [];
      var labs = [];
      for (var i = 0; i < 10; i++){
        vals.push(response.sample_values[i]);
        labs.push(response.otu_ids[i]);
      }
      newdata = {values: vals, labels: labs};
      updatePie(newdata);
      updateBub(newdata);
    });

    Plotly.d3.json(wfreqURL, function(error, response) {
      if (error) return console.warn(error);
      var newLevel = [];
      newdata = newLevel.push(response[0]);
      updateGauge(newdata);
    });
}