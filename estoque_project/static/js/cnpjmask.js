var cnpj=document.querySelector('#cnpj');

cnpj.addEventListener('keyup',function(){
    
    if(cnpj.value.length==2 || cnpj.value.length==6){
        return cnpj.value+='.';
    }else if(cnpj.value.length==10){
        return cnpj.value+='/';
    }else if(cnpj.value.length==15){
        cnpj.value+='-';
    }else if(cnpj.value.length>=15){
        cnpj.value+='';
    }

});



