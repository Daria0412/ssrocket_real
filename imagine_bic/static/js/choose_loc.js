function bkfun(){
    history.back();
}
function hfun(){
    location.href="/index";
}

function sm(company_loc){
    alert(document.getElementById("company_loc").value);
    document.getElementById("company_loc").value = company_loc;
    lanForm.submit();
}