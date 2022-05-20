// jslint browser: true
// global $, jQuery, alert

var $button = $('.btn-task');
var $form = $('.form');
var $submit = $('.submit');

$form.hide();

$button.on('click', function() {
  $form.show().fadeIn(3000);
});

$button.on('dblclick', function() {
  $form.hide();
});

$submit.on('click', function() {
  $form.hide();
});
