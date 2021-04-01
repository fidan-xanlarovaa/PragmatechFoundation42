let prev=document.querySelector(".prev")
let next=document.querySelector(".next")
let slider=document.querySelector(".main")
let slide=document.querySelector(".slider")
let width=slide.offsetWidth

a=0

number= document.querySelectorAll(".slidercont").length

prev.addEventListener('click',function(){
    if(a!=0 ){
        a+=width;
       }
       
    slider.style.transform = `translateX(${a}px)`
    
   
   

})

next.addEventListener('click',function(){
    if(a!=-(number-1)*width){
        a-=width;
    }
    
    slider.style.transform = `translateX(${a}px)`
    
    
})