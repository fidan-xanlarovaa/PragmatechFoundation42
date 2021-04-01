let prev=document.querySelector('.prev')
let next=document.querySelector('.next')
let slider=document.querySelector('.main')
let slide=document.querySelector('.slider')
let width=slide.offsetWidth;
a=0
let number=document.querySelectorAll('.slidercont').length


prev.addEventListener('click',function(){
    if(a>=0 ){
        a=-number*width;
       }
       a+=width;
    slider.style.transform = `translateX(${a}px)`
    
   
   

})

next.addEventListener('click',function(){
    if(a==-(number-1)*width){
        a=width;
    }
    a-=width;
    slider.style.transform = `translateX(${a}px)`
    
    
})
/*


prev.addEventListener('click',function(){
    if(a==0 ){
        a=-4000;
       }
       a+=1000;
    slider.style.transform = `translateX(${a}px)`
    
   
   

})

next.addEventListener('click',function(){
    if(a==-30000){
        a=1000;
    }
    a-=1000;
    slider.style.transform = `translateX(${a}px)`
    
    
})
*/