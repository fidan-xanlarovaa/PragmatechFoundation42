product=document.querySelector(".mehsul_h")
comments=document.querySelector(".comments11")
divComments=document.querySelector(".div-cm")
divProduct=document.querySelector(".div-pr")

function Show1(){
  product.className = 'mehsul_h d-block'
  comments.className= "comments11 d-none"
  divProduct.className="div-pr col-3 b-c-fbf9 cur-p b-25 d-flex align-items-center justify-content-center height-30  padding-t-15" 
  divComments.className="div-cm col-3 cur-p b-255 d-flex align-items-center justify-content-center height-30  padding-t-15"
}

function Show2(){
  product.className = 'mehsul_h d-none'
  comments.className= "comments11 d-block"
  divProduct.className="div-pr col-3  cur-p b-25 d-flex align-items-center justify-content-center height-30  padding-t-15" 
  divComments.className="div-cm col-3  cur-p b-255 d-flex align-items-center justify-content-center height-30  padding-t-15"
}


removeButtons=document.querySelectorAll(".remove")

for(i=0;i<removeButtons.length;i++){
  button=removeButtons[i]
  button.addEventListener("click",function(event){
    buttonClicked=event.target
    buttonClicked.parentElement.parentElement.parentElement.parentElement.remove()
  })
}


/*text=document.querySelector(".moving-t-d");
strText=text.textContent;
splitText=strText.split("");
text.textContent="";
for ( i=0; i<2*splitText.length; i++){
      
     text.innerHTML +="<span>"+ splitText[i] + "/<span>";
}

char=0;
timer=setInterval(onTick,70);

function onTick(){
  const span=text.querySelectorAll("span")[char];
  
  span.classList.add("list");
  char++;

  if(char===2*splitText.length){
    complete();
    return;
  }
}

function complete(){
  clearInterval(timer);
  timer=null;
}*/