$(document).ready( function() {

    $("#register-button").click( function() {
        $("#register").removeClass('hide');
    });
    $("#cancel-register-button").click(function() {
       $("#register").addClass('hide'); 
    });
});