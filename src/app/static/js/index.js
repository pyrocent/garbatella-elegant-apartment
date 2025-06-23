$(document).ready(function () {

    $("#languages").change(function () {
        fetch(window.location.href, {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: `lang=${$(this).val()}`,
        })
            .then(response => {
                if (response.status === 200) {
                    window.location.reload();
                }
            })
            .catch(error => {
                console.error(error);
            });
    });

    $(".book").click(function () {
        window.location.href = "/book-holiday-home"
    });

    $("#slider-for").slick({
        fade: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: "#slider-nav",
        prevArrow: "<button class = slick-prev><</button>",
        nextArrow: "<button class = slick-next>></button>"
    });

    if ($(window).width() <= 768) {
        $("#slider-nav").slick({
            arrows: false,
            autoplay: true,
            slidesToShow: 3,
            touchMove: false,
            slidesToScroll: 1,
            focusOnSelect: true,
            pauseOnHover: false,
            pauseOnFocus: false,
            autoplaySpeed: 3000,
            asNavFor: "#slider-for"
        });
    } else {
        $("#slider-nav").slick({
            arrows: false,
            autoplay: true,
            vertical: true,
            slidesToShow: 3,
            touchMove: false,
            slidesToScroll: 1,
            focusOnSelect: true,
            pauseOnHover: false,
            pauseOnFocus: false,
            autoplaySpeed: 3000,
            asNavFor: "#slider-for"
        });
    }

    $(".tab-button:not('#more')").click(function () {
        $(".tab-content").removeClass("active");
        $(".tab-button").removeClass("active");
        var $this = $(this);
        $this.addClass("active");
        $("#" + $this.data("tab")).addClass("active");
    });

    $("#more").click(function () {
        window.location.href = "/more"
    });

});