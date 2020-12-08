
function initMap(){  
  

// Plot map --------------------------------------------------------------------
    var mapContainer= document.querySelector('#maps');   

    var button = document.querySelector('#research');    
    var mapOptions = {
   
      center:{lat:-23.9618,lng:-46.3322},
      zoom:15,
      mapTypeId:'roadmap',
      zoom:15,
      styles:[
        {
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#ebe3cd"
            }
          ]
        },
        {
          "elementType": "labels.text.fill",
          "stylers": [
            {
              "color": "#523735"
            }
          ]
        },
        {
          "elementType": "labels.text.stroke",
          "stylers": [
            {
              "color": "#f5f1e6"
            }
          ]
        },
        {
          "featureType": "administrative",
          "elementType": "geometry.stroke",
          "stylers": [
            {
              "color": "#c9b2a6"
            }
          ]
        },
        {
          "featureType": "administrative.land_parcel",
          "elementType": "geometry.stroke",
          "stylers": [
            {
              "color": "#dcd2be"
            }
          ]
        },
        {
          "featureType": "administrative.land_parcel",
          "elementType": "labels.text.fill",
          "stylers": [
            {
              "color": "#ae9e90"
            }
          ]
        },
        {
          "featureType": "landscape.natural",
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#dfd2ae"
            }
          ]
        },
        {
          "featureType": "poi",
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#dfd2ae"
            }
          ]
        },
        {
          "featureType": "poi",
          "elementType": "labels.text.fill",
          "stylers": [
            {
              "color": "#93817c"
            }
          ]
        },
        {
          "featureType": "poi.park",
          "elementType": "geometry.fill",
          "stylers": [
            {
              "color": "#a5b076"
            }
          ]
        },
        {
          "featureType": "poi.park",
          "elementType": "labels.text.fill",
          "stylers": [
            {
              "color": "#447530"
            }
          ]
        },
        {
          "featureType": "road",
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#f5f1e6"
            }
          ]
        },
        {
          "featureType": "road.arterial",
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#fdfcf8"
            }
          ]
        },
        {
          "featureType": "road.highway",
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#f8c967"
            }
          ]
        },
        {
          "featureType": "road.highway",
          "elementType": "geometry.stroke",
          "stylers": [
            {
              "color": "#e9bc62"
            }
          ]
        },
        {
          "featureType": "road.highway.controlled_access",
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#e98d58"
            }
          ]
        },
        {
          "featureType": "road.highway.controlled_access",
          "elementType": "geometry.stroke",
          "stylers": [
            {
              "color": "#db8555"
            }
          ]
        },
        {
          "featureType": "road.local",
          "elementType": "labels.text.fill",
          "stylers": [
            {
              "color": "#806b63"
            }
          ]
        },
        {
          "featureType": "transit.line",
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#dfd2ae"
            }
          ]
        },
        {
          "featureType": "transit.line",
          "elementType": "labels.text.fill",
          "stylers": [
            {
              "color": "#8f7d77"
            }
          ]
        },
        {
          "featureType": "transit.line",
          "elementType": "labels.text.stroke",
          "stylers": [
            {
              "color": "#ebe3cd"
            }
          ]
        },
        {
          "featureType": "transit.station",
          "elementType": "geometry",
          "stylers": [
            {
              "color": "#dfd2ae"
            }
          ]
        },
        {
          "featureType": "water",
          "elementType": "geometry.fill",
          "stylers": [
            {
              "color": "#b9d3c2"
            }
          ]
        },
        {
          "featureType": "water",
          "elementType": "labels.text.fill",
          "stylers": [
            {
              "color": "#92998d"
            }
          ]
        }
      ],
      zoomControl:false,
      streetViewControl:false,
      mapTypeControlOptions:{
        style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
        position: google.maps.ControlPosition.TOP_CENTER
      },
      fullscreenControl:true,
      scaleControl:true,
      mapTypeControl:false
      
    }
    var map=new google.maps.Map(mapContainer, mapOptions);

//Autocomplete adress ---------------------------------------------------

var adress1= document.querySelector('#origins');
//var adress2= document.querySelector('#destination');


var completeOptions1 = {
    
    componentRestrictions: {country: 'br'}
  };
var autocomplete= new google.maps.places.Autocomplete(adress1,completeOptions1);

//var completeOptions2 = {
    //types: ['address'],
    //componentRestrictions: {country: 'br'}
  //};
//var autocomplete= new google.maps.places.Autocomplete(adress2,completeOptions2);


    
//Evento de click plotando Directions + Calculo de Distância-----------------------
    button.addEventListener('click',function(e){
        e.preventDefault();
//Variaveis -----------------------------------------------------------------------
      
        var origins= document.querySelector('#origins').value;
        var destination= 'Rua Comendador Alfaia Rodrigues, Santos, SP'; 
        var distance= document.querySelector('#distance');
        var time=document.querySelector('#time');
        var taxes=document.querySelector('#taxes');    
     
//Directions API ------------------------------------------------------------------
        
        var directionsService = new google.maps.DirectionsService();  
        
        directionsService.route({
            origin:origins ,
            destination:destination ,
            travelMode: 'WALKING',
            transitOptions: {
                modes: ['SUBWAY','BUS'],    
            },     
 
        }, function(results,status){
            
            if(status=='OK'){
               var directionsRenderer = new google.maps.DirectionsRenderer();
           
                
                directionsRenderer.setMap(map);
                directionsRenderer.setDirections(results);
            }else{
                console.log('Error: '+ status)
            }
        }); 

//Calculando Distance Matrix-------------------------------------------------------
var service = new google.maps.DistanceMatrixService();
service.getDistanceMatrix(
  {
    origins: [origins],
    destinations: [destination],
    travelMode: 'DRIVING',
    transitOptions: {
    
     modes: ['BUS','TRAIN','SUBWAY'],
     routingPreference: 'FEWER_TRANSFERS'
   },
    unitSystem: google.maps.UnitSystem.METRIC,
    avoidHighways: true,
    avoidTolls: true,
  }, callback);

function callback(response, status) { 
  
 if(status == 'OK'){ 
  distance.innerHTML="Distância: "+response.rows[0].elements[0].distance.text;
  time.innerHTML="Tempo estimado: "+response.rows[0].elements[0].duration.text; 
  
 }else{
   console.log('O que aconteceu?');
 }
};
       
});

var clean = document.querySelector('#clean');

clean.addEventListener('click',function(){

  var mapContainer= document.querySelector('#maps'); 
   
  var mapOptions = {
 
    center:{lat:-23.9618,lng:-46.3322},
    zoom:15,
    mapTypeId:'roadmap',
    zoom:15,
    styles:[
      {
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#ebe3cd"
          }
        ]
      },
      {
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#523735"
          }
        ]
      },
      {
        "elementType": "labels.text.stroke",
        "stylers": [
          {
            "color": "#f5f1e6"
          }
        ]
      },
      {
        "featureType": "administrative",
        "elementType": "geometry.stroke",
        "stylers": [
          {
            "color": "#c9b2a6"
          }
        ]
      },
      {
        "featureType": "administrative.land_parcel",
        "elementType": "geometry.stroke",
        "stylers": [
          {
            "color": "#dcd2be"
          }
        ]
      },
      {
        "featureType": "administrative.land_parcel",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#ae9e90"
          }
        ]
      },
      {
        "featureType": "landscape.natural",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#dfd2ae"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#dfd2ae"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#93817c"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#a5b076"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#447530"
          }
        ]
      },
      {
        "featureType": "road",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#f5f1e6"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#fdfcf8"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#f8c967"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [
          {
            "color": "#e9bc62"
          }
        ]
      },
      {
        "featureType": "road.highway.controlled_access",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#e98d58"
          }
        ]
      },
      {
        "featureType": "road.highway.controlled_access",
        "elementType": "geometry.stroke",
        "stylers": [
          {
            "color": "#db8555"
          }
        ]
      },
      {
        "featureType": "road.local",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#806b63"
          }
        ]
      },
      {
        "featureType": "transit.line",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#dfd2ae"
          }
        ]
      },
      {
        "featureType": "transit.line",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#8f7d77"
          }
        ]
      },
      {
        "featureType": "transit.line",
        "elementType": "labels.text.stroke",
        "stylers": [
          {
            "color": "#ebe3cd"
          }
        ]
      },
      {
        "featureType": "transit.station",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#dfd2ae"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#b9d3c2"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#92998d"
          }
        ]
      }
    ],
    zoomControl:false,
    streetViewControl:false,
    mapTypeControlOptions:{
      style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
      position: google.maps.ControlPosition.TOP_CENTER
    },
    fullscreenControl:true,
    scaleControl:true,
    mapTypeControl:false
    
  }
  var map=new google.maps.Map(mapContainer, mapOptions);

  // Apagando conteudo do input ---------------------------------------
  adress1.value="";
  //adress2.value="";
});
 
}
  

//src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCdj4cfypAzgr-E44tjCMU6A94Q69i8Ij4&libraries=places&language=pt&callback=initMap"