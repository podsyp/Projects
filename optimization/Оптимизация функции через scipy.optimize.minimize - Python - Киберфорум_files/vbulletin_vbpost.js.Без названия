function toggleimg(img)
{
  img_re = new RegExp("_collapsed\\.gif$");
  if (img.src.match(img_re))
  {
    img.src = img.src.replace(img_re, '.gif');
  }
  else
  {
    img_re = new RegExp("\\.gif$");
    img.src = img.src.replace(img_re, '_collapsed.gif');
  }
}

jQuery.fn.extend({

        vbshowRow: function ()
        {
                var animparam = new Object();
                animparam['opacity'] = 'show';
                if (!jQuery.browser.msie) animparam['height'] = 'show';
                this.find("td").not(".vbrowwrap").children().wrap("<div></div>").end().addClass("vbrowwrap");
                return this.show().find("div").not(".novbanim").animate(animparam,"fast");
        },

        vbhideRow: function ()
        {
                var animparam = new Object();
                animparam['opacity'] = 'hide';


                if (!jQuery.browser.msie) animparam['height'] = 'hide';
                var jqObject = this;
                this.find("td").not(".vbrowwrap").children().wrap("<div></div>").end().addClass("vbrowwrap");
                this.find("div").not(".novbanim").gt(0).animate(animparam,"fast");
                this.find("div").not(".novbanim").lt(1).animate(animparam,"fast", function()
                {
                        return jqObject.hide();
                });
                return jqObject;

        }

});

var vbpost_getting = 0;
function vbpost_get(postid)
{
	if ($("#vbpostrowget_"+postid).size() == 1)
	{
		var vbpostrowget = $("#vbpostrowget_"+postid);
		if (vbpostrowget.css("display") == "none")
		{
			vbpostrowget.vbshowRow();
		}
		else
		{
			vbpostrowget.vbhideRow();
			
		}
		toggleimg(fetch_object("vbpostimg_"+postid));
		return false;
	}

	if (!AJAX_Compatible)
	{
		// not AJAX compatible do not attempt to use AJAX
		return true;
	}
	else
	{
                if (vbpost_getting == 1)
                {
                        return false;
                }
                else
                {
                        vbpost_getting = 1;
                        setTimeout("vbpost_getting = 0", 1000);
                }
                var vbpost_param = new Object();
                vbpost_param['ajax'] = 1;
                vbpost_param['do'] = "vbpostget"
                vbpost_param['postid'] = postid;
		$("#vbpostimg_" + postid).attr("src",function() { return this.src.replace("expand","ajaxsmall")});
                $.post('vbpost_ajax.php', vbpost_param, function(data)
                {
			var lp = $('#vbpostrow_' + postid);
			var newrow = $(document.createElement("tr"));
			var newcol = $(document.createElement("td"));
			newrow.attr("id","vbpostrowget_" + postid).append(newcol).css("display","none");
			newcol.css("padding","0px").attr("colSpan",9).addClass("alt1").html(data);
			lp.after(newrow);
			$("#vbpostimg_" + postid).attr("src",function() { return this.src.replace("ajaxsmall","expand_collapsed")});
			newrow.find("#postmenu_"+postid+"_menu").addClass("novbanim").end().vbshowRow();
                });
		
		return false;
	}
}

