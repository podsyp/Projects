/**
 * Simple vBulletin editor AutoSave
 * Supports WYSIWYG editor and text box editor
 * Requires storage support in browser
 * Author: Adam Oest
 * Version: 0.5
 */
try
{
	if (window.localStorage || localStorage) 
	{
		// Returns whether or not given data is "empty"
		function isEmpty(data)
		{
			return (
				data == '<br />' 
				|| data == '<br>' 
				|| data == '<p></p>'
				|| data.replace(' ','').length == 0
			);
		}

		// Adds an event to the specified element based on browser
		function newEvent(element, event, callback)
		{
			// Non-IE
			if (element && element.addEventListener)
			{
				element.addEventListener(event, callback, false);
			}
			// IE
			else if (element && element.attachEvent)
			{
				element.attachEvent('on' + event, callback);
			}
		}

		// Replaces contents of text area with data
		function writeToTextarea()
		{
			formObject.message.value = storage.getItem(storageKey);

			// Firefox
			if (editorObject)
			{
				editorObject.innerHTML = storage.getItem(storageKey);
			}

			//console.log('AutoSave :: Auto-fetched from storage ' + storageKey);
		}

		// Replaces contents of editor with data
		function writeToEditor()
		{
			editorObject.innerHTML = storage.getItem(storageKey);
			//console.log('AutoSave :: Auto-fetched from storage ' + storageKey);
		}

		// Clears stored data
		function clearStorage()
		{
			storage.removeItem(storageKey);
			//console.log('AutoSave :: Cleared cache for ' + storageKey);
		}
	
		// Sets stored data
		function setStorage()
		{
			var data = getData();
			if (!isEmpty(data))
			{
				storage.setItem(storageKey, data);
			}
			else
			{
				clearStorage();
			}
		}

		// Gets text currently in the editor
		function getData()
		{	
			if (editorObject)
			{
				return editorObject.innerHTML;
			}
			else if (formObject && formObject.message)
			{
				return formObject.message.value;
			}
		}
	
		// Restores text into the editors / registers event handlers
		function insertData()
		{
			// Detect the editor object
			if (vB_Editor)
			{
				for (var i in vB_Editor)
				{
					editorObject = vB_Editor[i].editdoc.body;
					var rootEditorObject = vB_Editor[i].editdoc;
					break;
				}
			}

			// WYSIWYG editor mode, but also check if message field is empty (inside PMs)
			if (editorObject && formObject.id != 'message_form')
			{
				// IE, you suck
				if (storage.getItem(storageKey) && isEmpty(editorObject.innerHTML))
				{
					writeToEditor();
				}

				newEvent(editorObject,'keyup',setStorage);
				// Firefox
				if (rootEditorObject)
				{
					newEvent(rootEditorObject,'keyup',setStorage);
				}
			}
			// PMs and simple text editor
			else if (formObject && formObject.message)
			{
				if (storage.getItem(storageKey) && storage.getItem(storageKey) != formObject.message.value)
				{
					// Make an exception for PMs
					/*if (!isEmpty(formObject.message.value) && formObject.id == 'message_form')
					{
						if (confirm('The system has found an unfinished message draft.  Replace the editor contents with this draft?\n\n' + storage.getItem(storageKey)))
						{
							writeToTextarea();
						}
						else
						{
							clearStorage();
						}
					}
					else
					{*/
						writeToTextarea();
					//}
				}

				newEvent(formObject.message,'keyup',setStorage);
				// Firefox
				if (rootEditorObject)
				{
					newEvent(rootEditorObject,'keyup',setStorage);
				}
			}
		}

		// IE, you suck
		if (localStorage)
		{
			var storage = localStorage;
		}
		else
		{
			var storage = window.localStorage;
		}
		
		// Determine the URL for which data is being stored, ignore anchors
		try
		{
			var urllen = window.location.href.split('/');
			var dl = urllen[0].length + urllen[2].length + 2;
		}
		catch (error)
		{
			var dl = 0;
		}

		var storageKey = window.location.href.slice(dl);
		if (storageKey.indexOf('#') != -1)
		{
			storageKey = storageKey.slice(0, storageKey.indexOf('#'));
		}
		
		// Switch for WYSIWYG mode
		var editorObject = false;

		// Find the editor form
		if (document.vbform)
		{
			var formObject = document.vbform;
		}
		else if (document.getElementById('message_form'))
		{
			var formObject = document.getElementById('message_form');
		}

		// Main execution, no onload needed if script placed below editor
		if (formObject)
		{
			insertData();
			newEvent(formObject,'submit',clearStorage);

			var buttons = formObject.getElementsByClassName('button');
			for (var i = 0; i < buttons.length; i++)
			{
				if (buttons[i].name != 'preview')
				{
					newEvent(buttons[i],'click',clearStorage);
					newEvent(buttons[i],'mousedown',clearStorage);
				}
			}
		}
	}
}
catch (err) 
{ 
	console.log('AutoSave encountered an error ' + err);
}
