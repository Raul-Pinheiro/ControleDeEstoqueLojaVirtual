
      google.charts.load('current', {'packages':['corechart'],'language':'pt'});

      function desenharPizza(){

          var tabela = new google.visualization.DataTable();
          tabela.addColumn('string','categorias');
          tabela.addColumn('number','valores');
          tabela.addRows([

              ['Celular',500],
              ['Capa de celular',100],
              ['Pelicula',1000],
             
          ]);

          var opcoes= {
              'title':'Produtos mais vendidos',                            
              'pieHole':0.4,
              'legend':'right',
              'pieSliceText':'label',
              'slices':{

                  0:{color:'#40E0D0'},
                  1:{color:'#4682B2'},
                  2:{color:'rgb(95,158,160)'}
                
              },
              backgroundColor:'rgb(177, 182, 184)',
              borderRadius:100
          }

          var grafico = new google.visualization.PieChart(document.getElementById('produto_mais_vendidos'));
          grafico.draw(tabela, opcoes);
        }

  google.charts.setOnLoadCallback(desenharPizza);






