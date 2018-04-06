$('body').on('dblclick', '[data-editable]', function(){
  var $el = $(this);

  var $input = $('<input class="form-control" />').val( $el.text());
  $el.replaceWith( $input );

  var save = function(){
    var $p =  $('<div data-editable/>').text($input.val());
    $input.replaceWith( $p );
  };

  var reset = function(){
    $input.replaceWith( $el );
  }

  var enterEvent = new Event('enter');

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
