let images=document.querySelectorAll(".obj-cover")


function ShowImage(some){
    
    /*for(i=1;i<=use.length;i++){
        use[i].classList.remove()
    }*/
    some.className="obj-cover width-50"
    let overlay=`
    <div class="overlay">
    <img src="${some.getAttribute('src')}" onclick="CloseImage(this)">
    </div>`

    document.body.innerHTML+=overlay


}

function CloseImage(some){
    let img=some.getAttribute('src')
    console.log(img)


    for(i=0;i<images.length;i++){
        if(img==images[i].getAttribute("src")){
            console.log(images[i])
            images[i].className="obj-cover width-100"
        }
    }
    

    document.body.removeChild(some.parentElement)
}



