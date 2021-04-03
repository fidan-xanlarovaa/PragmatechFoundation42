elem_status = true
let p=document.querySelectorAll("p")
console.log(p.length)
function showHide(current) {

    let a=current.firstElementChild.innerHTML
   
    if (elem_status) {   
        
        for(i=0;i<p.length;i++){
           
            if(p[i]!=  current.nextElementSibling){
            p[i].className = 'my-0 p-2 bg-light border hide'
            p[i].previousElementSibling.firstElementChild.innerHTML="+"
            
            }
        }
        
        current.nextElementSibling.className = 'my-0 p-2 bg-light border show'
        /*current.nextElementSibling.style.display = "block"*/
        current.firstElementChild.innerHTML="-"
            elem_status = false
        
    } 
    
    
    else {
        current.nextElementSibling.className = 'my-0 p-2 bg-light border hide'
        //current.nextElementSibling.style.display = "none"
        current.firstElementChild.innerHTML="+"
        elem_status = true
    }
    
    
      
    

}