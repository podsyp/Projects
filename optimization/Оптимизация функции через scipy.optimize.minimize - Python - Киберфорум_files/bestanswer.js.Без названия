function AJAX_KRBA(options)
{
    this.img_is_answer = options.img_is_answer;
    this.img_is_not_answer = options.img_is_not_answer;
    this.krba_set = null;
    this.krba_removepost = null;
    this.krba_removeall = null;
}

AJAX_KRBA.prototype.close_window = function()
{
    if(fetch_object('krba_window_container'))
    {
        fetch_object('krba_window_container').parentNode.removeChild(fetch_object('krba_window_container'));
    }
}

AJAX_KRBA.prototype.show_window = function(str)
{
     var Obj = fetch_object('krba_window_container');
     if(Obj)
     {
          this.close_window();
     }
     var div = document.createElement('div');
     div.id = 'krba_window_container';
     div.style.maxWidth = "800px";
     div.style.padding = "5px";
     div.className = 'tborder alt1 smallfont';
     div.style.position = (is_ie && !is_ie7) ? "absolute" : "fixed";
     div.style.zIndex = "100";
     div.innerHTML = str;

     var closew_image = new Image();
     closew_image.src = IMGDIR_MISC + "/cross.png";
     closew_image.style.padding = '0 0 0 5px';
     closew_image.className = 'inlineimg';
     closew_image.alt = '';
     closew_image.border = '0';
     closew_image.onmousedown = function()
     {
          AJAX_KRBA.prototype.close_window();
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
     return false;
}

AJAX_KRBA.prototype.set = function(obj, action)
{
    var threadid = parseInt(obj.getAttribute('data-threadid')),
    postid = parseInt(obj.getAttribute('data-postid'));
    if(!threadid || !postid)
    {
        return true;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = 'bestanswer.php',
        postData = 'do=setanswer&t=' + threadid + '&p=' + postid + '&action=' + action + '&ajax=1&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'content'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    obj.outerHTML = html[0].childNodes[0].nodeValue;
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
                        this.show_window(error_html);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            document.location = 'bestanswer.php?do=setanswer&t=' + threadid + '&p=' + postid + '&action=' + action;
            return true;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout,
            scope: this
        };
        if(YAHOO.util.Connect.isCallInProgress(this.krba_set))
        {
            YAHOO.util.Connect.abort(this.krba_set);
        }
        this.krba_set = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
    return false;
}

AJAX_KRBA.prototype.removepost = function(obj)
{
    var threadid = parseInt(obj.getAttribute('data-threadid')),
    postid = parseInt(obj.getAttribute('data-postid'));
    if(!threadid || !postid)
    {
        return true;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = 'bestanswer.php',
        postData = 'do=removepost&t=' + threadid + '&p=' + postid + '&ajax=1&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'content'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata"),
                    krba_count = parseInt(html[0].childNodes[0].nodeValue),
                    krba_btn = html[0].getAttribute('data-btnhtml');
                    if(krba_count)
                    {
                        var remove_obj = fetch_object('krba_removepost_' + postid);
                    }
                    else
                    {
                        var remove_obj = fetch_object('krba_posts_' + threadid);
                    }
                    if(remove_obj)
                    {
                        remove_obj.outerHTML = '';
                    }
                    var btn_obj = fetch_object('krba_setpost_' + postid);
                    if(btn_obj && krba_btn)
                    {
                        btn_obj.outerHTML = krba_btn;
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
                        this.show_window(error_html);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            document.location = 'bestanswer.php?do=removepost&t=' + threadid + '&p=' + postid;
            return true;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout,
            scope: this
        };
        if(YAHOO.util.Connect.isCallInProgress(this.krba_removepost))
        {
            YAHOO.util.Connect.abort(this.krba_removepost);
        }
        this.krba_removepost = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
    return false;
}

AJAX_KRBA.prototype.removeall = function(obj)
{
    var threadid = parseInt(obj.getAttribute('data-threadid'));
    if(!threadid)
    {
        return true;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = 'bestanswer.php',
        postData = 'do=removeall&t=' + threadid + '&ajax=1&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'content'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata"),
                    krba_count = parseInt(html[0].childNodes[0].nodeValue);
                    var remove_obj = fetch_object('krba_posts_' + threadid);
                    if(remove_obj)
                    {
                        remove_obj.outerHTML = '';
                    }
                    var tbls = fetch_tags(fetch_object('posts'), 'table');
                    for(var i = 0; i < tbls.length; i++)
                    {
                        if(tbls[i].hasChildNodes() && tbls[i].id && tbls[i].id.substr(0, 4) == 'post')
                        {
                            var anchors = fetch_tags(tbls[i], 'a');
                            for(var j = 0; j < anchors.length; j++)
                            {
                                if(anchors[j].id && anchors[j].id.substr(0, 13) == 'krba_setpost_')
                                {
                                    var details = anchors[j].id.split('_'),
                                    btn_obj = fetch_object('krba_setpost_' + details[2]);
                                    if(btn_obj)
                                    {
                                        btn_obj.outerHTML = '<a id="krba_setpost_' + details[2] + '" data-threadid="' + threadid + '" data-postid="' + details[2] + '" onclick="KRBA.set(this, \'is_answer\'); return false;" href="bestanswer.php?do=setanswer&amp;action=is_answer&amp;t=' + threadid + '&amp;p=' + details[2] + '"><img src="' + this.img_is_answer + '" alt="" border="0" /></a>';
                                    }
                                }
                            }
                        }
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
                        this.show_window(error_html);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            document.location = 'bestanswer.php?do=removeall&t=' + threadid;
            return true;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout,
            scope: this
        };
        if(YAHOO.util.Connect.isCallInProgress(this.krba_removeall))
        {
            YAHOO.util.Connect.abort(this.krba_removeall);
        }
        this.krba_removeall = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
    return false;
}
