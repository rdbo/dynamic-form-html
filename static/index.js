var input_html = `
<input type="number" name="numbers[]" placeholder="Insert a number">
<button type="button" onclick="del_input(this);">Remove</button>
`

var myinputs = document.getElementById("my-inputs");

function add_input() {
	myinput = document.createElement("div");
	myinput.innerHTML = input_html;
	myinputs.appendChild(myinput);
}

function del_input(el) {
	myinputs.removeChild(el.parentElement);
}
