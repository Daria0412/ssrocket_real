function ch01fun(){
    location.href="/index";
    var img=document.getElementById("traveler");
    // img.src= "../../static/img/tr-bt2.png";
    document.getElementById("user_info").value=0
    useForm.submit();
}

function ch02fun(){
    location.href="/index/company/";
    var img=document.getElementById("company");
    // img.src= "../../static/img/comp-bt2.png";
    document.getElementById("user_info").value=1
    useForm.submit();
}

function gou(){
    location.href='index/';
}

function goc(){
    location.href='/index/company/';
}