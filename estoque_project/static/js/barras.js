google.charts.load('current', {'packages':['corechart']});

function desenharColuna(){
var array=
[   
    ["Mês","Entrada","Saída"],
    ['Jan',500,600],
    ['Fev',200,600],
    ['Mar',1000,600],
    ['Abr',2500,650],
    ['Mai',700,650],
    ['Jun',260, 1000],
    ['Jul',260,650],
    ['Ago',260,650],
    ['Set',200,650],
    ['Out',2260,650],
    ['Nov',260,650],
    ['Dez',500,650]

    ];
var tabela=google.visualization.arrayToDataTable(array);


var opcoes= {
         title:'Entradas e Saídas do Mês',
         vAxis:{
             gridlines:{
                 color:'transparent'
             },
             format:'currency',
             title:'Valores'
         },
         hAxis:{
             title:'Mês'
         }
         

    
    
}


    var tipodeGrafico = new google.visualization.BarChart(document.querySelector('#grafico_coluna'));
    tipodeGrafico.draw(tabela,opcoes);
};


google.charts.setOnLoadCallback(desenharColuna);