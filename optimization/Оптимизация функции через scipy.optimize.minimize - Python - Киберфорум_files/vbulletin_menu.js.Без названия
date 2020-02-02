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

vBulletin.add_event("vBmenuShow");
vBulletin.add_event("vBmenuHide");

/**
* vBulletin popup menu example usage:
*
* To create a new popup menu:
* 	<element id="x">Click me <script type="text/javascript"> vbmenu_register('x'); </script></element>
* The menu class expects an element with the id of x_menu that contains the menu.
*	<div id="x_menu" class="vbmenu_popup"> ... </div>
*/

// #############################################################################
// vB_Popup_Handler
// #############################################################################

/**
* vBulletin popup menu registry
*
* @package	vBulletin
* @version	$Revision: 39862 $
* @date		$Date: 2010-10-18 18:16:44 -0700 (Mon, 18 Oct 2010) $
* @author	Kier Darby, vBulletin Development Team
*/
function vB_Popup_Handler()
{
	/**
	* Options:
	*
	* @var	integer	Number of steps to use in sliding menus open
	* @var	boolean	Use opacity face in menu open?
	*/
	this.open_steps = 10;
	this.open_fade = false;

	this.active = false;

	this.menus = new Array();
	this.activemenu = null;
};

// =============================================================================
// vB_Popup_Handler methods

/**
* Activate / Deactivate the menu system
*
* @param	boolean	Active state for menus
*/
vB_Popup_Handler.prototype.activate = function(active)
{
	this.active = active;
	console.log("vBmenu :: System Activated");
};

/**
* Register a control object as a menu control
*
* @param	string	ID of the control object
* @param	boolean	Disable menu pop image addition
* @param	boolean	Disable menu slide open
*
* @return	vB_Popup_Menu
*/
vB_Popup_Handler.prototype.register = function(controlkey, noimage, noslide)
{
	//console.log("vBmenu :: registering '%s'", controlkey);
	this.menus[controlkey] = new vB_Popup_Menu(controlkey, noimage, noslide);

	// deal with usercss
	var usercss = YAHOO.util.Dom.get("usercss");
	if (usercss && YAHOO.util.Dom.isAncestor(usercss, controlkey))
	{
		this.menus[controlkey].imgsrc = IMGDIR_MISC + "/menu_open_usercss.gif";
	}

	this.menus[controlkey].startup();

	return this.menus[controlkey];
};

/**
* Hide active menu
*/
vB_Popup_Handler.prototype.hide = function()
{
	if (this.activemenu != null)
	{
		this.menus[this.activemenu].hide();
	}
};


// #############################################################################
// initialize menu registry

var vBmenu = new vB_Popup_Handler();

/**
* Function to allow anything to hide all menus
*
* @param	event	Event object
*
* @return	mixed
*/
function vbmenu_hide(e)
{
	if (e && e.button && e.button != 1 && e.type == 'click')
	{
		return true;
	}
	else
	{
		vBmenu.hide();
	}
};

// #############################################################################
// vB_Popup_Menu
// #############################################################################

/**
* vBulletin popup menu class constructor
*
* Manages a single menu and control object
* Initializes control object
*
* @package	vBulletin
* @version	$Revision: 39862 $
* @date		$Date: 2010-10-18 18:16:44 -0700 (Mon, 18 Oct 2010) $
* @author	Kier Darby, vBulletin Development Team
*
* @param	string	ID of the control object
* @param	boolean	Disable menu pop image addition
* @param	boolean	Disable menu slide open
*/
function vB_Popup_Menu(controlkey, noimage, noslide)
{
	this.controlkey = controlkey;
	this.noimage = noimage;
	this.noslide = noslide;

	this.menuname = this.controlkey.split('.')[0] + '_menu';
	this.imgsrc = IMGDIR_MISC + '/menu_open.gif';
};

// =============================================================================
// vB_Popup_Menu methods

/**
* Startup routine for a popup menu
*/
vB_Popup_Menu.prototype.startup = function()
{
	this.init_control(this.noimage);

	if (fetch_object(this.menuname))
	{
		this.init_menu();
	}

	this.slide_open = (this.noslide ? false : true);
	this.open_steps = vBmenu.open_steps;

	vBulletin.add_event("vBmenuShow_" + this.controlkey);
	vBulletin.add_event("vBmenuHide_" + this.controlkey);
}

/**
* Initialize the control object
*/
vB_Popup_Menu.prototype.init_control = function(noimage)
{
	this.controlobj = fetch_object(this.controlkey);
	this.controlobj.state = false;

	if (this.controlobj.firstChild && (this.controlobj.firstChild.tagName == 'TEXTAREA' || this.controlobj.firstChild.tagName == 'INPUT'))
	{
		// do nothing
	}
	else
	{
		if (!noimage && !(is_mac && is_ie))
		{
			var space = document.createTextNode(' ');
			this.controlobj.appendChild(space);

			var img = document.createElement('img');
			img.src = this.imgsrc;
			img.border = 0;
			img.title = '';
			img.alt = '';
			this.img = this.controlobj.appendChild(img);
		}

		this.controlobj.unselectable = true;
		if (!noimage)
		{
			this.controlobj.style.cursor = pointer_cursor;
		}
		this.controlobj.onclick = vB_Popup_Events.prototype.controlobj_onclick;
		this.controlobj.onmouseover = vB_Popup_Events.prototype.controlobj_onmouseover;
	}
};

/**
* Init the popup menu object
*/
vB_Popup_Menu.prototype.init_menu = function()
{
	this.menuobj = fetch_object(this.menuname);
	this.select_handler = new vB_Select_Overlay_Handler(this.menuobj);

	if (this.menuobj && !this.menuobj.initialized)
	{
		this.menuobj.initialized = true;
		this.menuobj.onclick = e_by_gum;
		this.menuobj.style.position = 'absolute';
		this.menuobj.style.zIndex = 50;

		// workaround border disappearing issues in IE
		if (is_ie && !is_mac)
		{
			if (YAHOO.env.ua.ie < 7)
			{
				// this seems to fix it in < IE7, but IE7 disables ClearType with filters...
				this.menuobj.style.filter += "alpha(enabled=1,opacity=100)";
			}
			else
			{
				// ...so use this trick for IE7. It seems to work, but I don't know why. :)
				this.menuobj.style.minHeight = '1%';
			}
		}

		this.init_menu_contents();
	}
};

/**
* Init the popup menu contents
*/
vB_Popup_Menu.prototype.init_menu_contents = function()
{
	var tags = new Array("td", "li");
	for (var j = 0; j < tags.length; j++)
	{
		var blocks = fetch_tags(this.menuobj, tags[j]);
		for (var i = 0; i < blocks.length; i++)
		{
			if (blocks[i].className == 'vbmenu_option')
			{
				if (blocks[i].title && blocks[i].title == 'nohilite')
				{
					// not an active cell
					blocks[i].title = '';
				}
				else
				{
					// create a reference back to the menu class
					blocks[i].controlkey = this.controlkey;

					// handle mouseover / mouseout highlighting events
					blocks[i].onmouseover = vB_Popup_Events.prototype.menuoption_onmouseover;
					blocks[i].onmouseout = vB_Popup_Events.prototype.menuoption_onmouseout;

					var links = fetch_tags(blocks[i], 'a');
					if (links.length == 1)
					{
						/* Ok we have a link, we should use this if
						1. There is no onclick event in the link
						2. There is no onclick event on the cell
						3. The onclick event for the cell should equal the link if the above are true

						If we find a browser thats gets confused we may need to set remove_link to true for it.
						*/

						blocks[i].className = blocks[i].className + ' vbmenu_option_alink';
						blocks[i].islink = true;

						var linkobj = links[0];
						var remove_link = false;

						blocks[i].target = linkobj.getAttribute('target');

						if (typeof linkobj.onclick == 'function')
						{
							blocks[i].ofunc = linkobj.onclick;
							blocks[i].onclick = vB_Popup_Events.prototype.menuoption_onclick_function;
							remove_link = true;
						}
						else if (typeof blocks[i].onclick == 'function')
						{
							blocks[i].ofunc = blocks[i].onclick;
							blocks[i].onclick = vB_Popup_Events.prototype.menuoption_onclick_function;
							remove_link = true;
						}
						else
						{
							blocks[i].href = linkobj.href;
							blocks[i].onclick = vB_Popup_Events.prototype.menuoption_onclick_link;
						}

						if (remove_link)
						{
							var newlink = document.createElement('a');
							newlink.innerHTML = linkobj.innerHTML;
							newlink.href = '#';
							newlink.onclick = function(e) { e = e ? e : window.event; e.returnValue = false; return false; };
							blocks[i].insertBefore(newlink, linkobj);
							blocks[i].removeChild(linkobj);
						}
					}
					else if (typeof blocks[i].onclick == 'function')
					{
						blocks[i].ofunc = blocks[i].onclick;
						blocks[i].onclick = vB_Popup_Events.prototype.menuoption_onclick_function;
					}
				}
			}

			// Get rid of the internal reference title if it is still lurking around 
			if (blocks[i].title == "nohilite")
			{
				blocks[i].title = '';
			}
		}
	}
};

/**
* Show the menu
*
* @param	object	The control object calling the menu
* @param	boolean	Use slide (false) or open instantly? (true)
*/
vB_Popup_Menu.prototype.show = function(obj, instant)
{
	if (!vBmenu.active)
	{
		return false;
	}
	else if (!this.menuobj)
	{
		this.init_menu();
	}

	if (!this.menuobj || vBmenu.activemenu == this.controlkey)
	{
		return false;
	}

	console.log("vBmenu :: Show '%s'", this.controlkey);

	if (vBmenu.activemenu != null && vBmenu.activemenu != this.controlkey)
	{
		vBmenu.menus[vBmenu.activemenu].hide();
	}

	vBmenu.activemenu = this.controlkey;

	this.menuobj.style.display = '';
	if (this.slide_open)
	{
		this.menuobj.style.clip = 'rect(auto, 0px, 0px, auto)';
	}

	this.set_menu_position(obj);

	if (!instant && this.slide_open)
	{
		this.intervalX = Math.ceil(this.menuobj.offsetWidth / this.open_steps);
		this.intervalY = Math.ceil(this.menuobj.offsetHeight / this.open_steps);
		this.slide((this.direction == 'left' ? 0 : this.menuobj.offsetWidth), 0, 0);
	}
	else if (this.menuobj.style.clip && this.slide_open)
	{
		this.menuobj.style.clip = 'rect(auto, auto, auto, auto)';
	}

	// deal with IE putting <select> elements on top of everything
	this.select_handler.hide();

	if (this.controlobj.editorid)
	{
		this.controlobj.state = true;
		//this.controlobj.editor.menu_context(this.controlobj, 'mousedown');
		vB_Editor[this.controlobj.editorid].menu_context(this.controlobj, 'mousedown');
	}

	vBulletin.events["vBmenuShow_" + this.controlkey].fire(this.controlkey);
	vBulletin.events.vBmenuShow.fire(this.controlkey);
};

/**
* Position the menu relative to a reference element
*
* @param	object	Reference HTML element
*/
vB_Popup_Menu.prototype.set_menu_position = function(obj)
{
	this.pos = this.fetch_offset(obj);
	this.leftpx = this.pos['left'];
	this.toppx = this.pos['top'] + obj.offsetHeight;

	if ((this.leftpx + this.menuobj.offsetWidth) >= document.body.clientWidth && (this.leftpx + obj.offsetWidth - this.menuobj.offsetWidth) > 0)
	{
		this.leftpx = this.leftpx + obj.offsetWidth - this.menuobj.offsetWidth;
		this.direction = 'right';
	}
	else
	{
		this.direction = 'left'
	}

	// move the pagenav menu to the calling object, so it appears to be styled like where it's displayed
	if (this.controlkey.match(/^pagenav\.\d+$/))
	{
		obj.appendChild(this.menuobj);
	}

	this.menuobj.style.left = this.leftpx + 'px';
	this.menuobj.style.top  = this.toppx + 'px';
};

/**
* Hide the menu
*/
vB_Popup_Menu.prototype.hide = function(e)
{
	if (e && e.button && e.button != 1)
	{
		// get around some context menu issues etc.
		return true;
	}

	console.log("vBmenu :: Hide '%s'", this.controlkey);

	this.stop_slide();

	this.menuobj.style.display = 'none';

	this.select_handler.show();

	if (this.controlobj.editorid)
	{
		this.controlobj.state = false;
		vB_Editor[this.controlobj.editorid].menu_context(this.controlobj, 'mouseout');
	}

	vBmenu.activemenu = null;

	vBulletin.events["vBmenuHide_" + this.controlkey].fire(this.controlkey);
	vBulletin.events.vBmenuHide.fire(this.controlkey);
};

/**
* Hover behaviour for control object
*/
vB_Popup_Menu.prototype.hover = function(obj)
{
	if (vBmenu.activemenu != null)
	{
		if (vBmenu.menus[vBmenu.activemenu].controlkey != this.id)
		{
			this.show(obj, true);
		}
	}
};

/**
* Slides menu open
*
* @param	integer	Clip X
* @param	integer	Clip Y
* @param	integer	Opacity (0-100)
*/
vB_Popup_Menu.prototype.slide = function(clipX, clipY, opacity)
{
	if (this.direction == 'left' && (clipX < this.menuobj.offsetWidth || clipY < this.menuobj.offsetHeight))
	{
		clipX += this.intervalX;
		clipY += this.intervalY;

		this.menuobj.style.clip = "rect(auto, " + clipX + "px, " + clipY + "px, auto)";
		this.slidetimer = setTimeout("vBmenu.menus[vBmenu.activemenu].slide(" + clipX + ", " + clipY + ", " + opacity + ");", 0);
	}
	else if (this.direction == 'right' && (clipX > 0 || clipY < this.menuobj.offsetHeight))
	{
		clipX -= this.intervalX;
		clipY += this.intervalY;

		this.menuobj.style.clip = "rect(auto, " + this.menuobj.offsetWidth + "px, " + clipY + "px, " + clipX + "px)";
		this.slidetimer = setTimeout("vBmenu.menus[vBmenu.activemenu].slide(" + clipX + ", " + clipY + ", " + opacity + ");", 0);
	}
	else
	{
		this.stop_slide();
	}
};

/**
* Abort menu slider
*/
vB_Popup_Menu.prototype.stop_slide = function()
{
	clearTimeout(this.slidetimer);

	this.menuobj.style.clip = 'rect(auto, auto, auto, auto)';
};

/**
* Fetch offset of an object
*
* @param	object	The object to be measured
*
* @return	array	The measured offsets left/top
*/
vB_Popup_Menu.prototype.fetch_offset = function(obj)
{
	if (obj.getBoundingClientRect)
	{
		// better, more accurate function for IE
		var rect = obj.getBoundingClientRect();

		var scrollTop = Math.max(document.documentElement.scrollTop, document.body.scrollTop);
		var scrollLeft = Math.max(document.documentElement.scrollLeft, document.body.scrollLeft);

		if (document.documentElement.dir == 'rtl')
		{
			// IE returns a positive scrollLeft, but we need a negative value to actually do proper calculations.
			// This actually flips the scolloing to be relative to the distance scrolled from the default.
			scrollLeft = scrollLeft + document.documentElement.clientWidth - document.documentElement.scrollWidth;
		}

		return { 'left' : rect.left + scrollLeft, 'top' : rect.top + scrollTop };
	}

	var left_offset = obj.offsetLeft;
	var top_offset = obj.offsetTop;

	while ((obj = obj.offsetParent) != null)
	{
		left_offset += obj.offsetLeft;
		top_offset += obj.offsetTop;
	}

	return { 'left' : left_offset, 'top' : top_offset };
};

// #############################################################################
// Menu event handler functions

/**
* Class containing menu popup event handlers
*/
function vB_Popup_Events()
{
};

/**
* Handles control object click events
*/
vB_Popup_Events.prototype.controlobj_onclick = function(e)
{
	if (typeof do_an_e == 'function')
	{
		do_an_e(e);
		if (vBmenu.activemenu == null || vBmenu.menus[vBmenu.activemenu].controlkey != this.id)
		{
			vBmenu.menus[this.id].show(this);
		}
		else
		{
			vBmenu.menus[this.id].hide();
		}
	}
};

/**
* Handles control object mouseover events
*/
vB_Popup_Events.prototype.controlobj_onmouseover = function(e)
{
	if (typeof do_an_e == 'function')
	{
		do_an_e(e);
		vBmenu.menus[this.id].hover(this);
	}
};

/**
* Handles menu option click events for options with onclick events
*/
vB_Popup_Events.prototype.menuoption_onclick_function = function(e)
{
	this.ofunc(e);
	vBmenu.menus[this.controlkey].hide();
};

/**
* Handles menu option click events for options containing links
*/
vB_Popup_Events.prototype.menuoption_onclick_link = function(e)
{
	e = e ? e : window.event;

	// Safari has "issues" with resetting what was clicked on, super minor and I dont care
	e.cancelBubble = true;
	if (e.stopPropagation) e.stopPropagation();
	if (e.preventDefault) e.preventDefault();

	if (e.shiftKey || (this.target != null && this.target != '' && this.target.toLowerCase() != '_self'))
	{
		if (this.target != null && this.target.charAt(0) != '_')
		{
			window.open(this.href, this.target);
		}
		else
		{
			window.open(this.href);
		}
	}
	else
	{
		window.location = this.href;
	}

	vBmenu.menus[this.controlkey].hide();
	return false;
};

/**
* Handles menu option mouseover events
*/
vB_Popup_Events.prototype.menuoption_onmouseover = function(e)
{
	this.className = 'vbmenu_hilite' + (this.islink ? ' vbmenu_hilite_alink' : '');
	this.style.cursor = pointer_cursor;
};

/**
* Handles menu option mouseout events
*/
vB_Popup_Events.prototype.menuoption_onmouseout = function(e)
{
	this.className = 'vbmenu_option' + (this.islink ? ' vbmenu_option_alink' : '');
	this.style.cursor = 'default';
};

/*======================================================================*\
|| ####################################################################
|| # NulleD By - FintMax
|| # CVS: $RCSfile$ - $Revision: 39862 $
|| ####################################################################
\*======================================================================*/
