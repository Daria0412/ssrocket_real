window.onload = function(){
    addyear();
    addmonth();
    adddate();
}
function h(){
    var a=document.getElementById("a");
    var abc=document.getElementById("abc");
    var ba=document.getElementById("ba");
    var c=document.getElementById("bannap");
    var d=document.getElementById("bannap1");
    a.style.display='none';
    abc.style.display='none';
    ba.style.display='flex';
    c.style.display='none';
    d.style.display='flex';

}

function k(){
    var a=document.getElementById("a");
    var abc=document.getElementById("abc");
    var ba=document.getElementById("ba");
    var c=document.getElementById("bannap");
    var d=document.getElementById("bannap1");
    a.style.display='flex';
    abc.style.display='inline';
    ba.style.display='none';
    c.style.display='flex';
    d.style.display='none';

}

function sm() {
    lanForm.submit();
}
function put(borr){
    document.getElementById("val").value = borr;
    c.submit();
}
function setfun(){
    history.back();
}

function addyear(){
    var year=new Date().getFullYear();
    var obj = document.getElementById("c_year");
    var opt = "";

for(var i=year; i<=(year+1); i++){
    opt = document.createElement('option');
    opt.text = i;
    opt.value = i;
    obj.add(opt);
    }
}

function addmonth(){
    var obj = document.getElementById("c_month");
    var opt = "";

for(var i=1; i<=12; i++){
    opt = document.createElement('option');
    opt.text = i;
    opt.value = i;
    obj.add(opt);
    }
}

function adddate(){
    var obj = document.getElementById("c_date");
    var opt = "";
    var y= new Date().getFullYear();
    var m= (new Date().getMonth())-1;
    var day = ( new Date(y, m, 0) ).getDate();

    for(var i=1; i<=day; i++){
        opt = document.createElement('option');
        opt.text = i;
        opt.value = i;
        obj.add(opt);
        }
    }

function choose(){
    var result = confirm("예약을 수락하시겠습니까?");
        if(result){
            alert("예약을 수락하셨습니다!");
        }else{
            alert("예약을 거부하셨습니다!");
        }
}
