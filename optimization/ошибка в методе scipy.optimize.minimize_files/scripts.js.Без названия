jQuery(function($) {
    "use strict";



    if ( getCookie('hide_modal') != 'hide' ) {
        setTimeout(function(){
            $('.js-overlay').fadeIn(100);
            $('.js-modal').fadeIn(300);
        }, 6000);
    }


    $('.js-modal-close, .js-overlay').click(function(){
        $('.js-modal').fadeOut(100);
        $('.js-overlay').fadeOut(300);

        set_cookie('hide_modal', 'hide', 86400, '/');
    });


    /********************************************************************
     * Social Image Hover
     *******************************************************************/

    function image_hover_social() {

        if ( ! $('.image-hover-social-buttons').length ) return false;

        var vetteo_image_hover = $('.entry-content, .post-image');
        var buttons = $('.image-hover-social-buttons').html();

        if ($(window).width() > 1000) {
            vetteo_image_hover.on('mouseenter', 'img', function (e) {
                e.preventDefault();

                //if ( ! $(this).hasClass(/^wp-image/) ) return false;

                if ($(this).width() < 200 || $(this).height() < 200) return false;
                if ($(this).closest(".image-hover").length > 0) return false;

                var image_hover_styles = image_hover_style($(this));

                $(this).addClass('image-hovered image-hover-reset');
                $(this).wrap('<div class="image-hover" style="' + image_hover_styles + '"></div>');
                $(this).after('<span class="image-hover-share">' + buttons + '</span>');
            });
            vetteo_image_hover.on('mouseleave', ".image-hover", function (e) {
                e.preventDefault();

                $(this).find('.image-hover-share').remove();
                $(this).find('.image-hovered').unwrap().removeClass('image-hovered').removeClass('image-hover-reset');
            });
        }
    }
    image_hover_social();

    function image_hover_style( el ) {
        var to_return = "",
            n, r = ["margin-top", "margin-bottom", "margin-left", "margin-right", "position", "top", "bottom", "left", "right", "float", "max-width"];
        for (var i = 0; i < r.length; i++) {
            var attribute = r[i];
            if (attribute === "position" && el.css(attribute) === "static") {
                n = "relative"
            } else if (attribute === "display" && el.css(attribute) === "inline") {
                n = "inline-block"
            } else if (attribute === "display" && el.css(attribute) === "none") {
                return
            } else if (attribute === "width") {
                n = "" + el.outerWidth() + "px"
            } else if (attribute === "height") {
                n = "" + el.outerHeight() + "px"
            } else {
                n = el.css(attribute)
            }
            to_return += attribute + ":" + n + ";"
        }
        return to_return
    }



    /********************************************************************
     * Поиск
     *******************************************************************/
    $('.header-search').hover(function(){
        $(this).addClass('open');
    }, function(){
        if ( $(this).find('input').val() == '' && ! $(this).find('input').is(":focus") ) {
            $(this).removeClass('open');
        }
    });
    if ( $('.header-search input').val() != '' ) {
        $('.header-search').addClass('open');
    }
    $('.header-search').on('blur', 'input', function(){
        if ( $(this).val() == '' ) {
            $(this).removeClass('open');
        } else {
            $(this).addClass('open');
        }
    });




    /**
     * Закрепляем панель верхнюю
     */
    /*$('.js-header-fixed').html( $('.site-header').html() );
    $(window).scroll(function(){
        if ( $(this).scrollTop() > 100 && $(window).width() > 1000 ) {
            $('.js-header-fixed').show();
        } else {
            $('.js-header-fixed').hide();
        }
    });*/

    $(window).scroll(function() {
        if ($(this).scrollTop() > 400 && $(window).width() > 1000) {
            $('.js-top-line').addClass('show');
        } else {
            $('.js-top-line').removeClass('show');
        }
    });


    /**
     * YouTube Like
     */
    $('.js-video-like-close').on('click', function(){
        $(this).parent().fadeOut(200);
    });


    /**
     * Menu Mobile
     */
     $('.menu-toggle').click(function(){
         $('.main-navigation').slideToggle();
     });

    $('.main-navigation a').click(function(){
        if ( $(this).parent().find('.sub-menu').length ) {
            $(this).parent().find('.sub-menu').slideToggle();
            return false;
        }
    });


    /**
     * Scroll to top
     */
    $(".js-scrolltop").click(function () {
        return $("body,html").animate({
            scrollTop: 0
        }, 500), !1
    });
    /*$(window).scroll(function () {
        $(this).scrollTop() > 100 ? $(".js-scrolltop").fadeIn() : $(".js-scrolltop").fadeOut()
    });*/

    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
            $(".js-scrolltop").addClass('show');
        } else {
            $(".js-scrolltop").removeClass('show');
        }
    });


    /**
     * Adaptive video
     */
    /*responsiveIframe();
    setTimeout(function(){
        responsiveIframe();
    }, 1000);
    setTimeout(function(){
        responsiveIframe();
    }, 3000);
    setTimeout(function(){
        responsiveIframe();
    }, 5000);
    setTimeout(function(){
        responsiveIframe();
    }, 10000);
    $(window).resize(function(){
        responsiveIframe();
    });*/

    function responsiveIframe() {
        /*$('.entry-content iframe').each(function(){
            if ( $(this).hasClass('instagram-media') ) return false;

            var small_height = Math.round( $(this).height() * (200 / $(this).width()) );

            // set small first for define parent width
            $(this).css({
                'width': 200,
                'height' : small_height
            });

            var iw = $(this).width();
            var ih = $(this).height();
            var ip = $(this).parent().width();
            var ipw = ip/iw;
            var ipwh = Math.round(ih*ipw);

            $(this).css({
                'width': ip,
                'height' : ipwh
            });
        });*/
    }


    /**
     * прилепление подвала к низу
     */
    stick_footer();
    setTimeout(function(){
        stick_footer();
    }, 500);
    setTimeout(function(){
        stick_footer();
    }, 1500);
    function stick_footer() {
        if ( screen.width < 997 ) return;
        var new_bottom = $('.site-footer').height() + 50;
        $('body').css('margin-bottom', new_bottom + 'px');
    }


    /**
     * Dropdown menu
     */
    var timer;

    if ( screen.width > 991 ) {
        jQuery('.menu .menu-item:has(ul)').hover(
            function () {
                jQuery(this).parent('ul').find('.sub-menu:visible').hide();
                jQuery(this).find('.sub-menu:first').fadeIn(100);
                clearTimeout(timer);
            },
            function () {
                timer = setTimeout(hideMenu, 400);
            }
        );
    }
    function hideMenu() { jQuery(".menu-item:has(ul) .sub-menu:visible").fadeOut(100); }


    /**
     * Social link share
     */
    $('body').on('click', '.js-share-link', function(){
        openWin($(this).data("uri"));
    });

    function openWin( url ) {
        var features, w = 626, h = 436;
        var top = (screen.height - h)/2, left = (screen.width - w)/2;
        if(top < 0) top = 0;
        if(left < 0) left = 0;
        features = 'top=' + top + ',left=' +left;
        features += ',height=' + h + ',width=' + w + ',resizable=no';
        open(url, 'displayWindow', features);
    }


    /**
     * Spoiler
     */
    $('.js-spoiler-box-title').click(function(){
        var $this = $(this);
        $this.toggleClass('active').next().slideToggle();
    })


    /**
     * Smiles
     */
    $('.js-comment-smiles img').click(function(){
        var $this = $(this);
        $('#comment').val( $('#comment').val() + ' ' + $this.prop('alt') + '' );
    });


    function set_cookie ( name, value, exp_s, path, domain, secure )
    {
        var cookie_string = name + "=" + escape ( value );
        if ( exp_s )
        {
            var expires = new Date();
            expires.setTime(expires.getTime() + exp_s * 1000);
            cookie_string += "; expires=" + expires.toGMTString();
        }

        if ( path )
            cookie_string += "; path=" + escape ( path );

        if ( domain )
            cookie_string += "; domain=" + escape ( domain );

        if ( secure )
            cookie_string += "; secure";

        document.cookie = cookie_string;
    }



    // возвращает cookie с именем name, если есть, если нет, то undefined
    function getCookie(name) {
        var matches = document.cookie.match(new RegExp(
            "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
        ));
        return matches ? decodeURIComponent(matches[1]) : undefined;
    }


    (function(hasClass) {

        jQuery.fn.hasClass = function hasClassRegExp( selector ) {
            if ( selector && typeof selector.test === "function" ) {
                for ( var i = 0, l = this.length; i < l; i++ ) {
                    var classNames = this[i].className.split( /\s+/ );
                    for ( var c = 0, cl = classNames.length; c < cl; c++ ) {
                        if (selector.test( classNames[c]) ) {
                            return true;
                        }
                    }
                }
                return false;
            } else {
                return hasClass.call(this, selector);
            }
        }

    })(jQuery.fn.hasClass);


});