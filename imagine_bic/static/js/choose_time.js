function bkfun(){
    history.back();
}

function hfun(){
    location.href="/index";
}
function f_fun(){
    timeForm.submit();
}

window.onload = function() {
    addyear();
    addmonth();
    adddate();
}

function addyear(){
    var year=new Date().getFullYear();
    var obj = document.getElementById("r_year");
    var opt = "";

for(var i=year; i<=(year+1); i++){
    opt = document.createElement('option');
    opt.text = i;
    opt.value = i;
    obj.add(opt);
    }
}

function addmonth(){
    var obj = document.getElementById("r_month");
    var opt = "";

for(var i=1; i<=12; i++){
    opt = document.createElement('option');
    opt.text = i;
    opt.value = i;
    obj.add(opt);
    }
}

function adddate(){
    var obj = document.getElementById("r_date");
    var opt = "";
    var y= new Date().getFullYear();
    var m= new Date().getMonth();
    var day = ( new Date( y, m, 0) ).getDate();

    for(var i=1; i<=day; i++){
        opt = document.createElement('option');
        opt.text = i;
        opt.value = i;
        obj.add(opt);
        }
    }






