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

// #############################################################################
// vB_Lightbox_Container
// call using:
// vBulletin.register_control("vB_Lightbox_Container", lightbox_container_id, lightbox_trigger_events)
// #############################################################################

vBulletin.events.systemInit.subscribe(function()
{
	if (vBulletin.elements["vB_Lightbox_Container"])
	{
		for (var i = 0; i < vBulletin.elements["vB_Lightbox_Container"].length; i++)
		{
			var element = vBulletin.elements["vB_Lightbox_Container"][i];
			init_postbit_lightbox(element[0], element[1]);
		}
		vBulletin.elements["vB_Lightbox_Container"] = null;
	}
});

/**
* Global variables for lightbox
*
* @var	array	Collection of all vB_Lightbox objects
* @var	object	Window overlay element - created in init_postbit_lightbox()
* @var	object	Window overlay intersecting <select> handler (vB_Select_Overlay_Handler)
* @var	integer	Default for the lightbox event initialisation
*/
var Lightboxes = new Array();
var Lightbox_overlay = null;
var Lightbox_overlay_select_handler = null;
var Lightbox_event_default = null;
var Lightbox_current = null;
var Lightbox_map = {};

// =============================================================================

/**
* Activates an attachment thumbnail to have lightbox functionality
*
* @package	vBulletin
* @version	$Revision: 24798 $
* @date		$Date: 2007-11-22 13:59:49 +0000 (Thu, 22 Nov 2007) $
* @author	Kier Darby
* @copyright	vBulletin Solutions, Inc.
*
* @param	object	Attachmnent Link
* @param	integer	Unique ID for the page
* @param	integer	Bitfield indicating what events to add
*/
function vB_Lightbox(element, uniqueid, containerid, events)
{
	/**
	* Main class variables
	*
	* @var	integer	Minimum border in pixels between the lightbox and the viewport edges
	* @var	integer	Minimum size in pixels for the image in the lightbox to shrink
	* @var	integer	Bitmask for click event
	* @var	integer	Bitmask for hover event
	* @var	boolean	True if a click triggered the lightbox to show
	* @var	object	Link that would normally open the image, to which events are attached
	* @var	object	Timeout handler for hover countdown
	* @var	object	Javascript Image object for preloading lightbox image
	* @var	integer	Status counter - increases value as status is closer to lightbox ready for display
	* @var	boolean	True if the lightbox is complete and visible
	*
	* @var	string	Link to full-size attachment
	* @var	string	File upload date
	* @var	string	File upload time
	* @var	string	File name
	* @var	string	Lightbox HTML from template 'lightbox'
	* @var  string  URL of the progress image
	*
	* @var	object	Container for lightbox
	* @var	object	Lightbox object
	* @var	object	Close lightbox button
	* @var	object	Image within lightbox
	* @var	object	YUI AJAX transaction
	*/
	this.minborder = 100;
	this.mindimension = 50;
	this.event_click = 0x1;
	this.event_hover = 0x2;
	this.click_triggered = false;
	this.events_enabled = false;
	this.element = element;
	this.timeout = null;
	this.imageloader = null;
	this.status = 0;
	this.active = false;
	this.ajax_req = null;
	this.cursor = null;

	this.link = null;
	this.date = null;
	this.time = null;
	this.name = null;
	this.html = null;
	this.loader_link = null;
	this.loader_height = null;
	this.loader_width = null;

	this.lightbox = null;
	this.closebtn = null;
	this.img = null;

	this.uniqueid = uniqueid;
	this.containerid = containerid;

	// hover events
	if (events & this.event_hover)
	{
		YAHOO.util.Event.on(this.element, "mouseover", this.countdown, this, true);
		YAHOO.util.Event.on(this.element, "mouseout", this.halt, this, true);
	}

	// click event
	if (events & this.event_click)
	{
		YAHOO.util.Event.on(this.element, "click", this.image_click, this, true);
	}
}

/**
* Sets the internal status of the object
*
* @param	integer	Status
*/
vB_Lightbox.prototype.set_status = function(status, caller)
{
	console.log("vB_Lightbox :: Set status = %d (%s)", status, caller);
	this.status = status;
}

/**
* Checks the internal status of the object
*
* @param	integer	Status (checks for >= status)
*
* @return	boolean
*/
vB_Lightbox.prototype.check_status = function(status)
{
	if (this.status >= status)
	{
		return true;
	}
	else
	{
		console.warn("Checked status for %d, found %d", status, this.status);
		return false;
	}
}

/**
* Starts a count-down to image loading
*/
vB_Lightbox.prototype.countdown = function(e)
{
	if (!this.active)
	{
		this.set_status(1, "countdown");
		this.cursor = YAHOO.util.Dom.getStyle(this.element, 'cursor');
		this.element.style.cursor = "wait";
		this.click_triggered = false;
		this.timeout = setTimeout("Lightboxes['" + this.uniqueid + "'].load_lightbox();", 1500);
	}
}

/**
* Aborts any count-downs that have been started
*/
vB_Lightbox.prototype.halt = function(e)
{
	if (this.status < 2)
	{
		this.set_status(0, "halt");
	}
	clearTimeout(this.timeout);
	this.element.style.cursor = this.cursor;
}

/**
* Click trigger to start the lightbox process
*/
vB_Lightbox.prototype.image_click = function(e)
{
	if (e.ctrlKey || e.shiftKey)
	{
		// ctrl or shift clicked -> let browser handle
		return true;
	}

	this.click_triggered = true;
	this.load_lightbox(e);
}

/**
* Loads the lightbox AJAX request to get info about the attachment
*/
vB_Lightbox.prototype.load_lightbox = function(e)
{
	if (this.check_status(0) && !YAHOO.util.Connect.isCallInProgress(this.ajax_req))
	{
		this.set_status(2, "load_lightbox 1");

		if (Lightbox_current && Lightbox_current.loader_link)
		{
			Lightbox_current.img.src = Lightbox_current.loader_link;
			Lightbox_current.img.width = Lightbox_current.loader_width;
			Lightbox_current.img.height = Lightbox_current.loader_height;
			center_element(Lightbox_current.lightbox);

			/*
			var width = Lightbox_current.img.width;
			var height = Lightbox_current.img.height;

			var holder = fetch_object('lightboxholder');
			YAHOO.util.Dom.setStyle(holder, "height", height + "px");
			YAHOO.util.Dom.setStyle(holder, "width", width + "px");
			YAHOO.util.Dom.setStyle(holder, "display", "table-cell");
			*/
		}

		if (e)
		{
			YAHOO.util.Event.stopEvent(e);
		}

		if (this.timeout)
		{
			clearTimeout(this.timeout);
			this.element.style.cursor = this.cursor;
		}

		if (this.html == null)
		{
			var imagelink = this.element.getAttribute("href");
			var requestlink = imagelink.substr(imagelink.indexOf("?") + 1) + "&securitytoken=" + SECURITYTOKEN + "&ajax=1&uniqueid=" + this.uniqueid;

			/*
			if (Lightbox_current)
			{
				requestlink = requestlink + "&width=" + width + "&height=" + height;
			}
			*/

			if (Lightbox_map[this.containerid][this.uniqueid + 1] == null)
			{
				requestlink = requestlink + "&last=1";
			}

			if (Lightbox_map[this.containerid][this.uniqueid - 1] == null)
			{
				requestlink = requestlink + "&first=1";
			}

			requestlink = requestlink + "&total=" + Lightbox_map[this.containerid].size();
			requestlink = requestlink + "&current=" + (Lightbox_map[this.containerid].find(this.uniqueid) + 1);

			this.show_overlay();

			try
			{
				this.ajax_req = YAHOO.util.Connect.asyncRequest("POST", imagelink, {
					success: this.handle_ajax_response,
					failure: this.handle_ajax_error,
					scope: this,
					timeout: vB_Default_Timeout
				}, requestlink);
			}
			catch(e)
			{
				var path = imagelink.substr(0, imagelink.indexOf("?"));
				var attach_filename;

				if (attach_filename = path.match(/\/([^/]*attachment\.php)$/))
				{
					this.ajax_req = YAHOO.util.Connect.asyncRequest("POST", attach_filename[1], {
						success: this.handle_ajax_response,
						failure: this.handle_ajax_error,
						scope: this,
						timeout: vB_Default_Timeout
					}, requestlink);
				}
				else if (this.click_triggered)
				{
					window.location = imagelink;
				}
			}
		}
		else
		{
			this.set_status(3, "load_lightbox 2");
			this.show_lightbox();
		}
	}
}

/**
* Handle AJAX Error
*
* @param	object	YUI AJAX
*/
vB_Lightbox.prototype.handle_ajax_error = function(ajax)
{
	vBulletin_AJAX_Error_Handler(ajax);

	if (this.click_triggered)
	{
		window.location = this.element.getAttribute("href");
	}
}

/**
* Handles the AJAX request with info about the attachment and builds the lightbox HTML
*
* @param	object	YUI AJAX
*/
vB_Lightbox.prototype.handle_ajax_response  = function(ajax)
{
	if (!this.check_status(2))
	{
		return;
	}

	if (ajax.responseXML)
	{
		var errors = ajax.responseXML.getElementsByTagName("error");
		if (errors.length)
		{
			this.set_status(0, "handle_ajax_response - error");

			if (errors[0].firstChild.nodeValue == "notimage")
			{
				console.warn("Attempted to load non-image (.%s) into lightbox. Aborted.", ajax.responseXML.getElementsByTagName("extension")[0].firstChild.nodeValue);
			}
			else
			{
				// TODO: not the prettiest error handler
				alert(errors[0].firstChild.nodeValue.replace(/<(\/|[a-z]+)[^>]+>/g, ""));
			}

			return false;
		}

		var link = ajax.responseXML.getElementsByTagName("link");
		if (link.length)
		{
			this.set_status(3, "handle_ajax_response - success");

			this.show_overlay();

			this.link = link[0].firstChild.nodeValue;

			this.imageloader = new Image();
			YAHOO.util.Event.on(this.imageloader, "load", this.show_lightbox, this, true);

			var xmlvars = new Array("date", "time", "name", "html");
			for (var i = 0; i < xmlvars.length; i++)
			{
				this[xmlvars[i]] = ajax.responseXML.getElementsByTagName(xmlvars[i])[0].firstChild.nodeValue;
			}

			this.lightbox = document.body.appendChild(string_to_node(this.html));

			this.closebtn = YAHOO.util.Dom.get("lightboxbutton" + this.uniqueid);
			YAHOO.util.Event.on(this.closebtn, "click",  this.hide_lightbox, this, true);
			YAHOO.util.Event.on(this.closebtn, "mouseover", this.highlight_btn, this.closebtn, true);
			YAHOO.util.Event.on(this.closebtn, "mouseout", this.highlight_btn, this.closebtn, true);

			this.prevbtn = YAHOO.util.Dom.get("lightboxprevbutton" + this.uniqueid);
			YAHOO.util.Event.on(this.prevbtn, "click",  this.prev_lightbox, this, true);
			YAHOO.util.Event.on(this.prevbtn, "mouseover", this.highlight_btn, this.prevbtn, true);
			YAHOO.util.Event.on(this.prevbtn, "mouseout", this.highlight_btn, this.prevbtn, true);

			this.nextbtn = YAHOO.util.Dom.get("lightboxnextbutton" + this.uniqueid);
			YAHOO.util.Event.on(this.nextbtn, "click",  this.next_lightbox, this, true);
			YAHOO.util.Event.on(this.nextbtn, "mouseover", this.highlight_btn, this.nextbtn, true);
			YAHOO.util.Event.on(this.nextbtn, "mouseout", this.highlight_btn, this.nextbtn, true);

			YAHOO.util.Event.on(YAHOO.util.Dom.get("lightboxlink" + this.uniqueid), "click",  this.hide_lightbox, this, true);

			this.img = YAHOO.util.Dom.get("lightboximg" + this.uniqueid);

			this.loader_link = this.img.src;
			this.loader_width = this.img.width;
			this.loader_height = this.img.height;

			this.imageloader.src = this.link;

			this.show_lightbox();
		}
		else if (this.click_triggered)
		{
			window.location = imagelink;
		}
	}
	else if (this.click_triggered)
	{
		window.location = imagelink;
	}
}

/**
* Shows, sizes and positions the window overlay/shade
*/
vB_Lightbox.prototype.show_overlay = function()
{
	if (this.check_status(2))
	{
		var vpi = fetch_viewport_info();

		if (Lightbox_overlay == null)
		{
			Lightbox_overlay = document.createElement("div");
			Lightbox_overlay.id = "Lightbox_overlay";

			var Lightbox_properties = {
				display: "none",
				position: "absolute",
				top: "0px",
				backgroundColor: "#000000",
				opacity: 0.85,
				zIndex: 10
			};

			if (document.dir == "rtl")
			{
				Lightbox_properties["right"] = "0px"
			}
			else
			{
				Lightbox_properties["left"] = "0px";
			}

			for (var property in Lightbox_properties)
			{
				if (YAHOO.lang.hasOwnProperty(Lightbox_properties, property))
				{
					YAHOO.util.Dom.setStyle(Lightbox_overlay, property, Lightbox_properties[property]);
				}
			}

			Lightbox_overlay = document.body.appendChild(Lightbox_overlay);
			Lightbox_overlay_select_handler = new vB_Select_Overlay_Handler(Lightbox_overlay);
		}

		YAHOO.util.Dom.setStyle(Lightbox_overlay, "display", "");
		YAHOO.util.Dom.setStyle(Lightbox_overlay, "width", vpi['w'] + "px");
		YAHOO.util.Dom.setStyle(Lightbox_overlay, "height", vpi['h'] + "px");
		YAHOO.util.Dom.setXY(Lightbox_overlay, [vpi['x'], vpi['y']]);

		Lightbox_overlay_select_handler.hide();
	}
}

/**
* Shows, sizes and positions the lightbox
*/
vB_Lightbox.prototype.show_lightbox = function()
{
	if (this.check_status(3))
	{
		if (Lightbox_current)
		{
			Lightbox_current.hide_lightbox(false, this, true);
		}

		this.show_overlay();

		if (!this.imageloader.complete && this.imageloader.readyState != 'complete')
		{
			// remove any old listeners that were hanging about, don't want to call this twice.
			YAHOO.util.Event.removeListener(this.imageloader, "load", this.show_lightbox);
			YAHOO.util.Event.on(this.imageloader, "load", this.show_lightbox, this, true);
		}
		else
		{
			this.img.src = this.link;
			this.resize_image();
			YAHOO.util.Dom.setStyle(this.closebtn, "display", "");
		}

		YAHOO.util.Dom.setStyle(this.lightbox, "display", "");
		YAHOO.util.Dom.setStyle(this.lightbox, "zIndex", 11);

		if (Lightbox_map[this.containerid].size() == 1)
		{
			YAHOO.util.Dom.setStyle(this.prevbtn, "display", "none");
			YAHOO.util.Dom.setStyle(this.nextbtn, "display", "none");
		}

		Lightbox_current = this;
		this.center_lightbox();
		this.active = true;
		this.enable_events();
	}
}

/**
* Hides the lightbox and the window overlay
*/
vB_Lightbox.prototype.hide_lightbox = function(event, lightbox, keepoverlay)
{
	if (event && event.type == 'keydown' && event.keyCode != 27)
	{
		return;
	}
	this.set_status(0, "hide_lightbox");
	this.disable_events();
	this.active = false;

	YAHOO.util.Dom.setStyle(this.lightbox, "display", "none");

	if (!keepoverlay)
	{
		YAHOO.util.Dom.setStyle(Lightbox_overlay, "display", "none");
	}

	Lightbox_overlay_select_handler.show();

	Lightbox_current = null;
}

/**
* Runs next lightbox
*/
vB_Lightbox.prototype.next_lightbox = function(event)
{
	var nextlightbox = null;

	if (Lightbox_map[this.containerid][this.uniqueid + 1] != null)
	{
		nextlightbox = Lightboxes[this.uniqueid + 1];
	}
	else
	{
		nextlightbox = Lightboxes[Lightbox_map[this.containerid].first()];
	}

	nextlightbox.load_lightbox();
}

/**
* Runs previous lightbox
*/
vB_Lightbox.prototype.prev_lightbox = function(event)
{
	var nextlightbox = null;

	if (Lightbox_map[this.containerid][this.uniqueid - 1] != null)
	{
		nextlightbox = Lightboxes[this.uniqueid - 1];
	}
	else
	{
		nextlightbox = Lightboxes[Lightbox_map[this.containerid].last()];
	}

	nextlightbox.load_lightbox();
}

/**
* Highlights a button control
*/
vB_Lightbox.prototype.highlight_btn = function()
{
	var color = YAHOO.util.Dom.getStyle(this, 'color');
	var bgcolor = YAHOO.util.Dom.getStyle(this, 'background-color');
	var inverted_color, inverted_bgcolor;

	inverted_color = ((color == "white" || color.toLowerCase() == "#ffffff") ? "black" : "white");
	inverted_bgcolor = ((bgcolor == "black" || bgcolor.toLowerCase() == "#000000") ? "white" : "black");

	YAHOO.util.Dom.setStyle(this, "color", inverted_color);
	YAHOO.util.Dom.setStyle(this, "background-color", inverted_bgcolor);
}

/**
* Centers the lightbox within the browser viewport
*/
vB_Lightbox.prototype.center_lightbox = function()
{
	center_element(this.lightbox);
}

/**
* Resizes and repositions the lightbox and the window overlay after the browser viewport has altered
*/
vB_Lightbox.prototype.handle_viewport_change = function()
{
	this.resize_image();
	this.center_lightbox();
	this.show_overlay();
}
/**
* Special case for IE - starts handle_viewport_change after a short delay
*/
vB_Lightbox.prototype.handle_viewport_change_ie = function()
{
	setTimeout("Lightboxes['" + this.uniqueid + "'].handle_viewport_change();", 100);
}


/**
* Resizes the lightbox image if it is too big for the viewport
*/
vB_Lightbox.prototype.resize_image = function()
{
	var vpi = fetch_viewport_info();
	var w = this.imageloader.width;
	var h = this.imageloader.height;

	if (w > vpi['w'] - this.minborder)
	{
		w = vpi['w'] - this.minborder;
		w = (w < this.mindimension ? this.mindimension : w);
		h = Math.ceil(this.imageloader.height * (w / this.imageloader.width));
	}

	if (h > vpi['h'] - this.minborder)
	{
		h = vpi['h'] - this.minborder;
		h = (h < this.mindimension ? this.mindimension : h);
		w = Math.ceil(this.imageloader.width * (h / this.imageloader.height));
	}

	this.img.setAttribute("width", w);
	this.img.setAttribute("height", h);

	this.img.setAttribute("title", this.name + "; \n" + this.imageloader.width + " x " + this.imageloader.height + " (@" + Math.ceil(w / this.imageloader.width * 100) + "%)");

	if (w < this.imageloader.width || h < this.imageloader.height)
	{
		console.info("vB_Lightbox :: Image original size: %dx%d, resizing to %dx%d", this.imageloader.width, this.imageloader.height, w, h);
	}
}

/**
* Enables various event handlers - onresize: re-do overlay and lightbox; onscroll: hide lightbox; onclick(overlay): hide lightbox
*/
vB_Lightbox.prototype.enable_events = function()
{
	if (!this.events_enabled)
	{
		YAHOO.util.Event.on(window, "resize", (is_ie ? this.handle_viewport_change_ie : this.handle_viewport_change), this, true);
		YAHOO.util.Event.on(window, "scroll", this.hide_lightbox, this, true);
		YAHOO.util.Event.on(window, "keydown", this.hide_lightbox, this, true);
		YAHOO.util.Event.on(Lightbox_overlay, "click", this.hide_lightbox, this, true);
		this.events_enabled = true;
	}
}

/**
* Disables the events set up by enable_events()
*/
vB_Lightbox.prototype.disable_events = function()
{
	if (this.events_enabled)
	{
		YAHOO.util.Event.removeListener(window, "resize", (is_ie ? this.handle_viewport_change_ie : this.handle_viewport_change));
		YAHOO.util.Event.removeListener(window, "scroll", this.hide_lightbox);
		YAHOO.util.Event.removeListener(window, "keydown", this.hide_lightbox);
		YAHOO.util.Event.removeListener(Lightbox_overlay, "click", this.hide_lightbox);
		this.events_enabled = false;
	}
}

/**
* Emulated assoc for a map of lightbox ids in individual posts/containers.
*/
vB_Lightbox_Container = function(){}

/**
* Add size method for objects emulating assoc arrays
*/
vB_Lightbox_Container.prototype.size = function()
{
	var length = 0;
	for (var m in this)
	{
		if (YAHOO.lang.hasOwnProperty(this, m))
		{
			length++;
		}
	}

	return length;
}

/**
* Gets the first item for an emulated assoc array
*/
vB_Lightbox_Container.prototype.first = function()
{
	for (var m in this)
	{
		if (YAHOO.lang.hasOwnProperty(this, m))
		{
			return m;
		}
	}
}

/**
* Gets the last item for an emulated assoc array
*/
vB_Lightbox_Container.prototype.last = function()
{
	var last;

	for (var m in this)
	{
		if (YAHOO.lang.hasOwnProperty(this, m))
		{
			last = m;
		}
	}

	return last;
}

/**
* Finds the index of an element in an emulated assoc array
*/
vB_Lightbox_Container.prototype.find = function(needle)
{
	var index = 0;
	for (var m in this)
	{
		if (YAHOO.lang.hasOwnProperty(this, m))
		{
			if (m == needle)
			{
				return index;
			}
			index++;
		}
	}

	return -1;
}

/**
* Checks that the <a> element passed is an attachment link
*
* @param	object	Attachment <a> link
*/
function is_lightbox_element(element)
{
	return (typeof(element.getAttribute("rel")) == 'string' && element.getAttribute("rel").match(/Lightbox[_]?(\d*)?/));
}

/**
* Creates the window overlay and hunts for attachment links to turn into lightboxes
*
* @param	mixed	Element/elementid containing attachment links
*/
function init_postbit_lightbox(element, events, reset_container)
{
	var webkit_version = userAgent.match(/applewebkit\/([0-9]+)/);
	// Safari 2.0 is broken, lets just skip if it is. Safari 3.0 is webkit 522.11
	if (webkit_version && webkit_version[1] < 522)
	{
		return;
	}

	// set a global default in case the value isn't present in a subsequent call (like quickedit)
	if (Lightbox_event_default === null)
	{
		Lightbox_event_default = events;
	}

	if (typeof(events) == "undefined" || events === false)
	{
		// click event + hover event is the default
		events = (Lightbox_event_default ? Lightbox_event_default : 0x1 + 0x2);
	}

	var elements = YAHOO.util.Dom.getElementsBy(is_lightbox_element, "a", element);
	for (var i = 0; i < elements.length; i++)
	{
		var uniqueid = Lightboxes.length;
		var containerid = elements[i].getAttribute("rel").match(/Lightbox[_]?(\d*)?/).pop();
		containerid = (containerid ? containerid : 0);

		Lightboxes[uniqueid] = new vB_Lightbox(elements[i], uniqueid, containerid, events);

		if (!Lightbox_map[containerid] || reset_container)
		{
			Lightbox_map[containerid] = new vB_Lightbox_Container();
			reset_container = false;
		}

		Lightbox_map[containerid][uniqueid] = uniqueid;
	}
}

/*======================================================================*\
|| ####################################################################
|| # NulleD By - FintMax
|| # CVS: $RCSfile$ - $Revision: 24191 $
|| ####################################################################
\*======================================================================*/
