function bkfun(){
    history.back();
}
function hfun(){
    location.href="/index";
}

function sm(company_loc){
    alert(document.getElementById("search").value);
    document.getElementById("search").value = company_loc;
    alert(document.getElementById("search").value);
    lanForm.submit();
}