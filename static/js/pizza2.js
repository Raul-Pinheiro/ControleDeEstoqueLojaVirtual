google.charts.load('current', {'packages':['corechart'],'language':'pt'});

      function desenharPizza2(){

          var tabela = new google.visualization.DataTable();
          tabela.addColumn('string','categorias');
          tabela.addColumn('number','valores');
          tabela.addRows([

              ['Despesa Anterior',10000],
              ['Receita Anterior',60000],
              ['Lucro Anterior',90000]
           
          ]);

          var opcoes= {
              'title':'Saldo do Mês Anterior',                        
              'is3D':true,
              'legend':'right',
              'pieSliceText':'label',
              'slices':{

                0:{color:'#40E0D0'},
                1:{color:'#4682B2'},
                2:{color:'rgb(95,158,160)', offset:0.3}
              
            },
              backgroundColor:'rgb(177, 182, 184)'
          }

          var grafico = new google.visualization.PieChart(document.getElementById('mesAnterior'));
          grafico.draw(tabela, opcoes);
        }

  google.charts.setOnLoadCallback(desenharPizza2);






