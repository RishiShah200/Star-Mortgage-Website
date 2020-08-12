document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }

});

// document.getElementById("p1").innerHTML = "New text!";

const email = document.getElementById("email");
const email_help = document.getElementById("email_help");


email.addEventListener("input", function (event) {
    if(email.validity.valid === false){
        email.classList.add("is-danger")
        email_help.classList.remove("is-success")
        email_help.classList.add("is-danger")
        email_help.innerHTML = "This email is invalid"
    }
    else{
        email.classList.remove("is-danger")
        email.classList.add("is-success")
        email_help.classList.remove("is-danger")
        email_help.classList.add("is-success")
        email_help.innerHTML = "This email is valid"
        
    }
    
    })

const user_name = document.getElementById("user_name");
const name_help = document.getElementById("name_help");

user_name.addEventListener("input", function (event) {
    if(user_name.validity.valid === false){
        user_name.classList.add("is-danger")
    }
    else{
        user_name.classList.remove("is-danger")
        user_name.classList.add("is-success")
        name_help.classList.remove("is-danger")
        name_help.classList.add("is-success")
    }
    
    })

const mode_toggle = document.getElementById("switch_example");
const theme_text = document.getElementById("theme")

mode_toggle.addEventListener("input", function (event) {
    if (mode_toggle.checked.checked === true){
        theme_text.href = "https://unpkg.com/bulmaswatch/darkly/bulmaswatch.min.css"
        
    }
    })
