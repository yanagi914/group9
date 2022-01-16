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

$(function(){
    $('.text').children().addBack().contents().each(function() {
      $(this).replaceWith($(this).text().replace(/(\S)/g, '<p><span>$&</span></p>'));
    });
  });
  $(window).on('load', function(){
    $(".text").addClass("active");
  });

  $(function(){
    $(".check1").on('click',function(){
      $(".is-open1").slideToggle();
    });
    
  });

  $(function(){
    $(".check2").on('click',function(){
      $(".is-open2").slideToggle();
    });
    
  });

  $(function(){
    $(".check3").on('click',function(){
      $(".is-open3").slideToggle();
    });
    
  });

  $(function(){
    $(".check4").on('click',function(){
      $(".is-open4").slideToggle();
    });
    
  });

  $(function(){
    $(".check5").on('click',function(){
      $(".is-open5").slideToggle();
    });
    
  });

  $(function(){
    $(".check6").on('click',function(){
      $(".is-open6").slideToggle();
    });
    
  });

  $(function(){
    $(".check7").on('click',function(){
      $(".is-open7").slideToggle();
    });
    
  });

  $(function(){
    $(".check8").on('click',function(){
      $(".is-open8").slideToggle();
    });
    
  });

  $(function(){
    $(".check9").on('click',function(){
      $(".is-open9").slideToggle();
    });
    
  });