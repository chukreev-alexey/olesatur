$(function() {
    function init_plugins() {
        //Placeholder
        $('input, textarea').placeholder();
        //Phone mask
        $(".vPhoneField").inputmask({
            "mask": '+7(999)-999-9999'
            //'autoUnmask' : true,
            //'clearMaskOnLostFocus': false
        });
        var flexslider = $('.flexslider').flexslider({
            animation: "slide",
            slideshowSpeed: 5000,
            animationSpeed: 1200,
            controlNav: false,
            useCSS: false,
            video: true,
            after: function (slider) {
                var title = $(slider.slides[slider.currentSlide]).data("title"),
                    price = $(slider.slides[slider.currentSlide]).data("price"),
                    description = $(slider.slides[slider.currentSlide]).data("description");

                $(".top-slider-title").html(title + " " + price + " <span>руб</span>");
                $(".top-slider-info").text(description);
            }
         });

        $(".top-slider-left").on("click", function () {
            flexslider.flexslider("prev");
        });

        $(".top-slider-right").on("click", function () {
            flexslider.flexslider("next");
        });
    }
    init_plugins();

    //Переключение табов на главной странице
    $("ul.left-menu").on("click", "li:not(.active) > a", function () {
        var $dst =  $('#index_block_' + $(this).attr('href').substr(1));
        if ($dst) {
            $("div.index_block_container").hide();
            $dst.show();
            $("ul.left-menu > li").removeClass('active');
            $(this).parent().addClass('active');
        }
        return false;
    });

    //Всплывающее окно заявки
    function close_popup(e) {
        $(".popup-outer").hide();
    }

    $(".popup").on('click', ".popup-close", close_popup);
    $(".popup").on('click', ".button > button", function () {
        var $form = $(this).closest('form');
        $.ajax({
            url: $form.attr('action'),
            type: "POST",
            data: $form.serializeArray()
        }).done(function(response) {
            if (response == 'success') {
                $(".popup-inner").html('<p>Ваша заявка принята в обработку. Наши менеджеры свяжутся с вами в ближайшее время.</p>');
                setInterval(close_popup, 5000);
            }
            else {
                $(".popup-inner").html(response);
                init_plugins();
            }
        });
        return false;
    });

    $("a.send-order[tour]").click(function () {
        var url = "/order_form/" + $(this).attr('tour') + '/';
        $.ajax({
            url: url,
            type: "GET"
        }).done(function(response) {
            $(".popup-inner").html(response);
            init_plugins();
        });
        $(".popup-outer").show();
        return false;
    });

    $(".popup-shadow").click(function (e) {
        if ($(e.target).hasClass("popup-outer")) {
            close_popup();
        }
        return false;
    });
});
