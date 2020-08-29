var sPath = window.location.pathname;
var sPage = sPath.substring(sPath.lastIndexOf('/') + 1);

if (sPage == "apply") {
    const user_name = document.getElementById("name");
    const name_help = document.getElementById("name_help");

    user_name.addEventListener("input", function (event) {
        if (user_name.validity.valid === false) {
            user_name.classList.add("is-danger")
            name_help.classList.add("is-danger")
        }
        else {
            user_name.classList.remove("is-danger")
            user_name.classList.add("is-success")
            name_help.classList.remove("is-danger")
            name_help.classList.add("is-success")
        }

    })


    const email = document.getElementById("email");
    const email_help = document.getElementById("email_help");


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

    const outreach = document.getElementById("outreach");
    const outreach_help = document.getElementById("outreach_help");

    outreach.addEventListener("input", function (event) {
        if (outreach.validity.valid === false) {
            outreach.classList.remove("is-success")
            outreach_help.classList.remove("is-success")
            outreach.classList.add("is-danger");
            outreach_help.classList.add("is-danger");
        }
        else {
            outreach.classList.remove("is-danger")
            outreach_help.classList.remove("is-danger")
            outreach.classList.add("is-success");
            outreach_help.classList.add("is-success");
        }
    })
}



// var interest = document.getElementById("interest");

// interest.addEventListener("input", function (event) {
//     var result = interest.options[interest.selectedIndex].text;
//     var other_input = document.getElementById("other_input");
//     var subject_input = document.getElementById("subject_input");
//     if (result == "Other") {
//         other_input.hidden = false
//         subject_input.setAttribute("required","false")
//     }
//     else{
//         other_input.hidden = true
//         subject_input.setAttribute("required","true")
//     }
// })