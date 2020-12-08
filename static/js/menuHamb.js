let icone=document.querySelector('.hamburguer_icon');
let menu=document.querySelector('.nav_menu_click');
let logo=document.querySelector('.header_logo_h1');
let exit=document.querySelector('.exit_icon');
let body=document.querySelector('.main');
let header=document.querySelector('.headerCliente');



icone.addEventListener('click',function(){   
    
    //remove icone hamb
    icone.style.display="none";
    //Some logo do header
    logo.style.display="none";
    //Faz aparecer a lista do menu    
    menu.style.display="flex";
    //Escurece body
   
    //Aparece icone de sair
    exit.style.display="block"; 

});

exit.addEventListener('click',function(){

 
    //some o Exit
    exit.style.display="none";
    //volta icone hamb
    icone.style.display="block";
    //volta logo do header
    logo.style.display="block";
    //Faz aparecer a lista do menu   
    menu.style.display="none";
    //Clareia body
      
   
});

body.addEventListener('mouseover',function(){

 
    //some o Exit
    exit.style.display="none";
    //volta icone hamb
    icone.style.display="block";
    //volta logo do header
    logo.style.display="block";
    //Faz aparecer a lista do menu   
    menu.style.display="none";
    //Clareia body
      
   
});



