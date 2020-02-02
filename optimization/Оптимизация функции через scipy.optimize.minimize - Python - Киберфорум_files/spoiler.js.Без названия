function initSpoilers(context)
{
    var context = context || 'body';
    $('div.spoiler-head', $(context))
        .unbind('click')
        .click(function(){
            $(this).toggleClass('unfolded');
            $(this).next('div.spoiler-body').slideToggle('fast');
        })
    ;
}
 
$(document).ready(function(){
    initSpoilers('body');
});