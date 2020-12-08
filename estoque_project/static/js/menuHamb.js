let abrir=document.querySelector('#open_hamb');
let menu=document.querySelector('.menu_dropdown');
let exit=document.querySelector('#close_hamb');
let body=document.querySelector('.main');
let header=document.querySelector('.headerCliente');



abrir.addEventListener('click',function(){   

    menu.style.display='block';

});

exit.addEventListener('click',function(){

    menu.style.display='none';
 
      
   
});

body.addEventListener('mouseover',function(){ 
    
    menu.style.display='none';
   
});



