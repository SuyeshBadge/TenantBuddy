$("#search-icon").click(function() {
  $(".nav").toggleClass("search");
  $(".nav").toggleClass("no-search");
  $(".search-input").toggleClass("search-active");
});

$('.menu-toggle').click(function(){
   $(".menu").toggleClass("mobile-nav");
   $(this).toggleClass("is-active");
});




  document.addEventListener('DOMContentLoaded', 
    function(){
      Typed.new('.entry', {
        strings: ["Welcome to TENANTBUDDY !!!", "Want rooms at affordable price ?", "You're at the right place.", "Search rooms on the go......"],
        typeSpeed: .5
      });
  });