const button = document.getElementById("modal--teste");
const modal = document.getElementById("modal--div");

button.onclick = function () { 
  modal.style.display = "block";
}

const closeBtn = document.getElementsByClassName("close")[0];
closeBtn.onclick = function() {
	modal.style.display = "none";
}

// ---------------------------------

const button1 = document.getElementById("modal--teste-two");
const modal1 = document.getElementById("modal--div-two");

button1.onclick = function () { 
  modal1.style.display = "block";
}

const closeBtn1 = document.getElementsByClassName("close-two")[0];
closeBtn1.onclick = function() {
	modal1.style.display = "none";
}

const modal3 = document.getElementById("modal--div-three");
const closeBtn2 = document.getElementsByClassName("close-three")[0];
closeBtn2.onclick = function(){
  modal3.style.display ="none";
}

function openModalcnt(){
  modal3.style.display = "block";
}


