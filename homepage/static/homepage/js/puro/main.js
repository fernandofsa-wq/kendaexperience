$(document).ready(function () {
    $('.materialboxed').materialbox();
    $('.sidenav').sidenav();
    $('.modal').modal();
    $(".dropdown-trigger").dropdown({
        hover:true,
        constrainWidth:false,
    });
    $('.slider').slider({
        indicators: true,
        height: 600,
    });
    // Patrocinio e Apoio
    $(".clients-carousel").owlCarousel({
        autoplay: true,
        dots: true,
        autoplayTimeout: 2000,
        loop: true,
        responsive: { 0: { items: 1 }, 768: { items: 2 }, 900: { items: 2 } }
    });
});

jQuery(document).ready(function($) {
    $(".scroll").click(function(event) {
        event.preventDefault();
        $('html,body').animate({ scrollTop: $(this.hash).offset().top }, 600);
    });
});

new VenoBox({
    selector: '.my-image-links',
    numeration: true,
    infinigall: true,
    share: true,
    spinner: 'rotating-plane'
});
      // Patrocinio e Apoio



