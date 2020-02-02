jQuery.extend(jQuery.fn, {
	toplinkwidth: function(){
		var totalContentWidth = jQuery('#content').outerWidth(); // ширина блока с контентом, включая padding
		var totalTopLinkWidth = jQuery(this).children('a').outerWidth(true); // ширина самой кнопки наверх, включая padding и margin
		var h = jQuery(window).width()/2-totalContentWidth/2-totalTopLinkWidth;
		if(h<0){
			// если кнопка не умещается, скрываем её
			jQuery(this).hide();
			return false;
		} else {
			if(jQuery(window).scrollTop() >= 1){
				jQuery(this).show();
			}
			//jQuery(this).css({'padding-right': h+'px'});
			jQuery(this).css({'width': '25px'});
			jQuery(this).css({'opacity': '0.6'});
			return true;
		}
	}
});
 
jQuery(function($){
	var topLink = $('#top-link');
	topLink.css({'padding-bottom': $(window).height()});
	// если вам не нужно, чтобы кнопка подстраивалась под ширину экрана - удалите следующие четыре строчки в коде
	//topLink.toplinkwidth();
	//$(window).resize(function(){
	//	topLink.toplinkwidth();
	//});
	$(window).scroll(function() {
		if($(window).scrollTop() >= 1 && topLink.toplinkwidth()) {
			topLink.fadeIn(300);
		} else {
			topLink.fadeOut(300);
		}
	});
	topLink.click(function(e) {
		$("body,html").animate({scrollTop: 0}, 100);
		return false;
	});
});