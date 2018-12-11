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
    }, 1000);
  });
}

var getUrl = window.location;
var baseurl = getUrl.origin;

function showModal(title, description, pub_date, location, image_link){
  $("#myModal #title").html(title)
  $("#myModal #description").html(description)
  $("#myModal #pub_date").html(pub_date)
  $("#myModal #location").html(location)
  $("#myModal #link").html(baseurl+image_link)
  $("#myModal img").attr('src', image_link)
  $("#myModal").modal();
}

const copyToClipboard = str => {
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

function closeModal(){
 $('.modal').on('hide.bs.modal', function (e) {
   $('.modal .modal-dialog').attr('class', 'modal-dialog  zoomOut slower  animated');
 }) 
}
$('.modal').on('show.bs.modal', function (e) {
  $('.modal .modal-dialog').attr('class', 'modal-dialog  zoomIn  animated');
})

var modal = document.getElementById('myModal');
window.onclick = function (event) {
   closeModal()
}