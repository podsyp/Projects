var addfield_ajax = null,
deleteanswer_ajax = null,
saveedit_ajax = null,
switchfields_ajax = null,
preview_ajax = null
postanswer_ajax = null,
deletefield_ajax = null,
finishtest_ajax = null,
showresult_ajax = null,
postcert_ajax = null;

function krtsts_showhide_selects(visible)
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

function krtsts_grayOut(vis, options)
{
    var options = options || {};
    var zindex = options.zindex || 50;
    var opacity = options.opacity || 65;
    var opaque = (opacity / 100);
    var bgcolor = options.bgcolor || '#000000';
    var dark = YAHOO.util.Dom.get('krtsts_darkenScreenObject');
    if(!dark)
    {
        var tbody = document.getElementsByTagName("body")[0];
        var tnode = document.createElement('div');           // Create the layer.
        tnode.style.position = 'absolute';                 // Position absolutely
        tnode.style.top = '0px';                           // In the top
        tnode.style.left = '0px';                          // Left corner of the page
        tnode.style.overflow = 'hidden';                   // Try to avoid making scroll bars
        tnode.style.display = 'none';                      // Start out Hidden
        tnode.id = 'krtsts_darkenScreenObject';                   // Name it so we can find it later
        tnode.onclick = function ()
        {
            krtsts.close_window();
        }
        tbody.appendChild(tnode);                            // Add it to the web page
        dark = YAHOO.util.Dom.get('krtsts_darkenScreenObject');  // Get the object.
    }
    if(vis)
    {
        // Calculate the page width and height
        if(document.body && (document.body.scrollWidth || document.body.scrollHeight))
        {
            var pageWidth = document.body.scrollWidth + 'px',
            pageHeight = document.body.scrollHeight + 'px';
        }
        else if(document.body.offsetWidth)
        {
            var pageWidth = document.body.offsetWidth + 'px',
            pageHeight = document.body.offsetHeight + 'px';
        }
        else
        {
            var pageWidth = '100%',
            pageHeight = '100%';
        }
        //set the shader to cover the entire page and make it visible.
        dark.style.opacity = opaque;
        dark.style.MozOpacity = opaque;
        dark.style.filter = 'alpha(opacity='+opacity+')';
        dark.style.zIndex = zindex;
        dark.style.backgroundColor = bgcolor;
        dark.style.width = pageWidth;
        dark.style.height = pageHeight;
        dark.style.display = 'block';
        if(is_ie)
        {
            krtsts_showhide_selects(false);
        }
    }
    else
    {
        dark.style.display = 'none';
        if(is_ie)
        {
            krtsts_showhide_selects(true);
        }
    }
}

function krtsts_load_jscssfile(filename, filetype)
{
    if(filetype == 'js')
    {   //if filename is a external JavaScript file
        var fileref = document.createElement('script')
        fileref.setAttribute("type", "text/javascript")
        fileref.setAttribute("src", filename)
    }
    else if(filetype == 'css')
    {   //if filename is an external CSS file
        var fileref = document.createElement("link")
        YAHOO.util.Dom.setAttribute(fileref, "rel", "stylesheet")
        YAHOO.util.Dom.setAttribute(fileref, "type", "text/css")
        YAHOO.util.Dom.setAttribute(fileref, "href", filename)
    }
    if(typeof fileref != "undefined")
    {
        document.getElementsByTagName("head")[0].appendChild(fileref);
    }
}

function krtsts_ctrl()
{
    this.answersPlaceHolder = YAHOO.util.Dom.get('question_answers');
    this.formid = krtsts['form_id'];
    this.formname = krtsts['form_name'];
    this.bburl = krtsts['bburl'];
    this.answers_count = krtsts['answers_count'];
    this.last_answerid = krtsts['last_answerid'];
    this.max_answerid = this.last_answerid;
    this.wait = krtsts['wait'];
    this.yesno = [];
    this.confirm_form_sent = (krtsts['confirm_form_sent']) ? krtsts['confirm_form_sent'] : 'Continue?';
}

krtsts_ctrl.prototype.strlen = function(string)
{
    return string.length;
}

krtsts_ctrl.prototype.count_chars = function(obj)
{
    var bg0 = '#C7C7C7', bg10 = '#2DDA2F', bg20 = '#CCF576', bg30 = '#EDC431', bg40 = '#EDA831',
    bg50 = '#ED8932', bg60 = '#ED7032', bg70 = '#C23308', bg80 = '#C2081E', bg90 = '#F70202', bg100 = '#ED2809',
    chrCount = this.strlen(obj.value),
    maxChars = parseInt(obj.getAttribute('data-max-chars')),
    counterObjID = obj.getAttribute('data-counterid'),
    progressObjID = obj.getAttribute('data-progressid'),
    chrPrcnt = (chrCount / maxChars * 100),
    rest = parseInt(maxChars - chrCount),
    cntObj = YAHOO.util.Dom.get(counterObjID),
    prgsObj = YAHOO.util.Dom.get(progressObjID);
    if(!cntObj || !prgsObj)
    {
        return;
    }
    if(chrPrcnt >= 100)
    {
        chrPrcnt = 100;
    }
    if(chrPrcnt <= 10)
    {
        prgsObj.style.backgroundColor = bg10;
    }
    if(chrPrcnt > 10 && chrPrcnt <= 20)
    {
        prgsObj.style.backgroundColor = bg20;
    }
    if(chrPrcnt > 20 && chrPrcnt <= 30)
    {
        prgsObj.style.backgroundColor = bg30;
    }
    if(chrPrcnt > 30 && chrPrcnt <= 40)
    {
        prgsObj.style.backgroundColor = bg40;
    }
    if(chrPrcnt > 40 && chrPrcnt <= 50)
    {
        prgsObj.style.backgroundColor = bg50;
    }
    if(chrPrcnt > 50 && chrPrcnt <= 60)
    {
        prgsObj.style.backgroundColor = bg60;
    }
    if(chrPrcnt > 60 && chrPrcnt <= 70)
    {
        prgsObj.style.backgroundColor = bg70;
    }
    if(chrPrcnt > 70 && chrPrcnt <= 80)
    {
        prgsObj.style.backgroundColor = bg80;
    }
    if(chrPrcnt > 80 && chrPrcnt <= 90)
    {
        prgsObj.style.backgroundColor = bg90;
    }
    if(chrPrcnt > 90)
    {
        prgsObj.style.backgroundColor = bg100;
    }
    prgsObj.style.width = chrPrcnt + '%';
    cntObj.innerHTML = rest;
}

krtsts_ctrl.prototype.recount_chars = function()
{
    var txtareaFileds = YAHOO.util.Dom.getElementsByClassName("tsts-counter-bits", "textarea");
    if(txtareaFileds.length)
    {
        for(var i = 0; i < txtareaFileds.length; i++)
        {
            krtsts.count_chars(txtareaFileds[i]);
        }
    }
}

krtsts_ctrl.prototype.switch_multiple = function(e, multiple)
{
    this.close_window();
    e = YAHOO.util.Event.getEvent(e);
    var targ = YAHOO.util.Event.getTarget(e),
    submitstring = this.get_submitstring(targ.form, 'tsts-field-name'),
    questionid = targ.getAttribute('data-questionid');
    if(!questionid)
    {
        return false;
    }
    if(!this.answersPlaceHolder)
    {
        this.show_window('Error! Try later...', true);
        return false;
    }
    
    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = 'do=switchfields&ajax=1&tstsquestionid=' + questionid
        + '&multiple=' + multiple
        + '&securitytoken=' + SECURITYTOKEN
        + submitstring,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    krtsts.answersPlaceHolder.innerHTML = html[0].childNodes[0].nodeValue;
                    krtsts.recount_chars();
                    krtsts.count_fields();
                    return false;
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
                        krtsts.show_window(error_html, true);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(switchfields_ajax))
        {
            YAHOO.util.Connect.abort(switchfields_ajax);
        }
        switchfields_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
    return false;
}
krtsts_ctrl.prototype.get_yesno = function()
{
    var ynFields = YAHOO.util.Dom.getElementsByClassName("tsts-fieldblock-yesno", "input", 'block_yesno');
    if(ynFields.length)
    {
        for(i = 0; i < ynFields.length; i++)
        {
            var field = ynFields[i];
            this.yesno[field.id] = field.checked ? 1 : 0;
        }
    }
}
krtsts_ctrl.prototype.field_wrapper = function(blockContent, max_answerid)
{
    var div = document.createElement('div');
    div.className = 'tsts-fieldblock-bit';
    div.id = 'aedit_' + max_answerid;
    div.setAttribute('data-answerid', max_answerid);
    div.innerHTML = blockContent;
    return div;
}
krtsts_ctrl.prototype.count_fields = function()
{
    var fields = this.get_fields(), answerids = [];
    if(fields.length)
    {
        this.answers_count = fields.length;
        for(var i = 0; i < fields.length; i++)
        {
            var findex = (i + 1),
            cObj = YAHOO.util.Dom.get('aedit_akey_' + fields[i].getAttribute('data-answerid'));
            if(cObj)
            {
                cObj.innerHTML = '#' + findex;
            }
            fields[i].setAttribute('data-counter', findex);
            answerids[i] = fields[i].getAttribute('data-answerid');
            this.max_answerid = Math.max(answerids[i]);
        }
    }
}
krtsts_ctrl.prototype.get_submitstring = function(blockobj, classname)
{
    fields = null;
    if(classname)
    {
        fields = YAHOO.util.Dom.getElementsByClassName(classname, '', blockobj.id);
    }
    else
    {
        fields = document.forms[this.formname].elements;
    }
    if(fields.length)
    {
        var submitstring = '';
        for(var i = 0; i < fields.length; i++)
        {
            if(fields[i].type == undefined || fields[i].type == 'fieldset')
            {
                continue;
            }
            switch(fields[i].type)
            {
                case 'text':
                case 'textarea':
                case 'hidden':
                  submitstring += '&' + fields[i].name + '=' + PHP.urlencode(fields[i].value);
                break;
                case 'number':
                  submitstring += '&' + fields[i].name + '=' + parseInt(fields[i].value);
                case 'checkbox':
                case 'radio':
                  submitstring += fields[i].checked ? '&' + fields[i].name + '=' + PHP.urlencode(fields[i].value) : '';
                break;
                case 'select-one':
                  submitstring += '&' + fields[i].name + '=' + PHP.urlencode(fields[i].options[fields[i].selectedIndex].value);
                break;
                case 'select-multiple':
                  for(var j = 0; j < fields[i].options.length; j++)
                  {
                      submitstring += (fields[i].options[j].selected ? '&' + fields[i].name + '=' + PHP.urlencode(fields[i].options[j].value) : '');
                  }
                break;
            }
        }
        return submitstring;
    }
    return false;
};

krtsts_ctrl.prototype.verify_form = function(formobj)
{
    var fields = document.forms[formobj.name].elements;
    if(fields.length)
    {
        var field_checked = 0;
        for(var i = 0; i < fields.length; i++)
        {
            if(fields[i].type == 'checkbox' || fields[i].type == 'radio')
            {
                console.log(fields[i].type);
                if(fields[i].checked)
                {
                    field_checked++;
                }
            }
        }
        if(!field_checked)
        {
            if(confirm(this.confirm_form_sent))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return true;
        }
    }
    return true;
};

krtsts_ctrl.prototype.show_result = function(dataObj)
{
    this.close_window();
    var elmid = parseInt(dataObj.getAttribute('data-elmid')),
    elmtype = dataObj.getAttribute('data-type');
    if(!elmid || !elmtype)
    {
        return true;
    }
    var submitdata = '';
    switch(elmtype)
    {
        case 'test':
          submitdata = '&testid=' + elmid;
        break;
        case 'user':
          submitdata = '&userid=' + elmid;
        break;
        case 'result':
          submitdata = '&result_id=' + elmid;
        break;
    }
    if(!submitdata)
    {
        return true;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = 'do=result&ajax=1' + submitdata + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    krtsts.show_window(html[0].childNodes[0].nodeValue);
                    return false;
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
                        krtsts.show_window(error_html, true);
                        setTimeout("krtsts.close_window()", 3000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(showresult_ajax))
        {
            YAHOO.util.Connect.abort(showresult_ajax);
        }
        showresult_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
}
krtsts_ctrl.prototype.request_cert = function(dataObj)
{
    this.close_window();
    var result_id = parseInt(dataObj.getAttribute('data-result_id')),
    targObg = YAHOO.util.Dom.get(dataObj.getAttribute('data-return-target'));
    if(!targObg || !result_id)
    {
        return true;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = 'do=reqcert&ajax=1&result_id=' + result_id + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata"),
                    success = parseInt(html[0].getAttribute('data-success'));
                    if(success)
                    {
                        targObg.parentNode.removeChild(targObg);
                    }
                    krtsts.show_window(html[0].childNodes[0].nodeValue, success ? false : true);
                    setTimeout("krtsts.close_window()", 9000);
                    return false;
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
                        krtsts.show_window(error_html, true);
                        setTimeout("krtsts.close_window()", 9000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(postcert_ajax))
        {
            YAHOO.util.Connect.abort(postcert_ajax);
        }
        postcert_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
}
krtsts_ctrl.prototype.finish_test = function(dataObj)
{
    this.close_window();
    var test_id = parseInt(dataObj.getAttribute('data-test_id')),
    targObg = YAHOO.util.Dom.get(dataObj.getAttribute('data-return-target'));
    if(!targObg || !test_id)
    {
        return false;
    }
    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = 'do=finishtest&ajax=1&test_id=' + test_id + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    targObg.innerHTML = html[0].childNodes[0].nodeValue;
                    return false;
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
                        krtsts.show_window(error_html, true);
                        setTimeout("krtsts.close_window()", 9000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(finishtest_ajax))
        {
            YAHOO.util.Connect.abort(finishtest_ajax);
        }
        finishtest_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
}
krtsts_ctrl.prototype.post_answer = function(e, targId)
{
    //return true;
    this.close_window();
    e = YAHOO.util.Event.getEvent(e);
    var targ = YAHOO.util.Event.getTarget(e),
    questionObj = YAHOO.util.Dom.get(targId);
    questionid = parseInt(targ.getAttribute('data-questionid'));
    e.preventDefault();
    if(!questionid)
    {
        return true;
    }
    var submitstring = this.get_submitstring(targ.form, false);
    if(!submitstring)
    {
        targ.form.submit();
    }
    
    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = submitstring + '&ajax=1&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata");
                    questionObj.innerHTML = html[0].childNodes[0].nodeValue;
                    return false;
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
                        krtsts.show_window(error_html, true);
                        setTimeout("krtsts.close_window()", 9000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(postanswer_ajax))
        {
            YAHOO.util.Connect.abort(postanswer_ajax);
        }
        postanswer_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
    return false;
}
krtsts_ctrl.prototype.saveedit_question = function(e, questionid)
{
    this.close_window();
    questionid = parseInt(questionid);
    if(!questionid)
    {
        return true;
    }
    e = YAHOO.util.Event.getEvent(e);
    var targ = YAHOO.util.Event.getTarget(e);
    e.preventDefault();
    var submitstring = this.get_submitstring(targ.form, false);
    if(!submitstring)
    {
        targ.form.submit();
    }
    
    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = submitstring + '&ajax=1&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata"),
                    hideButton = html[0].getAttribute('hidebutton');
                    krtsts.show_window(html[0].childNodes[0].nodeValue);
                    if(hideButton)
                    {
                        var btnObj = YAHOO.util.Dom.get('addanswer_button');
                        if(btnObj)
                        {
                            btnObj.parentNode.removeChild(btnObj);
                        }
                    }
                    setTimeout("krtsts.close_window()", 3000);
                    return false;
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
                        krtsts.show_window(error_html, true);
                        setTimeout("krtsts.close_window()", 9000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(saveedit_ajax))
        {
            YAHOO.util.Connect.abort(saveedit_ajax);
        }
        saveedit_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
    return false;
}
krtsts_ctrl.prototype.preview_answer = function(btnObj, id)
{
    var txtarea = YAHOO.util.Dom.get(id);
    txtarea.value = PHP.trim(txtarea.value);
    if(txtarea && txtarea.value == '')
    {
        this.show_window('<b>Empty!</b>', true);
        return false;
    }
    
    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = 'do=previewanswer&ajax=1'
        + '&answer=' + PHP.urlencode(txtarea.value)
        + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata"),
                    previewObj = YAHOO.util.Dom.get('aedit_preview_area_' + parseInt(btnObj.getAttribute('data-answerid')));
                    if(previewObj)
                    {
                        previewObj.innerHTML = html[0].childNodes[0].nodeValue;
                    }
                    else
                    {
                        krtsts.show_window(html[0].childNodes[0].nodeValue);
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
                        krtsts.show_window(error_html, true);
                        setTimeout("krtsts.close_window()", 9000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(preview_ajax))
        {
            YAHOO.util.Connect.abort(preview_ajax);
        }
        preview_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
}
krtsts_ctrl.prototype.addfield = function(obj)
{
    this.close_window();
    var questionid = obj.getAttribute('data-questionid'), multiple = 0;
    if(!questionid)
    {
        this.show_window('<b>Invalid questionid!</b>', true);
        return false;
    }
    this.count_fields();

    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = 'do=addfield&ajax=1'
        + '&tstsquestionid=' + questionid
        + '&maxanswerid=' + this.max_answerid
        + '&answers_count=' + this.answers_count
        + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata"),
                    max_answerid = parseInt(html[0].getAttribute('nextid')),
                    hideButton = html[0].getAttribute('hidebutton'),
                    wrapper = krtsts.field_wrapper(html[0].childNodes[0].nodeValue, max_answerid);
                    krtsts.answersPlaceHolder.appendChild(wrapper);
                    krtsts.count_fields();
                    if(hideButton)
                    {
                        var btnObj = YAHOO.util.Dom.get('addanswer_button');
                        if(btnObj)
                        {
                            btnObj.parentNode.removeChild(btnObj);
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
                        krtsts.show_window(error_html, true);
                        setTimeout("krtsts.close_window()", 9000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(addfield_ajax))
        {
            YAHOO.util.Connect.abort(addfield_ajax);
        }
        addfield_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
}
krtsts_ctrl.prototype.delete_answer = function(obj)
{
    this.close_window();
    var answerid = parseInt(obj.getAttribute('data-answerid'), 10),
    questionid = parseInt(obj.getAttribute('data-questionid'), 10);
    if(!questionid)
    {
        this.show_window('<b>Invalid Question ID!</b>', true);
        return false;
    }

    if(AJAX_Compatible)
    {
        var sendUrl = krtsts['bburl'] + '/krtests.php',
        postData = 'do=deleteanswer&ajax=1'
        + '&tstsquestionid=' + questionid
        + '&answerid=' + answerid
        + '&answers_count=' + this.answers_count
        + '&securitytoken=' + SECURITYTOKEN,
        handleSuccess = function(ajax)
        {
            if(ajax.responseXML !== undefined)
            {
                if(fetch_tag_count(ajax.responseXML, 'html'))
                {
                    var html = ajax.responseXML.documentElement.getElementsByTagName("htmldata"),
                    showButton = parseInt(html[0].getAttribute('showbutton'), 10),
                    answerObj = YAHOO.util.Dom.get('aedit_' + answerid),
                    questionAnswers = YAHOO.util.Dom.get('question_answers'),
                    btnObj = YAHOO.util.Dom.get('addanswer_button');
                    if(answerObj)
                    {
                        answerObj.parentNode.removeChild(answerObj);
                    }
                    if(showButton && !btnObj && questionAnswers)
                    {
                        btnObj = document.createElement('div');
                        btnObj.id = 'addanswer_button';
                        btnObj.innerHTML = html[0].childNodes[0].nodeValue;
                        btnObj.onclick = function()
                        {
                            krtsts.addfield(this);
                        }
                        btnObj.setAttribute('data-questionid', questionid);
                        krtsts.insertAfter(btnObj, questionAnswers);
                        YAHOO.util.Dom.addClass(btnObj, 'smallfont tsts-txtbtn');
                    }
                    krtsts.count_fields();
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
                        krtsts.show_window(error_html, true);
                        setTimeout("krtsts.close_window()", 9000);
                        return false;
                    }
                }
            }
        },
        handleFailure = function(ajax)
        {
            console.warn("AJAX Error: Status = %s: %s", ajax.status, ajax.statusText);
            krtsts.show_window('AJAX Error!', true);
            setTimeout("krtsts.close_window()", 3000);
            return false;
        },
        callback =
        {
            success: handleSuccess,
            failure: handleFailure,
            timeout: vB_Default_Timeout
        };
        if(YAHOO.util.Connect.isCallInProgress(deleteanswer_ajax))
        {
            YAHOO.util.Connect.abort(deleteanswer_ajax);
        }
        deleteanswer_ajax = YAHOO.util.Connect.asyncRequest('POST', sendUrl, callback, postData);
        return false;
    }
}
krtsts_ctrl.prototype.insertAfter = function(newNode, referenceNode)
{
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}
krtsts_ctrl.prototype.get_fields = function()
{
    return YAHOO.util.Dom.getElementsByClassName("tsts-fieldblock-bit", "div", this.answersPlaceHolder);
}
krtsts_ctrl.prototype.close_window = function()
{
    krtsts_grayOut(false);
    if(YAHOO.util.Dom.get('krtsts_window_container'))
    {
        YAHOO.util.Dom.get('krtsts_window_container').parentNode.removeChild(YAHOO.util.Dom.get('krtsts_window_container'));
    }
}
krtsts_ctrl.prototype.show_window = function(dataContent, showerror)
{
    var win = YAHOO.util.Dom.get('krtsts_window_container');
    if(win)
    {
        this.close_window();
    }
    var div = document.createElement('div');
    div.id = 'krtsts_window_container';
    div.style.maxWidth = "650px";
    div.style.minWidth = "400px";
    div.style.padding = "5px";
    div.className = 'tborder alt1';
    if(showerror)
    {
        div.style.border = '1px solid red';
    }
    div.style.position = (is_ie && !is_ie7) ? "absolute" : "fixed";
    div.style.zIndex = "100";
    div.innerHTML = dataContent;

    var closew_image = new Image();
    closew_image.src = IMGDIR_MISC + "/cross.png";
    closew_image.style.padding = '0 0 0 5px';
    closew_image.style.position = 'absolute';
    closew_image.style.top = '3px';
    closew_image.style.right = '3px';
    closew_image.className = 'inlineimg';
    closew_image.alt = '';
    closew_image.border = '0';
    closew_image.onmousedown = function()
    {
        krtsts.close_window();
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
    krtsts_grayOut(true);
    return false;
}
krtsts_ctrl.prototype.startTimer = function(config)
{
    var start = Date.now(), diff, minutes, seconds,
    objId = config.objId,
    parentId = config.parentId,
    timeLeft = config.timeLeft,
    phrases = config.phrases,
    cntObj = YAHOO.util.Dom.get(objId),
    prntObj = YAHOO.util.Dom.get(parentId);

    function timer()
    {
        diff = timeLeft - (((Date.now() - start) / 1000) | 0);
        var tdiff = diff;
        var seconds = Math.floor(tdiff % 60);
        var tdiff = tdiff / 60;
        var minutes = Math.floor(tdiff % 60);
        var tdiff = tdiff / 60;
        var hours = Math.floor(tdiff % 24);
        
        hours = hours < 10 ? "0" + hours : hours;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        if(cntObj)
        {
            cntObj.innerHTML = hours + ":" + minutes + ":" + seconds; 
        }
        if(diff <= 0)
        {
            stop();
        }
    };
    function stop()
    {
        if(prntObj)
        {
            prntObj.innerHTML = phrases.failed;
            setTimeout(function()
            {
                btnObj = YAHOO.util.Dom.get('answer_button');
                if(btnObj)
                {
                    krtsts.finish_test(btnObj);
                }
            }, 6000);
        }
        clearInterval(timer);
    }
    timer();
    setInterval(timer, 1000);
}
