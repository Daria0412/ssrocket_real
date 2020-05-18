function ch01fun(num){
    console.log(num)
    switch(num){
        case "1" : value = "modify";break;
        case "2" : value = "secession";break;
        case "3": value = "counsel";break;
        case "4": value = "logout";break;
    }
    document.getElementById("setUrl").value=value;
    setForm.submit();
}

function bkfun(){
    history.back();
}

function bkHome(user_info){
    if(user_info=="0"){location.href="/index";}
    if(user_info=="1"){location.href="/index/company";}
}