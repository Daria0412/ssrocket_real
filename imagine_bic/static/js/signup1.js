function bkfun(){
    history.back();
}

function chfun(){
    location.href="/signin";
}

function sm() {
    joinForm.submit();
}

$(function () {
    var id = $("#id").val();
    var name = $("#name").val();
    var pwd = $("#pwd").val();

    if (id === "" || name === "" || pwd === "") {
        $("#joinBt").attr("disabled", "disabled");
    }
});

/* 중복체크! */
$(function () {
    /* 아이디 수정했을 때 */
    $('#id').change(function () {
        $('#barEmailck').show();
        $("#joinBt").attr("id_check_result", "fail");
        $("#joinBt").attr("disabled", "disabled");
    });

    // 중복확인 버튼을 눌렀을 때
    $('#barEmailck').click(function () {
        var id = $('#id').val();
        // 이메일 란이 공백일 경우
        if (id == '') {
            alert('이메일을 입력해주세요.');
            $("#joinBt").attr("id_check_result", "fail");
            $("#joinBt").attr("disabled", "disabled");
            return false;
        }
        // debugger;
        $.ajax({
            url: 'check_email',
            data: {
                id: id
            },
            type: 'get',
            dataType: 'json',
            success: function (response) {
                if (response.result !== 'success') {
                    console.error(response.data)
                    return;
                }
                if (response.data === 'exist') {
                    alert("존재하는 이메일 입니다!");
                    $('#id').val('').focus();
                    $("#joinBt").attr("id_check_result", "fail");
                    $("#joinBt").attr("disabled", "disabled");
                    return;
                } else {
                    alert("사용 가능한 이메일입니다!");
                    $("#joinBt").attr("id_check_result", "success");
                    $("#joinBt").removeAttr("disabled");
                    $('#barEmailck').hide();
                    return;
                }
                // console.log(response)
            },
            error: function (xhr, error) {
                alert("서버와의 통신에서 문제가 발생했습니다.");
                $("#joinBt").attr("id_check_result", "fail");
                $("#joinBt").attr("disabled", "disabled");
                console.error("error : " + error);
            }
        });

        return false;
    });

    // 가입 버튼 눌렀을 때
    $('#joinForm').submit(function () {
        console.log($("#joinBt").attr("id_check_result"));
        if ($("#joinBt").attr("id_check_result") === "fail") {
            alert("이메일 중복 확인를 해주시기 바랍니다.");
            $("#joinBt").attr("disabled", "disabled");
            $("#id").focus();
            return false;
        }
    });

    $("#id").on("propertychange change keyup paste input", function () {
        $('#barEmailck').show();
        $("#joinBt").attr("id_check_result", "fail");
    });
});

// 비밀번호 확인
$(function () {
    $("input").keyup(function () {
        var pwd = $("#pwd").val();
        var pwdCk = $("#pwdck").val();
        if (pwd !== "" || pwdCk !== "") {
            if (pwd === pwdCk) {
                $("#alert-success").show();
                $("#alert-danger").hide();
                $("#joinBt").removeAttr("disabled");
            } else {
                $("#alert-success").hide();
                $("#alert-danger").show();
                $("#joinBt").attr("disabled", "disabled");
            }
        } else {
            $("#alert-success").hide();
            $("#alert-danger").show();
            $("#joinBt").attr("disabled", "disabled");
        }
    });
});