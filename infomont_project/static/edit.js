 // TODO refactor. This should not be attached to the body

$('body').on('dblclick', '[data-editable]', function(){
  var $el = $(this);

  var $text = $el.find('div');
  var $input = $el.find('input');

  $input.val( $text.text());

  $text.hide();
  $input.show();

  //var $input = $('<input class="form-control"/>').val( $el.text());
  //$el.replaceWith( $input );

  var save = function(){
    //var $p =  $('<div data-editable/>').text($input.val());
    //$input.replaceWith( $p );
    $text = $text.text($input.val())
    $text.show();
    $input.hide();
  };

  var reset = function(){
    //$input.replaceWith( $el );
    $text.show();
    $input.hide();
  }

  /**
    We're defining the callback with `one`, because we know that
    the element will be gone just after that, and we don't want
    any callbacks leftovers take memory.
    Next time `p` turns into `input` this single callback
    will be applied again.
  */
  $input.one('blur', reset).focus();

  $input.keyup(function(event) {
    if (event.keyCode === 13) { // enter key
        save();
    }
  });

  $input.keyup(function(event) {
    if (event.keyCode === 27) { // esc key
        reset();
    }
  });

});
