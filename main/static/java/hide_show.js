function showText(elem,zag)
{
    if (document.getElementById(elem).className == "show"){
		document.getElementById(elem).className = "hide";
		document.getElementById(zag).className = "hide_h";
	}
	else{
		document.getElementById(elem).className = "show";
		document.getElementById(zag).className = "show_h";
	}
}