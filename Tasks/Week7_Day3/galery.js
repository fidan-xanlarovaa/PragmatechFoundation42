let use=document.querySelectorAll(".use")


function ShowImage(some){
    
    /*for(i=1;i<=use.length;i++){
        use[i].classList.remove()
    }*/
    some.style.padding="50p x"
    let overlay=`
    <div class="overlay">
    <img src="${some.getAttribute('src')}" onclick="CloseImage(this)">
    </div>`

    document.body.innerHTML+=overlay
    some.style.padding="0px"
    


}

function CloseImage(some){
    let img=some.getAttribute('src')
    console.log(img)

    document.body.removeChild(some.parentElement)
}



