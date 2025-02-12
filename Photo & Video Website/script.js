

let menu=document.querySelector('#menu-btn');
let navbar=document.querySelector('.header .navbar');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
};

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
};
var swiper = new Swiper(".home-slider", {
    loop:true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");

    if (loginForm) {
        loginForm.addEventListener("submit", function (e) {
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            if (username === "" || password === "") {
                e.preventDefault();
                alert("Both fields are required.");
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener("submit", function (e) {
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;
            const confirmPassword = document.getElementById("confirm-password").value;

            if (username === "" || password === "" || confirmPassword === "") {
                e.preventDefault();
                alert("All fields are required.");
            } else if (password !== confirmPassword) {
                e.preventDefault();
                alert("Passwords do not match.");
            }
        });
    }
});
document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("register-form");
  form.addEventListener("submit", function(event) {
      const password = document.getElementById("password").value;
      const confirmPassword = document.getElementById("confirm_password").value;
      
      if (password !== confirmPassword) {
          event.preventDefault();
          alert("Passwords do not match.");
      }
  });
});

