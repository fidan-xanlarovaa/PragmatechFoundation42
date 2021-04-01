
let div=document.querySelector('img');
let prevBtn=document.querySelector('.Prev');
let nextBtn=document.querySelector('.Next');
let arrows=document.querySelector('#arrows');



let imgSrc=document.querySelector('#main img')
let imgTitle=document.querySelector('#text p')

let slider=[
    {
        img:'1.jpg',
        title:'Adventurer Cheesecake Brownie'
    },
    {
        img:'2.jpg',
        title:'Adventurer Lemon'
    },
    {
        img:'3.jpg',
        title:'Adventurer Donut'
    },

    {
        img:'4.jpg',
        title:'Adventurer Caramel'
    }

]

div.addEventListener('mouseover',function(){
    
    if (arrows.style.display === "none") {
      arrows.style.display = "block";
    } else {
      arrows.style.display = "none";
    }
  })

 

imgSrc.setAttribute('src',slider[0].img)
imgTitle.innerHTML=slider[0].title
i=0
prevBtn.addEventListener('click',function(){ 
        if(i>0){
            imgSrc.setAttribute('src',slider[i].img)
            imgTitle.innerHTML=slider[i].title
            i--
        }else{
            i=slider.length-1
        }
})

nextBtn.addEventListener('click',function(){
    if(i<slider.length){
        imgSrc.setAttribute('src',slider[i].img)
        imgTitle.innerHTML=slider[i].title
        i++
    }else{
        i=0;
    }
})