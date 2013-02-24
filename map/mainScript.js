$(document).ready(function(){
	window.alert("hoo");
	// Event handlers
	$("#up_button").click(function() {
		loadMap(tanzania, "small");
	});


	$("#small_button").click(function() {
		loadMap(current_view, "small");	
	});	
	
	$("#medium_button").click(function() {
		loadMap(current_view, "medium");	
	});

	$("#dewormed_button").click(function() {
		loadMap(current_view, "dewormed");	
	});


	// Hard-coded data structures
		var lindi = {
		"center": {"lat": -9.49, "lng": 38.39},
		"zoom_value": 8,
		"regions": [
			{"name": "Lindi",
			"boundary": 
				[
				{"lat": -9.413838916006183, "lng": 39.59197998046875},
				{"lat": -9.416548498325543, "lng": 39.64691162109375},
				{"lat": -9.933682229573083, "lng": 39.78973388671875},
				{"lat": -10.128413073382205, "lng": 40.00946044921875},
				{"lat": -10.13517245102933, "lng": 40.001220703125},
				{"lat": -10.3540986430304, "lng": 39.6441650390625},
				{"lat": -10.576922006062146, "lng": 39.6331787109375},
				{"lat": -10.508066443913318, "lng": 39.5013427734375},
				{"lat": -10.377063578093669, "lng": 39.5013427734375},
				{"lat": -10.35680048746009, "lng": 39.428558349609375},
				{"lat": -10.320323625412541, "lng": 39.431304931640625},
				{"lat": -10.35, "lng": 39.36},
				{"lat": -9.34, "lng": 38.79},
				{"lat": -9.42, "lng": 39.58}],
			"reached": {"small":3, "medium":15, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": null
			},

			{"name": "Ruangwa",
			"boundary": 
				[{"lat": -10.35, "lng": 39.36},
				{"lat": -9.34, "lng": 38.79},
				{"lat": -9.49, "lng": 38.39},
				{"lat": -10.48, "lng": 38.82}],
			"reached": {"small":20, "medium":40, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": null
			},

			{"name": "Nachinwea",
			"boundary": 
				[{"lat": -10.48, "lng": 38.82},
				{"lat": -9.49, "lng": 38.39},

				{"lat": -10.53, "lng": 37.73},
				{"lat": -10.83, "lng": 37.97}],
			"reached": {"small":15, "medium":40, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": null
			},

			{"name": "Liwale",
			"boundary": 
				[{"lat": -9.49, "lng": 38.39},
				{"lat": -10.53, "lng": 37.73},
				
				
				{"lat": -10.144635340238576, "lng": 36.81793212890625},
				{"lat": -10.03917597234094, "lng": 36.87286376953125},
				{"lat": -9.86604011578546, "lng": 36.89208984375},
				{"lat": -9.654907854199012, "lng": 37.1282958984375},
				{"lat": -9.397580976145512, "lng": 37.2711181640625},
				{"lat": -9.167178732976664, "lng": 37.32330322265625},
				{"lat": -9.00716428515312, "lng": 37.44415283203125},
				{"lat": -8.811796526762704, "lng": 37.33978271484375},
				{"lat": -8.507686571784284, "lng": 37.3809814453125},
				{"lat": -7.95043683502936, "lng": 37.8369140625},

				
				{"lat": -7.98, "lng": 37.83},
				{"lat": -8.44, "lng": 38.75}],
			"reached": {"small":5, "medium":40, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": null
			},

			{"name": "Kilwa",
			"boundary": 
				[{"lat": -8.44, "lng": 38.75},
				{"lat": -8.29, "lng": 39.32},
				{"lat": -9.42, "lng": 39.58},
				{"lat": -9.34, "lng": 38.79},
				{"lat": -9.49, "lng": 38.39}],
			"reached": {"small":5, "medium":40, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": null
			}]
			
		};

		var tanzania = {
		"center": {"lat": -8.45, "lng": 36.72},

		"zoom_value": 6,
		"regions": [
			{"name": "Mtwara",
			"boundary": 
				[
				{"lat": -10.14193168613103, "lng": 39.979248046875},
				{"lat": -10.352747712085751, "lng": 39.4134521484375},
				{"lat": -10.48241044158667, "lng": 38.6663818359375},
				{"lat": -10.860281096281652, "lng": 38.0072021484375}, //UP
				{"lat": -11.256531087565222, "lng": 38.06488037109375}, //DOWN
				{"lat": -11.42618683357128, "lng": 38.4796142578125},
				{"lat": -11.173012874215052, "lng": 38.91357421875},
				{"lat": -10.81711974903753, "lng": 39.96826171875},
				{"lat": -10.471607278043903, "lng": 40.4351806640625},
				{"lat": -10.136524309456217, "lng": 40.001220703125}
				],
			"reached": {"small":3, "medium":15, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": null
			},

			{"name": "Ruwuma",
			"boundary": 
				[{"lat": -11.555380322321756, "lng": 34.98046875},
				{"lat": -11.555380322321756, "lng": 35.628662109375},
				{"lat": -11.431571076012272, "lng": 35.8319091796875},
				{"lat": -11.700651804193889, "lng": 36.27685546875},
				{"lat": -11.6952727330294, "lng": 37.353515625},
				{"lat": -11.275386692600028, "lng": 38.0401611328125},
				{"lat": -11.256531087565222, "lng": 38.06488037109375},
				{"lat": -10.860281096281652, "lng": 38.0072021484375},
				{"lat": -10.558022013388603, "lng": 37.8094482421875},
				{"lat": -10.14193168613103, "lng": 36.8316650390625},
				{"lat": -9.893098633379571, "lng": 35.26611328125},
				{"lat": -10.520218543737034, "lng": 34.5849609375},
				{"lat": -11.544616463449655, "lng": 34.95849609375}],
			"reached": {"small":20, "medium":40, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": null
			},

			{"name": "Lindi",
			"boundary": 
				[{"lat": -10.860281096281652, "lng": 38.0072021484375},
				{"lat": -10.48241044158667, "lng": 38.6663818359375},
				{"lat": -10.352747712085751, "lng": 39.4134521484375},
				{"lat": -10.14193168613103, "lng": 39.979248046875},
				{"lat": -8.249546418605748, "lng": 39.3365478515625},
				{"lat": -8.450638800330989, "lng": 38.759765625},
				{"lat": -7.972197714386866, "lng": 37.8424072265625},
				{"lat": -9.020727597059931, "lng": 37.430419921875},
				{"lat": -10.120301632173906, "lng": 36.8646240234375},
				{"lat": -10.14193168613103, "lng": 36.8316650390625},
				{"lat": -10.558022013388603, "lng": 37.8369140625}],
			"reached": {"small":15, "medium":40, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": lindi
			},

			{"name": "Pwani",
			"boundary": 
				[{"lat": -8.249546418605748, "lng": 39.3365478515625},
				{"lat": -8.450638800330989, "lng": 38.759765625},
				{"lat": -7.972197714386866, "lng": 37.8424072265625},
				{"lat": -7.563992005533067, "lng": 37.9083251953125},
				{"lat": -7.618442212274373, "lng": 38.3258056640625},
				{"lat": -6.719164960283201, "lng": 38.3587646484375},
				{"lat": -6.610044093207648, "lng": 38.0126953125},
				{"lat": -5.922044619883305, "lng": 37.8204345703125},
				{"lat": -5.998533174329328, "lng": 38.7982177734375},
				{"lat": -6.604587414293243, "lng": 39.144287109375},
				{"lat": -6.82826134882511, "lng": 39.0179443359375},
				{"lat": -7.0082158366633935, "lng": 39.5452880859375},
				{"lat": -7.759980241585288, "lng": 39.385986328125}],
			"reached": {"small":5, "medium":40, "dewormed":20},
			"total": {"small":20, "medium": 50, "dewormed":40},
			"submap": null
			}]
			
		};	


	// Program variables
	var map, regions, regionStructure, current_view;

	

	// Main method
	function loadMap(incoming_data, attribute) {
		var mapOptions = {
			center: new google.maps.LatLng(
				incoming_data["center"]["lat"],
				incoming_data["center"]["lng"]),
			zoom: incoming_data["zoom_value"],
			mapTypeId: google.maps.MapTypeId.ROADMAP,
	     	   };

		map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
	
		regions = new Array();
		for(var j=0; j<incoming_data["regions"].length; j++) {
			var boundary = new Array();
			for(var i=0; i<incoming_data["regions"][j]["boundary"].length; i++) {
				boundary.push(new google.maps.LatLng(
						incoming_data["regions"][j]["boundary"][i]["lat"],
						incoming_data["regions"][j]["boundary"][i]["lng"]));
			};
			
			var percentAttribute = 1.0*incoming_data["regions"][j]["reached"][attribute] / 
					incoming_data["regions"][j]["total"][attribute];


			var regionPoly = new google.maps.Polygon({
				paths: boundary,
				strokeColor: "#000000",
				strokeOpacity: 0.8,
				strokeWeight: 2,	
				fillColor: "rgb(0," + Math.round(255*percentAttribute) + ", 0)",
				fillOpacity: 0.4
			});

			regions.push(regionPoly);
			regionPoly.setMap(map);

			var info_panel = generateInfoPanel(incoming_data["regions"][j]);
			google.maps.event.addListener(regionPoly, "mouseover", 
				createMouseOverListener(info_panel)
			);
		
			google.maps.event.addListener(regionPoly, "mouseout", 
			function(event) {$("#region_info").html("Move mouse cursor over a region to see details");}
			);

			google.maps.event.addListener(regionPoly, "click", 
				createOnClickListener(incoming_data["regions"][j])
			);

			current_view = incoming_data;
		}
	}
		
	
	function createMouseOverListener(description) {
		return function(event) {
			$("#region_info").html(description);
		}
	}

	function createOnClickListener(region) {
		return function(event) {
			if(region["submap"] != null) loadMap(region["submap"], "small");
		}
	}

	function generateInfoPanel(region) {
		var result = "<b>Region info:</b><br />" +
			"Region name: " + region["name"] + "<br>" + 
			"Small: " + region["reached"]["small"] + " out of " + region["total"]["small"] + " -> " +
				Math.round(100*region["reached"]["small"] / region["total"]["small"]) + " % <br />" +			'<div class="progress">  <div class="bar" style="width: 60%;"></div></div> <br />' +
			"Medium: " + region["reached"]["medium"] + " out of " + region["total"]["medium"] + " -> " +
				Math.round(100*region["reached"]["medium"] / region["total"]["medium"]) + " % <br />" +
			"Dewormed: " + region["reached"]["dewormed"] + " out of " + region["total"]["dewormed"] + " -> " +
				Math.round(100*region["reached"]["dewormed"] / region["total"]["dewormed"]) + " % <br />";
	

		return result;
	}


	// Main entry point
	loadMap(tanzania, "small");
});

