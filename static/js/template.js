document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
  
      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
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

var nodeArray = [
    document.querySelector('#cardPurchaseHome'),
    document.querySelector('#cardRefinanceHome'),
    document.querySelector('#cardApplyNow'),

    document.querySelector('#mortgageCalculator'),
    document.querySelector('#principalCalculator'),
    document.querySelector('#homeAffordabilityCalculator'),
    document.querySelector('#homeValueEstimator'),

    document.querySelector('#interestOnlyCalculator'),
    document.querySelector('#extraPaymentCalculator'),
    document.querySelector('#taxBenifitsBuying'),
    document.querySelector('#whatsMyAPR'),

    document.querySelector('#basic_form'),

    // document.querySelector("#interest_apr")
];

ScrollReveal({ reset: true, duration: 2000, distance: '25%', scale: 0.85, delay: 300 }); //changes for all the elements
//ScrollReveal().reveal('#cardRobotics'); //can add ScrollReveal().reveal('.EXAMPLE', { delay: 500 }); to target a specific element
ScrollReveal().reveal(nodeArray);

ScrollReveal().reveal('#cardPurchaseHome', { origin: 'left' })
ScrollReveal().reveal('#cardRefinanceHome', { origin: 'bottom' })
ScrollReveal().reveal('#cardApplyNow', { origin: 'right' })

ScrollReveal().reveal('#mortgageCalculator', { origin: 'left' })
ScrollReveal().reveal('#principalCalculator', { origin: 'bottom' })
ScrollReveal().reveal('#homeAffordabilityCalculator', { origin: 'top' })
ScrollReveal().reveal('#homeValueEstimator', { origin: 'right' })

ScrollReveal().reveal('#interestOnlyCalculator', { origin: 'right' })
ScrollReveal().reveal('#extraPaymentCalculator', { origin: 'top' })
ScrollReveal().reveal('#taxBenifitsBuying', { origin: 'bottom' })
ScrollReveal().reveal('#whatsMyAPR', { origin: 'left' })



var sPath = window.location.pathname;
var sPage = sPath.substring(sPath.lastIndexOf('/') + 1);
if (sPage == "report_issue") {
    var email = document.getElementById("email");
    var email_help = document.getElementById("email_help");

    var user_name = document.getElementById("name");
    var name_help = document.getElementById("name_help");
    email.addEventListener("input", function (event) {
        if (email.validity.valid === false) {
            email.classList.add("is-danger")
            email_help.classList.remove("is-success")
            email_help.classList.add("is-danger")
            email_help.innerHTML = "This email is invalid"
        }
        else {
            email.classList.remove("is-danger")
            email.classList.add("is-success")
            email_help.classList.remove("is-danger")
            email_help.classList.add("is-success")
            email_help.innerHTML = "This email is valid"

        }

    })

    user_name.addEventListener("input", function (event) {
        if (user_name.validity.valid === false) {
            user_name.classList.add("is-danger")
        }
        else {
            user_name.classList.remove("is-danger")
            user_name.classList.add("is-success")
            name_help.classList.remove("is-danger")
            name_help.classList.add("is-success")
        }

    })
}


// const dropdown = document.getElementById("dropdown_item");
// dropdown.addEventListener('click', function(event) {
// //   event.stopPropagation();
//   dropdown.classList.add("is-active");
// })

// function onReady(callback) {
//     var intervalID = window.setInterval(checkReady, 1000);

//     function checkReady() {
//         if (document.getElementsByTagName('body')[0] !== undefined) {
//             window.clearInterval(intervalID);
//             callback.call(this);
//         }
//     }
// }

// function show(id, value) {
//     document.getElementById(id).style.display = value ? 'block' : 'none';
// }

// onReady(function () {
//     show('page', true);
//     show('loading', false);
// });

