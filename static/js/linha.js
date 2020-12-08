google.charts.load('current', {'packages':['corechart']});

function desenharLinha(){
var tabela2=new google.visualization.DataTable();

    tabela2.addColumn('string','Mes');
    tabela2.addColumn('number', 'Lucro Obtido');
    tabela2.addRows([
        ['Jan',500],
        ['Fev',200],
        ['Mar',1000],
        ['Abr',2500],
        ['Mai',700],
        ['Jun',260],
        ['Jul',260],
        ['Ago',260],
        ['Set',200],
        ['Out',2260],
        ['Nov',260],
        ['Dez',500]

    ]);

    var opcoes = {
    title: 'Análise de Lucratividade',
    
    vAxis: {
            format: 'currency', 
            gridlines: {count:3,color:'transparent'}
    },
    curveType: 'function',
    legend:'none',
    backgroundColor:'rgb(203, 208, 209)'
}

    var tipodeGrafico = new google.visualization.LineChart(document.querySelector('#linha'));
    tipodeGrafico.draw(tabela2,opcoes);
}


google.charts.setOnLoadCallback(desenharLinha);