var $logo = $('#headliner');
$(document).scroll(function () {
  $logo.css({ display: $(this).scrollTop() > 600 ? "none" : "block" });
});