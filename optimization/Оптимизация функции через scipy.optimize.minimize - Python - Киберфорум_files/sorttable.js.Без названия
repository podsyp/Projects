// makes tables sortable
// based on http://www.kryogenix.org/code/browser/sorttable/
// file is part of the vB Code [table] product by StGaensler
// (available from http://www.vbulletin.org/forum/showthread.php?t=107985)
// file rev: 0.1.5.3.3

addEvent(window, "load", sortables_init);

var SORT_COLUMN_INDEX;

function sortables_init() {
   // Find all tables with class sortable and make them sortable
   if (!document.getElementsByTagName) return;
   tbls = document.getElementsByTagName("table");
   for (ti=0;ti<tbls.length;ti++) {
		thisTbl = tbls[ti];
		if (((' '+thisTbl.className+' ').indexOf("sortable") != -1) && (thisTbl.id)) {
			ts_makeSortable(thisTbl);
		}
	}
}

function ts_makeSortable(table) {
	if (table.rows && table.rows.length > 0) {
		var firstRow = table.rows[0];
	}
	if (!firstRow) return;

	// We have a first row: assume it's the header, and make its contents clickable links
	for (var i=0;i<firstRow.cells.length;i++) {
		var cell = firstRow.cells[i];
		var txt = cell.innerHTML; //ts_getInnerText(cell);
		cell.innerHTML = '<a href="#" class="sortheader" onclick="ts_resortTable(this, '+i+');return false;">'+txt+'<span class="sortarrow">&nbsp;</span></a>';

		// create link for sorting the column
		//var link = document.createElement('a');
		//link.className = 'sortheader';
		//link.href = '#';
		//var onclick = document.createAttribute("onclick")
		//onclick.nodeValue = 'ts_resortTable(this, '+i+');return false;'
		//link.setAttributeNode(onclick);

		// move the current contents of the cell into the hyperlink
		//var inner = cell.childNodes;
		//for (var j=0;j<inner.length;j++) {
		//	link.appendChild(inner[j]);
		//}

		// create and append sortarrow span
		//var span = document.createElement('span');
		//span.className = 'sortarrow';
		//span.appendChild(document.createTextNode('\u00A0'));
		//link.appendChild(span);

		// add the new link back into the cell
		//cell.appendChild(link);
	}
}

function ts_getInnerText(el) {
	if (typeof el == "string") return el;
	if (typeof el == "undefined") { return el };
	if (el.innerText) return el.innerText;	//Not needed but it is faster
	var str = "";

	var cs = el.childNodes;
	var l = cs.length;
	for (var i = 0; i < l; i++) {
		switch (cs[i].nodeType) {
			case 1: //ELEMENT_NODE
				str += ts_getInnerText(cs[i]);
				break;
			case 3:	//TEXT_NODE
				str += cs[i].nodeValue;
				break;
		}
	}
	return str;
}

function ts_resortTable(lnk,clid) {
	// get the span
	var span;
	for (var ci=0;ci<lnk.childNodes.length;ci++) {
		if (lnk.childNodes[ci].tagName && lnk.childNodes[ci].tagName.toLowerCase() == 'span') span = lnk.childNodes[ci];
	}
	var spantext = ts_getInnerText(span);
	var td = lnk.parentNode;
	var column = clid || td.cellIndex;
	var table = getParent(td,'TABLE');

	// Work out a type for the column
	if (table.rows.length <= 1) return;
	var itm = ts_getInnerText(table.rows[1].cells[column]);
	sortfn = ts_sort_caseinsensitive;
	if (itm.match(/^\d\d[\/-]\d\d[\/-]\d\d\d\d$/)) sortfn = ts_sort_date;
	if (itm.match(/^\d\d[\/-]\d\d[\/-]\d\d$/)) sortfn = ts_sort_date;
	if (itm.match(/^[£$]/)) sortfn = ts_sort_currency;
	if (itm.match(/^[\d\.]+$/)) sortfn = ts_sort_numeric;
	SORT_COLUMN_INDEX = column;
	var firstRow = new Array();
	var newRows = new Array();
	for (i=0;i<table.rows[0].length;i++) { firstRow[i] = table.rows[0][i]; }
	for (j=1;j<table.rows.length;j++) { newRows[j-1] = table.rows[j]; }

	newRows.sort(sortfn);

	if (span.getAttribute("sortdir") == 'down') {
		ARROW = '&nbsp;<img src="' + IMGDIR_BUTTON + '/sortasc.gif" />';
		newRows.reverse();
		span.setAttribute('sortdir','up');
	} else {
		ARROW = '&nbsp;<img src="' + IMGDIR_BUTTON + '/sortdesc.gif" />';
		span.setAttribute('sortdir','down');
	}

	// We appendChild rows that already exist to the tbody, so it moves them rather than creating new ones
	// don't do sortbottom rows
	for (i=0;i<newRows.length;i++) {
		if (!newRows[i].className || (newRows[i].className && (newRows[i].className.indexOf('sortbottom') == -1))){
			table.tBodies[0].appendChild(newRows[i]);
		}
	}
	// do sortbottom rows only
	for (i=0;i<newRows.length;i++) {
		if (newRows[i].className && (newRows[i].className.indexOf('sortbottom') != -1)){
			table.tBodies[0].appendChild(newRows[i]);
		}
	}

	// restore alternating row background by StG
	for (i=1;i<table.rows.length;i++) {
		if (table.rows[i].className.substring(0, 3) == "alt"){
			if (i%2){
				table.rows[i].className = "alt2" + table.rows[i].className.substring(4);
			} else {
				table.rows[i].className = "alt1" + table.rows[i].className.substring(4);
			}
		}
	}

	// Delete any other arrows there may be showing
	var allspans = document.getElementsByTagName("span");
	for (var ci=0;ci<allspans.length;ci++) {
		if (allspans[ci].className == 'sortarrow') {
			if (getParent(allspans[ci],"table") == getParent(lnk,"table")) { // in the same table as us?
				allspans[ci].innerHTML = '&nbsp;';
			}
		}
	}

	span.innerHTML = ARROW;
}

function getParent(el, pTagName) {
	if (el == null) return null;
	else if (el.nodeType == 1 && el.tagName.toLowerCase() == pTagName.toLowerCase())	// Gecko bug, supposed to be uppercase
		return el;
	else
		return getParent(el.parentNode, pTagName);
}
function ts_sort_date(a,b) {
	aa = ts_getInnerText(a.cells[SORT_COLUMN_INDEX]);
	bb = ts_getInnerText(b.cells[SORT_COLUMN_INDEX]);
	if (aa.length == 10) {
		dt1 = aa.substr(6,4)+aa.substr(3,2)+aa.substr(0,2);
	} else {
		yr = aa.substr(6,2);
		if (parseInt(yr) < 50) { yr = '20'+yr; } else { yr = '19'+yr; }
		dt1 = yr+aa.substr(3,2)+aa.substr(0,2);
	}
	if (bb.length == 10) {
		dt2 = bb.substr(6,4)+bb.substr(3,2)+bb.substr(0,2);
	} else {
		yr = bb.substr(6,2);
		if (parseInt(yr) < 50) { yr = '20'+yr; } else { yr = '19'+yr; }
		dt2 = yr+bb.substr(3,2)+bb.substr(0,2);
	}
	if (dt1==dt2) return 0;
	if (dt1<dt2) return -1;
	return 1;
}

function ts_sort_currency(a,b) {
	aa = ts_getInnerText(a.cells[SORT_COLUMN_INDEX]).replace(/[^0-9.]/g,'');
	bb = ts_getInnerText(b.cells[SORT_COLUMN_INDEX]).replace(/[^0-9.]/g,'');
	return parseFloat(aa) - parseFloat(bb);
}

function ts_sort_numeric(a,b) {
	aa = parseFloat(ts_getInnerText(a.cells[SORT_COLUMN_INDEX]));
	if (isNaN(aa)) aa = 0;
	bb = parseFloat(ts_getInnerText(b.cells[SORT_COLUMN_INDEX]));
	if (isNaN(bb)) bb = 0;
	return aa-bb;
}

function ts_sort_caseinsensitive(a,b) {
	aa = ts_getInnerText(a.cells[SORT_COLUMN_INDEX]).toLowerCase();
	bb = ts_getInnerText(b.cells[SORT_COLUMN_INDEX]).toLowerCase();
	if (aa==bb) return 0;
	if (aa<bb) return -1;
	return 1;
}

function ts_sort_default(a,b) {
	aa = ts_getInnerText(a.cells[SORT_COLUMN_INDEX]);
	bb = ts_getInnerText(b.cells[SORT_COLUMN_INDEX]);
	if (aa==bb) return 0;
	if (aa<bb) return -1;
	return 1;
}


function addEvent(elm, evType, fn, useCapture)
{
  if (elm.addEventListener){
	elm.addEventListener(evType, fn, useCapture);
	return true;
  } else if (elm.attachEvent){
	var r = elm.attachEvent("on"+evType, fn);
	return r;
  } else {
	alert("Handler could not be removed");
  }
}
