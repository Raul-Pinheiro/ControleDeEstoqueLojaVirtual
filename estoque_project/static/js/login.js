
var button= document.querySelector('#acesso');
var button2= document.querySelector('#acesso2');
var login= document.querySelector('#login');
var senha= document.querySelector('#senha');
var href= "painel.html";


button.addEventListener('click',function(){

    if(login.value =="raulmatheus.rm@gmail.com" & senha.value=="1234"){

        button.setAttribute('href',href);

    }else{
        document.querySelector('#aviso').style.display="block";
    }
});

button2.addEventListener('click',function(){

    if(login.value =="raulmatheus.rm@gmail.com" & senha.value=="1234"){

        button.setAttribute('href',href);

    }else{
        document.querySelector('#aviso').style.display="block";
    }
});