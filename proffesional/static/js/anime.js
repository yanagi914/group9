const targetElement = document.querySelectorAll(".title"); //cssの書き方で
//console.log(targetElement)

document.addEventListener("scroll", function () {
    for (let i = 0; i < targetElement.length; i++) {
        const getElementDistance = targetElement[i].
            getBoundingClientRect().top + targetElement[i].clientHeight * .6;

        if (window.innerHeight > getElementDistance) {
            targetElement[i].classList.add("show");
        }
    }
})

//jqueryを使った記述でスクロール

$(window).scroll(function () {
    $(".number").each(function () {
        var position = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > position - windowHeight + windowHeight * .4) {
            $(this).addClass('active');
        }

    });
});

$(window).scroll(function () {
    $(".table").each(function () {
        var position = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > position - windowHeight + windowHeight * .4) {
            $(this).addClass('fade-in');
        }

    });
});

$(window).scroll(function () {
    $(".bullets").each(function () {
        var position = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > position - windowHeight + windowHeight * .4) {
            $(this).addClass('fade-in');
        }
    //console.log(変数);で確認できる！
    });
});

$(window).scroll(function () {
    $(".word2").each(function () {
        var position = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > position - windowHeight + windowHeight * .4) {
            $(this).addClass('fade-in');
        }

    });
});

$(window).scroll(function () {
    $(".paragraph").each(function () {
        var position = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > position - windowHeight ) {
            $(this).addClass('fade-in');
        }

    });
});