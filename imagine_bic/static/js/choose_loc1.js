function bkfun(){
    history.back();
}
function hfun(){
    location.href="/index";
}

<<<<<<< HEAD:imagine_bic/static/js/choose_loc1.js
function sm(){
    alert("HELLO");
=======
function sm(company_loc){
    document.getElementById("search").value = company_loc;
>>>>>>> ebd9a93655c08be44186181701d919bb2c3408eb:imagine_bic/static/js/choose_loc.js
    lanForm.submit();
}