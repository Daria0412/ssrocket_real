function bkfun(){
    history.back();
}
function hfun(){
    location.href="/index";
}

function sm(company_loc){
    document.getElementById("search").value = company_loc;
    lanForm.submit();
}