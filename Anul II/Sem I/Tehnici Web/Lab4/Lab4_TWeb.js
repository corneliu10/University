function counter(){
	var c = 0;
	function inc(){
		c++;
	}
	inc.ret = function(){
		return c;
	}
	return inc;
}

var c = counter();
var elements = document.getElementsByClassName("ass");

function change(index) {
    elements[index].innerHTML = "saladass " + index;
}

function showc(){
	//c();
    //document.getElementById("counter").innerHTML = c.ret();
    for(let i=0; i<elements.length; ++i) {
        var btn = document.createElement("BUTTON");
        var t = document.createTextNode("Button " + i);
        btn.appendChild(t);

        document.body.appendChild(btn);
        btn.onclick = function(){
            change(i);
        };
        btn.addEventListener('click', function(){});
    }
}	


// window.addEventListener( 'load' , ()=> {
// 	document.getElementById("counter").previousSibling.addEventListener('click',showc);
// })

// var btn = document.createElement('B');
// var d = document.getElementById("counter");
// d.insertBefore(btn, d);
// btn.onclick = function(){};
// btn.addEventListener('click',function(){});

var btn = document.createElement("BUTTON");        // Create a <button> element
var t = document.createTextNode("CLICK ME");       // Create a text node
btn.appendChild(t);                                // Append the text to <button>
document.body.appendChild(btn);                 // Append <button> to <body>
btn.onclick = function(){ showc();};
btn.addEventListener('click', function(){});