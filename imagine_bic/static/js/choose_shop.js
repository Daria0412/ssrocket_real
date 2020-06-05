function bkfun(){
    history.back();
}
function hfun(){
    location.href="/index";
}
function bic_num(bic_num,company_num){
    if (bic_num==0) alert("현재 업체에 예약이 마감되었습니다.\n 다른 업체를 선택해주세요.");
    else{
        location.href=company_num+'/';
    }
}

