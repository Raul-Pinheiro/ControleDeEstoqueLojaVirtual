
var input = document.querySelector('.input_type');


input.addEventListener('input', function(event){

    event.preventDefault();
    var produto = document.querySelectorAll('.tbody_line');
    var colunas = document.querySelectorAll('.tbody_column');

    var expressao= new RegExp(input.value, "i");
    produto.forEach(colunas => {
        if(!expressao.test(colunas)){
            console.log('Funcionou');
            
           
            
        }else{        
            console.log('Deu errado');
            produto.style.display="none";
        }
    });


});

//input.addEventListener('input', function(event){
    //event.preventDefault();
//produto.forEach(function(coluna){

        //var info= coluna.querySelectorAll('.tbody_column');
       // var expressao= new RegExp(input.value, "i");


        //var dado=info.textContent;

        
        //if(input.value==0){
         //   return produto.classList.remove("invisivel");
        //}
        //if(expressao.test(dado) ){
        //    return produto.textContent;  
       // }else{
        //    produto.classList.add("invisivel");
       // }
  //  });

//});




