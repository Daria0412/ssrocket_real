function ch01fun(num){
    switch(num){
        case 1 : value = "modify";break;
        case 2 : value = "secession";break;
        case 3: value = "counsel";break;
        case 4: value = "logout";break;
    }
    document.getElementById("setUrl").value=value;
    setForm.submit();
}

