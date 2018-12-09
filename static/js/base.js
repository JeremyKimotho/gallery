var $logo = $('#headliner');
$(document).scroll(function () {
  $logo.css({ display: $(this).scrollTop() > 350 ? "none" : "block" });
});

if ($('#back-to-top').length) {
  var scrollTrigger = 100, // px
    backToTop = function () {
      var scrollTop = $(window).scrollTop();
      if (scrollTop > scrollTrigger) {
        $('#back-to-top').addClass('show');
      } else {
        $('#back-to-top').removeClass('show');
      }
    };
  backToTop();
  $(window).on('scroll', function () {
    backToTop();
  });
  $('#back-to-top').on('click', function (e) {
    e.preventDefault();
    $('html,body').animate({
      scrollTop: 0
    }, 700);
  });
}

function showModal(title, description, pub_date, location, image_link){
  $("#myModal #title").html(title)
  $("#myModal #description").html(description)
  $("#myModal #pub_date").html(pub_date)
  $("#myModal #location").html(location)
  $("#myModal #link").html(image_link)
  $("#myModal").modal();
}

function copyToClipboard(str){
  const el = document.createElement('textarea');
  el.value = str;
  el.setAttribute('readonly', '');
  el.style.position = 'absolute';
  el.style.left = '-9999px';
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
};

$('.grid').masonry({
  itemSelector: '.grid-item',
  columnWidth: 200
});