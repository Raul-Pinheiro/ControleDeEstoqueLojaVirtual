google.charts.load('current', {'packages':['corechart'],'language':'pt'});

      function desenharPizza3(){

          var tabela = new google.visualization.DataTable();
          tabela.addColumn('string','categorias');
          tabela.addColumn('number','valores');
          tabela.addRows([

              ['Despesa Atual',15000],
              ['Receita Atual',45000],
              ['Lucro Atual',30000]
           
          ]);

          var opcoes= {
              'title':'Saldo Atual',                          
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

          var grafico = new google.visualization.PieChart(document.getElementById('mesAtual'));
          grafico.draw(tabela, opcoes);
        }

  google.charts.setOnLoadCallback(desenharPizza3);
