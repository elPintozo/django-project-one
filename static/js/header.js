$(document).ready(function() {
    $(".button-collapse").sideNav({
    	menuWidth: 330, // Default is 240
      	edge: 'right', // Choose the horizontal origin
    });
    
  $('.dropdown-button').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrain_width: true, // Does not change width of dropdown to that of the activator
      hover: false, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: true, // Displays dropdown below the button
      alignment: 'left' // Displays dropdown with edge aligned to the left of button
    }
  );
        
});