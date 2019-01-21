$('input').change(function (e) {

  //stop the form from firing as usual
  e.preventDefault();
  
  //set the label for the input to the new color value
  $("label[for='" + $(this).attr('id') + "'] > span").html(Math.round(this.value, 0));
  
  //set the color bar
  $('#output').css('backgroundColor','rgb(' + Math.round($('#red-slider').val(),0) + ',' + Math.round($('#green-slider').val(),0) + ',' + Math.round($('#blue-slider').val(),0) + ')');
	  
	//call flask and pass it the form
  $.ajax({
    url: '/',
    data: $('form').serialize(),
    type: 'POST',
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    }
  });
});
