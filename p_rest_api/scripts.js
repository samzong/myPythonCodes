$(function() {
    $('button').click(function() {
        var user = $('#txtUsername').val();
        var pass = $('#txtPassword').val();
        $.ajax({
            url: '/signUpUser',
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});