 // TODO refactor. This should not be attached to the body

$('body').on('dblclick', '[data-editable]', function(){
  var $el = $(this);

  var $text = $el.find('div');
  var $input = $el.find('edit-tag');
  var $inner = $input.children().first()
  $inner.val( $text.text());

  $text.hide();
  $input.show();

  var save = function(){
    $text = $text.text($inner.val())
    $text.show();
    $input.hide();
  };

  var reset = function(){
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
  $inner.one('blur', reset).focus();

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
