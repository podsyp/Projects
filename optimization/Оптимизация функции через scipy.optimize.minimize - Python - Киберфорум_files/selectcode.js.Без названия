function selectCode(evt)
{
    evt.preventDefault();
    var link = evt.target;
    var table = link.parentElement.parentElement.parentElement.parentElement;
    var pre = table.querySelectorAll("pre.de1")[1];
    var rng = document.createRange();
    rng.selectNodeContents(pre);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(rng);
}
 
var heads = document.querySelectorAll("td.head");
for(var i = 0; i < heads.length; i++)
  {
    var link = document.createElement("a");
    //link.style.marginLeft = "10px"
    link.style.float = "right"
    link.style.color = "#606060"
    link.style.fontWeight = "normal"
    link.textContent = "Выделить код";
    link.href = "#";
    link.addEventListener("click",selectCode,false);  
    heads[i].appendChild(link);
  }