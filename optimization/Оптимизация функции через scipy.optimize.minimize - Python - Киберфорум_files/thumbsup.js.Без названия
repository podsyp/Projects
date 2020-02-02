var add_thumb = null, remove_thumb = null, view_thumbs = null, delete_thumb = null, user_rate = null, show_form = null;
function krthumbs_grayOut(vis, options)
{
    var options = options || {};
    var zindex = options.zindex || 50;
    var opacity = options.opacity || 65;
    var opaque = (opacity / 100);
    var bgcolor = options.bgcolor || '#000000';
    var dark = YAHOO.util.Dom.get('krthumbs_darkenScreenObject');
    if(!dark)
    {
        var tbody = document.getElementsByTagName("body")[0];
        var tnode = document.createElement('div'); // Create the layer.
        tnode.style.position = 'absolute';         // Position absolutely
        tnode.style.top = '0px';                   // In the top
        tnode.style.left = '0px';                  // Left corner of the page
        tnode.style.overflow = 'hidden';           // Try to avoid making scroll bars
        tnode.style.display = 'none';              // Start out Hidden
        tnode.id = 'krthumbs_darkenScreenObject';  // Name it so we can find it later
        tnode.onclick = function ()
        {
            krthumbs_close_window();
        }
        tbody.appendChild(tnode);                            // Add it to the web page
        dark = YAHOO.util.Dom.get('krthumbs_darkenScreenObject');  // Get the object.
    }
    if(vis)
    {
        // Calculate the page width and height
        if(document.body && document.body.scrollHeight)
        {
            var pageHeight = document.body.scrollHeight + 'px';
        }
        else if(document.body.offsetWidth)
        {
            var pageHeight = document.body.offsetHeight + 'px';
        }
        else
        {
            var pageHeight = '100%';
        }
        //set the shader to cover the entire page and make it visible.
        dark.style.opacity = opaque;
        dark.style.MozOpacity = opaque;
        dark.style.filter = 'alpha(opacity='+opacity+')';
        dark.style.zIndex = zindex;
        dark.style.backgroundColor = bgcolor;
        dark.style.width = '100%';
        dark.style.height = pageHeight;
        dark.style.display = 'block';
        if(is_ie)
        {
            krthumbs_showhide_selects(false);
        }
    }
    else
    {
        dark.style.display = 'none';
        if(is_ie)
        {
            krthumbs_showhide_selects(true);
        }
    }
}

function krthumbs_showhide_selects(visible)
{
    var selects = document.getElementsByTagName("select");
    if(selects.length)
    {
        var old = {};
        for(var i = 0; i < selects.length; i++)
        {
            old[i] = selects[i].style.cssText;
            if(visible)
            {
                selects[i].style.cssText = old[i];
                selects[i].style.display = '';
            }
            else
            {
                selects[i].style.display = 'none';
            }
        }
    }
}
function krthumbs_close_window()
{
    krthumbs_grayOut(false);
    if(YAHOO.util.Dom.get('krthumbs_window_container'))
    {
        YAHOO.util.Dom.get('krthumbs_window_container').parentNode.removeChild(YAHOO.util.Dom.get('krthumbs_window_container'));
    }
}
function krthumbs_show_window(str, showError)
{
    var win = YAHOO.util.Dom.get('krthumbs_window_container');
    if(win)
    {
        krthumbs_close_window();
    }
    var div = document.createElement('div');
    div.id = 'krthumbs_window_container';
    if(showError)
    {
        div.style.border = '1px solid red';
    }
    div.style.maxWidth = "600px";
    div.style.minWidth = "400px";
    div.style.padding = "0 3px 3px 0";
    div.className = 'tborder alt1 smallfont thumbs-shadow';
    div.style.position = (is_ie && !is_ie7) ? "absolute" : "fixed";
    div.style.zIndex = "100";
    div.innerHTML = str;
    var closew_image = new Image();
    closew_image.src = IMGDIR_MISC + "/cross.png";
    closew_image.style.padding = '0 0 0 3px';
    closew_image.style.position = 'absolute';
    closew_image.style.top = '3px';
    closew_image.style.right = '3px';
    closew_image.className = 'inlineimg';
    closew_image.alt = '';
    closew_image.border = '0';
    closew_image.onmousedown = function()
    {
        krthumbs_close_window();
        return false;
    }
    var elm_a = document.createElement('a');
    elm_a.href = '#';
    elm_a.title = 'Close Window';
    elm_a.style.cssFloat = 'right';
    elm_a.appendChild(closew_image);
    div.appendChild(elm_a);
    document.body.appendChild(div);
    center_element(div);
    krthumbs_grayOut(true);
    return false;
}

function krthumbs_add_comment(postid, thumb)
{
    krthumbs_close_window();
    thumbsobj = YAHOO.util.Dom.get('thumbs_box_' + postid);
    if(!thumbsobj)
    {
        return false;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = 'thumbs.php',
        postData = 'do=showform&ajax=1&postid=' + postid + '&thumb=' + thumb + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    krthumbs_show_window(html[0].childNodes[0].nodeValue);
                }
                else
                {
                    var errors = ajax.responseXML.getElementsByTagName('error');
                    if(errors.length)
                    {
                        var error_html = '<ol>';
                        for(i = 0; i < errors.length; i++)
                        {
                            error_html += '<li>' + errors[i].firstChild.nodeValue + '</li>';
                        }
                        error_html += '</ol>';
                        krthumbs_show_window(error_html, true);
                        setTimeout("krthumbs_close_window()", 6000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            return true;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(show_form))
        {
            YAHOO.util.Connect.abort(show_form);
        }
        show_form = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
};

function krthumbs_add(postid, thumb)
{
    var comment = '',
    commentobj = YAHOO.util.Dom.get('thumbs_text_comment_' + postid);
    if(commentobj && commentobj.value != '')
    {
        comment = PHP.urlencode(commentobj.value);
    }
    krthumbs_close_window();
    thumbsobj = YAHOO.util.Dom.get('thumbs_box_' + postid);
    if(!thumbsobj)
    {
        return false;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = 'thumbs.php',
        postData = 'do=add&ajax=1&postid=' + postid + '&thumb=' + thumb + '&comment=' + comment + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    thumbsobj.outerHTML = html[0].childNodes[0].nodeValue;
                }
                else
                {
                    var errors = ajax.responseXML.getElementsByTagName('error');
                    if(errors.length)
                    {
                        var error_html = '<ol>';
                        for(i = 0; i < errors.length; i++)
                        {
                            error_html += '<li>' + errors[i].firstChild.nodeValue + '</li>';
                        }
                        error_html += '</ol>';
                        krthumbs_show_window(error_html, true);
                        setTimeout("krthumbs_close_window()", 6000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            return true;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(add_thumb))
        {
            YAHOO.util.Connect.abort(add_thumb);
        }
        add_thumb = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
};

function krthumbs_remove(btnobj, postid)
{
    krthumbs_close_window();
    var thumbsobj = YAHOO.util.Dom.get('thumbs_box_' + postid),
    thumbid = btnobj.getAttribute('data-thumbid');
    this.thumbsobj = thumbsobj;
    if(!thumbsobj || !thumbid)
    {
        return false;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = 'thumbs.php',
        postData = 'do=remove&ajax=1&postid=' + postid + '&thumbid=' + thumbid + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    thumbsobj.outerHTML = html[0].childNodes[0].nodeValue;
                }
                else
                {
                    var errors = ajax.responseXML.getElementsByTagName('error');
                    if(errors.length)
                    {
                        var error_html = '<ol>';
                        for(i = 0; i < errors.length; i++)
                        {
                            error_html += '<li>' + errors[i].firstChild.nodeValue + '</li>';
                        }
                        error_html += '</ol>';
                        krthumbs_show_window(error_html, true);
                        setTimeout("krthumbs_close_window()", 6000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            return true;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(remove_thumb))
        {
            YAHOO.util.Connect.abort(remove_thumb);
        }
        remove_thumb = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
};
function krthumbs_view(postid, page)
{
    krthumbs_close_window();
    if(!postid)
    {
        return false;
    }
    if(!page)
    {
        page = 1;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = 'thumbs.php',
        postData = 'do=view&ajax=1&postid=' + postid + '&page=' + page + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    krthumbs_show_window(html[0].childNodes[0].nodeValue);
                }
                else
                {
                    var errors = ajax.responseXML.getElementsByTagName('error');
                    if(errors.length)
                    {
                        var error_html = '<ol>';
                        for(i = 0; i < errors.length; i++)
                        {
                            error_html += '<li>' + errors[i].firstChild.nodeValue + '</li>';
                        }
                        error_html += '</ol>';
                        krthumbs_show_window(error_html, true);
                        setTimeout("krthumbs_close_window()", 6000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krthumbs_show_window('<div class="thumbs-ajax-error">AJAX Error! Try later please...</div>');
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(view_thumbs))
        {
            YAHOO.util.Connect.abort(view_thumbs);
        }
        view_thumbs = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
};
function krthumbs_delete(elmobj, posneg)
{
    krthumbs_close_window();
    var postid = elmobj.getAttribute('data-postid'),
    thumbid = elmobj.getAttribute('data-thumbid'),
    thumbsobj = YAHOO.util.Dom.get('thumbs_box_' + postid);
    this.thumbsobj = thumbsobj;
    if(!postid)
    {
        return false;
    }
    else if(posneg == 0 && (!thumbid || !postid))
    {
        return false;
    }
    if(posneg > 0 || posneg < 0)
    {
        thumbid = 0;
        var confirm_delete = posneg > 0 ? krthumbs['confirm_delete_pos'] : krthumbs['confirm_delete_neg'];
        if(!confirm(confirm_delete))
        {
            return false;
        }
    }
    else if(thumbid)
    {
        posneg = 0;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = 'thumbs.php',
        postData = 'do=delete&ajax=1&postid=' + postid + '&thumbid=' + thumbid + '&posneg=' + posneg + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata"),
                    thumbs = parseInt(html[0].getAttribute('thumbs')),
                    ratedata = ajax.responseXML.documentElement.getElementsByTagName("ratedata");
                    krthumbs_show_window(html[0].childNodes[0].nodeValue);
                    thumbsobj.outerHTML = ratedata[0].childNodes[0].nodeValue;
                    if(thumbs <= 0)
                    {
                        setTimeout("krthumbs_close_window()", 3000);
                    }
                }
                else
                {
                    var errors = ajax.responseXML.getElementsByTagName('error');
                    if(errors.length)
                    {
                        var error_html = '<ol>';
                        for(i = 0; i < errors.length; i++)
                        {
                            error_html += '<li>' + errors[i].firstChild.nodeValue + '</li>';
                        }
                        error_html += '</ol>';
                        krthumbs_show_window(error_html, true);
                        setTimeout("krthumbs_close_window()", 6000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krthumbs_show_window('<div class="thumbs-ajax-error">AJAX Error! Try later please...</div>');
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(delete_thumb))
        {
            YAHOO.util.Connect.abort(delete_thumb);
        }
        delete_thumb = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
};
function krthumbs_user_rate(userid)
{
    krthumbs_close_window();
    if(!userid)
    {
        return false;
    }

    if(AJAX_Compatible)
    {
        var sendUrl = 'thumbs.php',
        postData = 'do=userate&ajax=1&userid=' + userid + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    krthumbs_show_window(html[0].childNodes[0].nodeValue);
                }
                else
                {
                    var errors = ajax.responseXML.getElementsByTagName('error');
                    if(errors.length)
                    {
                        var error_html = '<ol>';
                        for(i = 0; i < errors.length; i++)
                        {
                            error_html += '<li>' + errors[i].firstChild.nodeValue + '</li>';
                        }
                        error_html += '</ol>';
                        krthumbs_show_window(error_html, true);
                        setTimeout("krthumbs_close_window()", 6000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krthumbs_show_window('<div class="thumbs-ajax-error">AJAX Error! Try later please...</div>');
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(user_rate))
        {
            YAHOO.util.Connect.abort(user_rate);
        }
        user_rate = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
};
