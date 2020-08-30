var firebaseConfig = {
    apiKey: "AIzaSyCoiMkQWKnNZIW5z4FszLRzPfF80cLsnY4",
    authDomain: "star-mortgage.firebaseapp.com",
    databaseURL: "https://star-mortgage.firebaseio.com",
    projectId: "star-mortgage",
    storageBucket: "star-mortgage.appspot.com",
    messagingSenderId: "636144215641",
    appId: "1:636144215641:web:5000b4eb967caddb703348",
    measurementId: "G-WER4MSNPTJ"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

// firebase.auth.Auth.Persistence.LOCAL;


function signUp() {
    var email = document.getElementById("email");
    var password = document.getElementById("password");


    firebase.auth().createUserWithEmailAndPassword(email.value, password.value).then(function (user) {
        var user = firebase.auth().currentUser;
        user.sendEmailVerification().then(function() {
            console.log("email sent");
          }).catch(function(error) {
            console.log(error);
          });
        console.log(user); // Optional
    }, function (error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log(errorCode + " " + errorMessage);
    });

    alert("Signed Up");
    alert("Check email to confirm valid email address");
}

function signIn() {
    var email = document.getElementById("email");
    var password = document.getElementById("password");

    firebase.auth().signInWithEmailAndPassword(email.value, password.value).catch(function (error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log(errorCode);
        console.log(errorMessage);
    });


    console.log("Signed in: " + email.value);
}

function signOut() {
    firebase.auth().signOut().then(function () {
        // Sign-out successful.
        console.log('User Logged Out!');
    }).catch(function (error) {
        // An error happened.
        console.log(error);
    });
}