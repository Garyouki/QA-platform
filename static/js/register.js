//This function will be executed when the web page is completely loaded
$(function () {
    $("#captcha-btn").click(function (event) {
        // blocking default click handling
        event.preventDefault()

        // get the input for element which name is "email"
        var email = $("input[name='email']").val();
        // send verification using ajax
        $.ajax({
            url: "/auth/captcha/email?email=" + email,
            method: "GET",
            success: function (result) {
                var code = result['code'];
                // if send successfully, alert the successful message
                if (code == 200) {
                    alert("email verification send successfully")
                }
                else {
                    alert(result['message'])
                }
            },
            fail: function (error) {
                console.log(error);
            }
        })
    });
});