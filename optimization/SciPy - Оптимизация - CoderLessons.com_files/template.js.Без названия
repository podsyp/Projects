/**
*	Theme main theme Frontend JavaScript file
*/
(function($){
$(document).ready(function() {

	'use strict';

	// iOS buttons style fix
	var platform = navigator.platform;

    if (platform === 'iPad' || platform === 'iPhone' || platform === 'iPod') {
        $('input.button, input[type="text"], input[type="button"], input[type="password"], textarea, input.input-text').css('-webkit-appearance', 'none');
    }

	// Disable animations for touch devices
	if(isTouchDevice()===true) {
	    $("#animations-css").remove();
	}

	// Select restyling
	$("select").select2({
		allowClear: true,
		minimumResultsForSearch: 10
	});

	// Init elements appear animations
	AOS.init({
		once: true
	});

	// Add body class for title header with background
	if($("body.single-post .container-page-item-title.with-bg, body.page .container-page-item-title.with-bg").length > 0) {
		$("body").addClass('blog-post-header-with-bg');
	}

	// Remove embed responsive container from Gutenberg elements, except Video
	$('.wp-block-embed:not(.is-type-video) .embed-container').removeClass('embed-container');

	// Add images backgrounds
	$('.saxon-post-image').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});
	$('.saxon-next-post').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});
	$('.sidebar .widget.widget_saxon_text .saxon-textwidget').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});
	$('.container-page-item-title').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});
	$('.saxon-featured-categories-wrapper .saxon-featured-category').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});
	$('.saxon-featured-categories-wrapper .saxon-featured-category a').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});
	$('.sidebar .widget .post-categories a').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});
	$('.saxon-post .post-categories a').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});
	$('.footer-html-block').each(function( index ) {
		$(this).attr('style', ($(this).attr('data-style')));
	});

	// Move WooCommerce sale badge
	$('.woocommerce.single span.onsale').prependTo($('.woocommerce div.product div.images.woocommerce-product-gallery'));

	// Mini search form behaviour
	$('.search-toggle-wrapper.search-header .search-toggle-btn').on('click', function(e){

		if($('.search-toggle-wrapper .searchform input[type="search"]').val() !== '') {
			$('.search-toggle-wrapper .searchform .submit').click();
		}
	});

	// Fullscreen search form behaviour
	$('.search-toggle-wrapper.search-fullscreen .search-toggle-btn').on('click', function(e){

		$(document).keyup(function(e){
		    if(e.keyCode === 27)
		        $('.search-fullscreen-wrapper').fadeOut();
		});

		$('.search-fullscreen-wrapper').fadeIn();
		$('.search-fullscreen-wrapper .search-fullscreen-form input[type="search"]').focus();
		$('.search-fullscreen-wrapper .search-fullscreen-form input[type="search"]').val('');
	});

	$('.search-close-btn').on('click', function(e){
		$('.search-fullscreen-wrapper').fadeOut();
	});

	// Main menu toggle button
	$('header .mainmenu-mobile-toggle').on('click', function(e){
		$('header .navbar-toggle').click();
	});

	// Top mobile menu
	var topmenuopened = 0;
	$( document ).on( "click", ".menu-top-menu-container-toggle", function(e) {
		if(topmenuopened == 0) {
			$(this).next().slideDown();
			topmenuopened = 1;
		} else {
			topmenuopened = 0;
			$(this).next().slideUp();
		}
	});

	// Mobile menu clicks for top and main menus
	$('.nav li > a, .header-menu li > a').on('click', function(e){

		if($(window).width() < 991) {

			// Open dropdown on click
			if ( $(this).next(".sub-menu").length > 0 ) {
				var sm = $(this).next(".sub-menu");

				if(sm.data('open') !== 1) {
					e.preventDefault();
					e.stopPropagation();

					sm.slideDown();

					sm.data('open', 1);

					$(this).parent().addClass('mobile-submenu-opened');

				} else {
					// Close dropdown if no href in link
					if($(this).attr('href') == '#') {
						e.preventDefault();
						e.stopPropagation();

						sm.slideUp();

						sm.data('open', 0);

						$(this).parent().removeClass('mobile-submenu-opened');
					}
				}

			}
		} else {
			// Mobile menu clicks for touch devices
			if(isTouchDevice()===true) {

				if ( $(this).next(".sub-menu").length > 0 ) {
					var sm = $(this).next(".sub-menu");

					if(sm.data('open') !== 1) {
						e.preventDefault();
						e.stopPropagation();

						sm.slideDown();

						sm.data('open', 1);
					}

				}

			}

		}
	});

	// Sidebar menu widget clicks
	$('.sidebar .widget.widget_nav_menu a').on('click', function(e){

			if ( $(this).next(".sub-menu").length > 0 ) {
				var sm = $(this).next(".sub-menu");

				if(sm.data('open') !== 1)
				{
					e.preventDefault();
					e.stopPropagation();
					sm.slideDown();

					sm.data('open', 1);

					$(this).parent().addClass('mobile-submenu-opened');
				}

			}
	});

	// Cookie bar plugin restyle
	if($('#catapult-cookie-bar').length > 0) {
		$('#catapult-cookie-bar button').addClass('btn');
	}

	/**
	*	Scroll related functions
	*/

	// Calculations in Single post page
	if($('.single-post').length > 0) {
		var post_container_height = $('.blog-post.blog-post-single').height();
		var post_container_top = $('.blog-post.blog-post-single').offset().top;
		var post_container_bottom = post_container_top + post_container_height;
	}

	// Post reading progress for single post page
	if($('.single-post .blog-post-reading-progress').length > 0) {

		var current_position_inside_post = 0;
		var current_progress = 0;

		$(window).scroll(function () {

			current_position_inside_post = $(window).scrollTop() - post_container_top;
			current_progress = current_position_inside_post * 100 / post_container_height;

			if(current_progress > 100) {
				current_progress = 100;
			}

			if(current_progress < 0) {
				current_progress = 0;
			}

			$('.blog-post-reading-progress').width(current_progress + '%');

		});
	}

	// Fixed social share for single post page
	if($('.single-post .saxon-social-share-fixed').length > 0) {

		var current_position_inside_post2 = 0;
		var current_progress2 = -1;

		saxon_fixedSocialWorker();

		$(window).scroll(function () {

			saxon_fixedSocialWorker();

		});
	}

	function saxon_fixedSocialWorker() {

		if(post_container_height > $('.single-post .saxon-social-share-fixed').height()) {
			current_position_inside_post2 = $(window).scrollTop() - post_container_top;

			current_progress2 = current_position_inside_post2 * 100 / (post_container_height - $('.single-post .saxon-social-share-fixed').height());


			if(current_progress2 > 100) {


				$('.single-post .saxon-social-share-fixed').css('position', 'absolute');
				$('.single-post .saxon-social-share-fixed').css('bottom', 0);
				$('.single-post .saxon-social-share-fixed').css('top', 'auto');
				$('.single-post .saxon-social-share-fixed').css('opacity', 0);

			} else if(current_progress2 > 90) {
				$('.single-post .saxon-social-share-fixed').css('opacity', 0);
			} else if(current_progress2 < 0) {

				$('.single-post .saxon-social-share-fixed').css('position', 'absolute');
				$('.single-post .saxon-social-share-fixed').css('bottom', 'auto');
				$('.single-post .saxon-social-share-fixed').css('top', 0);
				$('.single-post .saxon-social-share-fixed').css('margin-top', 0);
				$('.single-post .saxon-social-share-fixed').css('opacity', 1);

			} else {

				$('.single-post .saxon-social-share-fixed').css('position', 'fixed');
				$('.single-post .saxon-social-share-fixed').css('bottom', 'auto');
				$('.single-post .saxon-social-share-fixed').css('top', 0);
				$('.single-post .saxon-social-share-fixed').css('margin-top', '200px');
				$('.single-post .saxon-social-share-fixed').css('opacity', 1);

			}
		}

	}

	// Scroll to top button
	var scrollonscreen = 0;

	$(window).scroll(function () {
		scrollonscreen = $(window).scrollTop() + $(window).height();

		if(scrollonscreen > $(window).height() + 350){
			$('.scroll-to-top').css("bottom", "60px");
		}
		else {
			$('.scroll-to-top').css("bottom", "-60px");
		}

	});

	// Scroll to top animation
	$('.scroll-to-top').on('click', function(e){
		$('body,html').stop().animate({
			scrollTop:0
		},800,'easeOutCubic')
		return false;
	});

	// Sticky header
	if($(window).width() > 991 && !isTouchDevice()) {

		var $stickyheader = $('header.main-header.sticky-header');
		var STICKY_HEADER_OFFSET = 500; // Offest after header to show sticky version

		if($stickyheader.length > 0) {
			var $fixedheader = $stickyheader.clone();
		   	$fixedheader.insertAfter($stickyheader);
		   	$fixedheader.addClass('fixed');

		   	if($("#wpadminbar").length > 0) {
		   		$fixedheader.css('top', $("#wpadminbar").height());
		   	}

			$(window).scroll(function() {

			    if ($(window).scrollTop() > $stickyheader.offset().top + STICKY_HEADER_OFFSET) {
			        $fixedheader.fadeIn();
			    } else {
			        $fixedheader.fadeOut('fast');
			    }
			});
		}
	}


	/**
	*	Resize events
	*/

	$(window).resize(function () {

	});

	/**
	* Social share for posts
	*/

	function saxon_socialshare(type, post_url, post_title, post_image) {

		switch (type) {
		  case 'facebook':
		    window.open( 'https://www.facebook.com/sharer/sharer.php?u='+post_url, "facebookWindow", "height=380,width=660,resizable=0,toolbar=0,menubar=0,status=0,location=0,scrollbars=0" );
		    break;
		  case 'google':
		    window.open( 'https://plus.google.com/share?url='+post_url, "googleplusWindow", "height=380,width=660,resizable=0,toolbar=0,menubar=0,status=0,location=0,scrollbars=0" );
		    break;
		  case 'twitter':
		    window.open( 'http://twitter.com/intent/tweet?text='+post_title + ' ' + post_url, "twitterWindow", "height=370,width=600,resizable=0,toolbar=0,menubar=0,status=0,location=0,scrollbars=0" );
		    break;
		  case 'pinterest':
		    window.open( 'http://pinterest.com/pin/create/button/?url='+post_url+'&media='+post_image+'&description='+post_title, "pinterestWindow", "height=620,width=600,resizable=0,toolbar=0,menubar=0,status=0,location=0,scrollbars=0" );
		    break;
		  case 'whatsapp':
		    window.open( 'https://api.whatsapp.com/send?text='+post_title+' '+post_url, "whatsupWindow", "height=620,width=600,resizable=0,toolbar=0,menubar=0,status=0,location=0,scrollbars=0" );
			break;
		  case 'vk':
		    window.open( 'https://vk.com/share.php?url='+post_url+'&title='+post_title+'&description=&image='+post_image, "vkWindow", "height=620,width=600,resizable=0,toolbar=0,menubar=0,status=0,location=0,scrollbars=0" );
			break;
		  case 'linkedin':
		    window.open( 'https://www.linkedin.com/shareArticle?url='+post_url+'&title='+post_title, "linkedinWindow", "height=620,width=600,resizable=0,toolbar=0,menubar=0,status=0,location=0,scrollbars=0" );
			break;
		  default:

		}

		return false;
	}

	$('.post-social a').on('click', function(e){

		if($(this).data('type') !== 'link') {
			e.preventDefault();
			e.stopPropagation();

			var share_type = $(this).data('type');
			var post_image = $(this).data('image');
			var post_title = encodeURIComponent($(this).data('title'));
			var post_url = $(this).attr('href');

			saxon_socialshare(share_type, post_url, post_title, post_image);
		}

	});

	/**
	*	Other scripts
	*/

	/**
	*	Common functions
	*/

	// Check for touch device
    function isTouchDevice(){
	    return true == ("ontouchstart" in window || window.DocumentTouch && document instanceof DocumentTouch);
	}

});
})(jQuery);

// Global functions
'use strict';

/* Cookie functions */
function setCookie(name,value,days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else var expires = "";
    document.cookie = name+"="+value+expires+"; path=/";
}

function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}
