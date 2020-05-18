function bkfun(){
    history.back();
}
function hfun(){
    location.href="/index";
}
function sd(){
    location.href="{% url 'shop_detail' pk=company.company_num %}"
}

