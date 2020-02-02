var CtrlPagenav = {

	elements: {'prev': null, 'next': null, 'start': null, 'end': null},
	title: 'Ctrl' + (is_opera ? '+Alt' : ''),

	init: function()
	{
		var blocks = YAHOO.util.Dom.getElementsByClassName('pagenav');
		for (var i = 0; i < blocks.length; i++)
		{
			var items = YAHOO.util.Dom.getElementsBy(this.is_pagenav_item, "a", blocks[i]);
			for (var ii = 0; ii < items.length; ii++)
			{
				var item = items[ii].getAttribute("rel");
				this.elements[item] = items[ii].href;
				switch (item)
				{
					case 'prev':
						items[ii].innerHTML = '<span class="pnarrow"><</span> ' + this.title;
					break;
					case 'next':
						items[ii].innerHTML = this.title + ' <span class="pnarrow">></span>';
					break;
				}
			}
		}
		if (blocks.length)
		{
			YAHOO.util.Event.on(document, "keydown", this.onkeydown, this, true);
		}
	},

	is_pagenav_item: function(item)
	{
		return (typeof(item.getAttribute("rel")) == 'string' && item.getAttribute("rel").match(/(prev|next|start|end)/));
	},

	onkeydown: function(e)
	{
		e = e || window.event;
		if (e.ctrlKey)
		{
			t = (e.target || e.srcElement);
			if (t.tagName != 'TEXTAREA' && !(t.tagName == 'INPUT' && t.type == 'text'))
			{
				var href = null;
				switch (e.keyCode)
				{
					case 37: // left
						href = this.elements[e.shiftKey ? 'start' : 'prev'];
					break;
					case 39: // right
						href = this.elements[e.shiftKey ? 'end' : 'next'];
					break;
				}
				if (href)
				{
					YAHOO.util.Event.stopEvent(e);
					window.location = href;
				}
			}
		}
	}
};
CtrlPagenav.init();