$(document).ready(function () {
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
  $('INPUT#btn_translate').click(function (e) {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
