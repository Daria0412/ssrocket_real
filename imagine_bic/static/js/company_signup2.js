function bkfun(){
    history.back();
}

function sm(){
    location.href="main.html"
    joinForm.submit();
}

window.onload=
function addmonth(){
    var obj = document.getElementById("bicycle_num");
    var opt = "";

for(var i=1; i<=100; i++){
    opt = document.createElement('option');
    opt.text = i;
    opt.value = i;
    obj.add(opt);
    }
}