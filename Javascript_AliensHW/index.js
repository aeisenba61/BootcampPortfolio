// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $stateInput = document.querySelector("#state");
var $cityInput = document.querySelector("#city");
var $dateInput = document.querySelector("#date");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
var $searchBtn = document.querySelector("#search");
$searchBtn.addEventListener("click", filterDataButton);

// Set filteredSightings to addressData initially
var filteredSightings = dataSet;
//console.log(filteredSightings)

// renderTable renders the filteredsighting to the tbody
function renderTable() {
  var $tbody = document.querySelector("tbody");
  for (var i = 0; i < filteredSightings.length; i++) {
    // Get get the current sighting object and its fields
    var sighting = filteredSightings[i];
    fields = Object.keys(sighting);
    //console.log(fields)
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the sighting object, create a new cell at set its inner text to be the current value at the current sighting's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sighting[field];
    }
  }
}

function filterDataButton() {
  var $countryInput = '';
  var $stateInput = '';
  var $cityInput = '';
  var $dateInput = '';
  var $shapeInput = '';
  $countryInput = document.getElementById("country").value.toLowerCase().trim();
  $stateInput = document.getElementById("state").value.toLowerCase().trim();
  $cityInput = document.getElementById("city").value.toLowerCase().trim();
  $dateInput = document.getElementById("date").value.trim();
  $shapeInput = document.getElementById("shape").value.toLowerCase().trim();
  var filters = {};

  //  
  if ($stateInput != "" && $stateInput != undefined) {
  filters.state = document.getElementById("state").value.trim().toLowerCase()
  }
  if ($cityInput != "" && $cityInput != undefined) {
  filters.city = document.getElementById("city").value.trim().toLowerCase()
  }
  if ($dateInput != "" && $dateInput != undefined) {
  filters.datetime = document.getElementById("date").value.trim()
  }
  if ($countryInput !="" && $countryInput != undefined) {
  filters.country = document.getElementById("country").value.trim().toLowerCase()
  }
  if ($shapeInput !="" && $shapeInput != undefined) {
  filters.shape = document.getElementById("shape").value.trim().toLowerCase()
  }

  filteredSightings = dataSet.filter(function(sighting) {
    for(var key in filters) {
      //console.log(sighting[key])
      if(sighting[key] === undefined || sighting[key] != filters[key].trim().toLowerCase())
        //console.log(sighting[key]);
        return false;
    }
    console.log(sighting[key]);
    
    return filteredSightings;

  });
  renderTable();
};

renderTable();

$(document).ready(function() {
    $('#tabler').DataTable( {
        "language": {
          "search": "Search comments: "
        }
     })
} );

