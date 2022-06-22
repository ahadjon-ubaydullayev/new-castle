$(function() {
    $('.language__item:first-child').on('click', function(e) {
        e.preventDefault();
        $('.language__item:not(:first-child)').toggleClass('language-dropdown');
        $('.language__item:first-child').toggleClass('active');
    });

    $('.profile').on('click', function(e) {
        e.preventDefault();
        $('.profile-dropdown').toggleClass('active');
    });

    $('.profile').on('click', function(e) {
        e.preventDefault();
        $('.profile').toggleClass('active');
    });

    $('.menu-group').on('click', function(e) {
        e.preventDefault();
        $('.menu-group .menu-dropdown').toggleClass('menu-group__item');
        $('.menu-group .menu__link').toggleClass('active');
    });

    $('.menu-finance').on('click', function(e) {
        e.preventDefault();
        $('.menu-finance .menu-dropdown').toggleClass('menu-finance__item');
        $('.menu-finance .menu__link').toggleClass('active');
    });

    $('.log-in__form-item').on('focusin', function() {
        $(this).addClass('blur');
        if ($('.log-in__form-item:first').hasClass('blur')) {
            $('.login-label').addClass('blur');
        } else {
            $('.login-label').removeClass('blur');
        }
        if ($('.log-in__form-item:last').hasClass('blur')) {
            $('.password-label').addClass('blur');
        } else {
            $('.password-label').removeClass('blur');
        }
    });
    $('.log-in__form-item').on('focusout', function() {
        $(this).removeClass('blur');
        if ($('.log-in__form-item:first').hasClass('blur')) {
            $('.login-label').removeClass('blur');
        }
        if ($('.log-in__form-item:last').hasClass('blur')) {
            $('.password-label').removeClass('blur');
        }
    });

    $('.password-icon').on('mousedown', function() {
        $('#password').attr('type', 'text');
    });
    $('.password-icon').on('mouseup', function() {
        $('#password').attr('type', 'password');
    });

    $('.modal-input').on({
        change: function() {
            $(this).toggleClass('active');
        }
    })

    $('input').attr('autocomplete', 'off');


    $('.build-export__item').on('click', function() {
        $('.build-export__dropdown').toggleClass('build-export__dropdown_show');
    });

    $('select.modal-input').on('click', function() {
        this.classList.toggle('active');
    });



    // FILTER

    let filter = $('.filter');
    let filterList = $('.filter-list');

    filter.on('click', function() {
        filter.toggleClass('filter_active');
        filterList.toggleClass('filter-list_active');
        $('.filter-arrow').toggleClass('filter-arrow_active');
    });

    let category = $('.categories');
    let categoryList = $('.categories-list');

    category.on('click', function() {
        category.toggleClass('categories_active');
        categoryList.toggleClass('categories-list_active');
    });

    // JOURNAL

    $('.journal-date').on({
        click: function() {
            $(this).toggleClass('journal-date_active');
        },


    })

    $('#modal-delete-no').click(function(e) {
        e.preventDefault();
        $('.modal-delete').css('display', 'none')
    });

    $('.desk-fname a').click(function(e) {
        e.preventDefault(e);
        $('.modal-delete').css('display', 'block');
    });

    // PLUS

    $('.journal-list__item').click(function() {
        $(this).toggleClass('journal-list__item_active');
    })

    $(window).contextmenu(function(e) {
        e.preventDefault();
    })
    $('.desk-plus').click(function(e) {
        e.preventDefault();
    })

    $('.desk-plus').mousedown(function(e) {
        e.preventDefault();
        if (e.which == 3) {

            if ($('.desk-plus').next().hasClass('journal-check_active')) {
                $('.desk-plus').next().removeClass('journal-check_active');
            } else {
                $(this).next().toggleClass('journal-check_active');
            }
            if ($(this).next().hasClass('journal-check_active')) {
                $(this).text('-')
            } else {
                $(this).text('+')
            }

        }
    });

    $('.desk-table:not(:last)').dblclick(function() {
        window.location = '/view-attendance';
    })

    $('.journal-check__plus').click(function(e) {
        e.preventDefault();
        $('.journal-state').addClass('journal-state_active');
        $(this).parent().removeClass('journal-list__item_active');
    });



    $('#journalEditClose').click(function(e) {
        e.preventDefault();
        $('.journal-state').removeClass('journal-state_active');
    })

    let deskYellow = $('.desk-yellow');
    let deskYellowIcon = $('.journal-icon');
    deskYellow.has(deskYellowIcon).addClass('desk-yellow_blue')




});


let btnGrey = document.getElementsByClassName('grey-btn');
let body = document.getElementsByTagName('body')[0];

for (let i = 0; i < btnGrey.length; i++) {
    btnGrey[i].addEventListener('click', function() {
        this.querySelector('.blue-select').classList.toggle('blue-select_active');
    });
}

let edit = document.getElementsByClassName('build-table__item--7');
let item = document.getElementsByClassName('build-table__dropdown');

for (i = 0; i < edit.length; i++) {
    edit[i].addEventListener('click', function() {
        this.querySelector('.build-table__dropdown').classList.toggle('build-table__dropdown--active');
    });
}

let menuBtn = document.querySelector('.menu-btn');
let navbar = document.querySelector('.navbar');
let contentItem = document.querySelector('.content-item');
let header = document.querySelector('.header');
let btnWrapper = document.querySelector('.btn-wrapper');
let closer = document.querySelector('.btn-close');

if (body.contains(menuBtn)) {
    menuBtn.onclick = function() {
        navbar.classList.add('navbar--visible');
        contentItem.classList.add('menu-move');
        header.classList.add('menu-move');
        btnWrapper.classList.add('btn-move');
        closer.style.display = "block";
    }

    closer.onclick = function() {
        contentItem.classList.remove('menu-move');
        header.classList.remove('menu-move');
        btnWrapper.classList.remove('btn-move');
        navbar.classList.remove('navbar--visible');
        closer.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == navbar) {
            navbar.classList.remove('navbar--visible');
            contentItem.classList.remove('menu-move');
            header.classList.remove('menu-move');
            btnWrapper.classList.remove('btn-move');
        }
    }

}

let greyBtn = document.getElementsByClassName('grey-btn');

for (let i = 0; i < greyBtn.length; i++) {
    greyBtn[i].onclick = function() {
        this.querySelector('.grey-arrow').classList.toggle('active');
    }
}

// TEACHER / STUDENT VIEW


let teacherView = document.querySelectorAll('.teacher-table .build-table--light');

for (let i = 0; i < teacherView.length; i++) {
    teacherView[i].addEventListener('dblclick', function() {
        window.location = 'view-teacher.html'
    });
}

let studentView = document.querySelectorAll('.student-table.build-table--light');

for (let i = 0; i < studentView.length; i++) {
    studentView[i].addEventListener('dblclick', function() {
        window.location = 'view-student.html'
    });
}