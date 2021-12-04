const targetElement = document.querySelectorAll(".title"); //cssの書き方で
//console.log(targetElement)

document.addEventListener("scroll",function(){
    for (let i = 0; i < targetElement.length; i++){
        const getElementDistance = targetElement[i].
        getBoundingClientRect().top + targetElement[i].clientHeight * .6;

        if (window.innerHeight > getElementDistance){
            targetElement[i].classList.add("show");
        }
    }
})