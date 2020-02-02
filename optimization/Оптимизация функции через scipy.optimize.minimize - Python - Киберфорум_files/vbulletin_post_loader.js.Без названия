/*!======================================================================*\
|| #################################################################### ||
|| # vBulletin 3.8.7
|| # ---------------------------------------------------------------- # ||
|| # Copyright ©2000-2011 vBulletin Solutions, Inc. All Rights Reserved. ||
|| # This file may not be redistributed in whole or significant part. # ||
|| # ---------------- VBULLETIN IS NOT FREE SOFTWARE ---------------- # ||
|| # http://www.vbulletin.com | http://www.vbulletin.com/license.html # ||
|| #################################################################### ||
\*======================================================================*/

/**
* Attempts to display a post via AJAX, falling back to opening a new window if AJAX not available
*
* @param	integer	Post ID
*
* @return	boolean	False
*/
function display_post(postid)
{
	if (AJAX_Compatible)
	{
		vB_PostLoader[postid] = new vB_AJAX_PostLoader(postid);
		vB_PostLoader[postid].init();
	}
	else
	{
		pc_obj = fetch_object('postcount' + this.postid);
		openWindow('showpost.php?' + (SESSIONURL ? 's=' + SESSIONURL : '') + (pc_obj != null ? '&postcount=' + PHP.urlencode(pc_obj.name) : '') + '&p=' + postid);
	}
	return false;
};

// #############################################################################
// vB_AJAX_PostLoader
// #############################################################################

var vB_PostLoader = new Array();

/**
* Class to load a postbit via AJAX
*
* @package	vBulletin
* @version	$Revision: 39862 $
* @date		$Date: 2010-10-18 18:16:44 -0700 (Mon, 18 Oct 2010) $
* @author	Kier Darby, vBulletin Development Team
*
* @param	integer	Post ID
*/
function vB_AJAX_PostLoader(postid)
{
	this.postid = postid;
	this.container = fetch_object('edit' + this.postid);
};

/**
* Initiates the AJAX send to showpost.php
*/
vB_AJAX_PostLoader.prototype.init = function()
{
	if (this.container)
	{
		postid = this.postid;
		pc_obj = fetch_object('postcount' + this.postid);

		YAHOO.util.Connect.asyncRequest("POST", "showpost.php?p=" + this.postid, {
			success: this.display,
			failure: this.handle_ajax_error,
			timeout: vB_Default_Timeout,
			scope: this
		}, SESSIONURL + "securitytoken=" + SECURITYTOKEN + "&ajax=1&postid=" + this.postid + (pc_obj != null ? "&postcount=" + PHP.urlencode(pc_obj.name) : ""));
	}
};

/**
* Handles AJAX Errors
*
* @param	object	YUI AJAX
*/
vB_AJAX_PostLoader.prototype.handle_ajax_error = function(ajax)
{
	//TODO: Something bad happened, try again
	vBulletin_AJAX_Error_Handler(ajax);
};

/**
* Takes the AJAX HTML output and replaces the existing post placeholder with the new HTML
*
* @param	object	YUI AJAX
*/
vB_AJAX_PostLoader.prototype.display = function(ajax)
{
	if (ajax.responseXML)
	{
		var postbit = ajax.responseXML.getElementsByTagName("postbit");

		if (postbit.length)
		{
			this.container.innerHTML = postbit[0].firstChild.nodeValue;
			PostBit_Init(fetch_object('post' + this.postid), this.postid);
		}
		else
		{	// parsing of XML failed, probably IE
			openWindow('showpost.php?' + (SESSIONURL ? 's=' + SESSIONURL : '') + (pc_obj != null ? '&postcount=' + PHP.urlencode(pc_obj.name) : '') + '&p=' + this.postid);
		}
	}
};

/*======================================================================*\
|| ####################################################################
|| # NulleD By - FintMax
|| # CVS: $RCSfile$ - $Revision: 39862 $
|| ####################################################################
\*======================================================================*/
