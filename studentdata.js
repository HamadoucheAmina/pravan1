loadData();

function actualiser(){
	location.reload();
}

function loadData(){
    httpRequest1 = new XMLHttpRequest();
    httpRequest1.open('GET', '/api/dataGenre');
    httpRequest1.onreadystatechange = function (){
        if (httpRequest1.readyState === 4 && httpRequest1.status === 200){
            jsonData = JSON.parse(httpRequest1.response);
            updatePie(jsonData);
        }
    };
    httpRequest1.send();
    
    httpRequest2 = new XMLHttpRequest();
    httpRequest2.open('GET', '/api/dataSpec');
    httpRequest2.onreadystatechange = function (){
        if (httpRequest2.readyState === 4 && httpRequest2.status === 200){
            jsonData = JSON.parse(httpRequest2.response);
            updateRadar(jsonData);
        }
    };
    httpRequest2.send();
    
    httpRequest3 = new XMLHttpRequest();
    httpRequest3.open('GET', '/api/dataAdmitted');
    httpRequest3.onreadystatechange = function (){
        if (httpRequest3.readyState === 4 && httpRequest3.status === 200){
            jsonData = JSON.parse(httpRequest3.response);
            updateGroupedBar_Admitted(jsonData);
        }
    };
    httpRequest3.send();

    httpRequest4 = new XMLHttpRequest();
    httpRequest4.open('GET', '/api/dataAVG');
    httpRequest4.onreadystatechange = function (){
        if (httpRequest4.readyState === 4 && httpRequest4.status === 200){
            jsonData = JSON.parse(httpRequest4.response);
            updateHorizontalBar(jsonData);
        }
    };
    httpRequest4.send();
    
    httpRequest5 = new XMLHttpRequest();
    httpRequest5.open('GET', '/api/dataDenied');
    httpRequest5.onreadystatechange = function (){
        if (httpRequest5.readyState === 4 && httpRequest5.status === 200){
            jsonData = JSON.parse(httpRequest5.response);
            updateGroupedBar_Denied(jsonData);
        }
    };
    httpRequest5.send();
    /*
    httpRequest6 = new XMLHttpRequest();
    httpRequest6.open('GET', '/api/dataSPECAVG');
    httpRequest6.onreadystatechange = function (){
        if (httpRequest6.readyState === 4 && httpRequest6.status === 200){
            jsonData = JSON.parse(httpRequest6.response);
            updateScatter19(jsonData);
        }
    };
    httpRequest6.send();
    */
    httpRequest7 = new XMLHttpRequest();
    httpRequest7.open('GET', '/api/dataMAXAVG');
    httpRequest7.onreadystatechange = function (){
        if (httpRequest7.readyState === 4 && httpRequest7.status === 200){
            jsonData = JSON.parse(httpRequest7.response);
            updateLines(jsonData);
        }
    };
    httpRequest7.send();
}

function updatePie(jsonData){

    var labels = jsonData.map(function(e) {
        return e.Genre;
    });
    
    var data = jsonData.map(function(e) {
        return e.Count;
    });

    new Chart(document.getElementById("genre_pie"), {
        type: 'pie',
		data: {
		  labels: labels,
		  datasets: [{
			label: "Nombre d'Etudiants",
			backgroundColor: ["#F4A259", "#160C28"],
			data: data
		  }]
		},
		options: {
		  responsive: false,
		  maintainAspectRatio: true,
		  title: {
			display: true,
			text: "Nombre Total d'Etudiants par Genre"
		  },
		  legend:{
			position:'right'
		  }
		}
    })
}
function updateRadar(jsonData){
    jsonData0 = jsonData[0];
    var labels = jsonData0.map(function(e){
        return e.Spec;
    });
    var data19 = jsonData0.map(function(e){
        return e.Count;
    });
    jsonData1 = jsonData[1];
    var data20 = jsonData1.map(function(e){
        return e.Count;
    });
    jsonData2 = jsonData[2];
    var data21 = jsonData2.map(function(e){
        return e.Count;
    });
    
    new Chart(document.getElementById("spec_radar"), {
        type: 'radar',
        data: {
          labels: labels,
          datasets: [
            {
                label: "2019",
                fill: true,
                backgroundColor: "rgba(255, 194, 39, 0.3)",
                borderColor: "#ffa600",
                pointBorderColor: "#ffa600",
                pointBackgroundColor: "#ffa600",
                pointBorderColor: "#fff",
                data: data19
            }, {
                label: "2020",
                fill: true,
                backgroundColor: "#1d597e6f",
                borderColor: "#1d597e",
                pointBackgroundColor: "#1d597e",
                pointBorderColor: "#fff",
                data: data20
            }, {
                label: "2021",
                fill: true,
                backgroundColor: "rgba(139, 0, 0, 0.573)",
                borderColor: "rgb(139, 0, 0)",
                pointBackgroundColor: "rgb(139, 0, 0)",
                pointBorderColor: "#fff",
                data: data21
              }
          ]
        },
		options: {
            responsive: false,
            maintainAspectRatio: true,
            title: {
              display: true,
              text: "Distribution des Étudiants par Spécialité"
            },
            legend:{
              position:'top'
            },
            scale: {
                ticks: {
                    beginAtZero: true,
                    suggestedMin: 0,
                    suggestedMax: 100
                }
            }
          }
    });
}
function updateGroupedBar_Admitted(jsonData){
    jsonData0 = jsonData[0];
    var labels = jsonData0.map(function(e){
        return e.Spec;
    });
    var data19 = jsonData0.map(function(e){
        return e.Count;
    });
    jsonData1 = jsonData[1];
    var data20 = jsonData1.map(function(e){
        return e.Count;
    });
    jsonData2 = jsonData[2];
    var data21 = jsonData2.map(function(e){
        return e.Count;
    });

    new Chart(document.getElementById("admitted_grouped_bar"), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: "2019",
                    backgroundColor: "#ffa600",
                    data: data19
                }, {
                    label: "2020",
                    backgroundColor: "#ca5a00",
                    data: data20
                }, {
                    label: "2021",
                    backgroundColor: "rgb(139, 0, 0)",
                    data: data21
                }
            ]
        },
        options: {
            responsive: false,
            maintainAspectRatio: true,
            title: {
              display: true,
              text: "Nombre d'Étudiants Admits par Année en fonction de la Specialité"
            },
            legend:{
              position:'top'
            },
            scale: {
                ticks: {
                    beginAtZero: true,
                    suggestedMax: 50
                }
            }
          }
    });
}
function updateHorizontalBar(jsonData){
    jsonData0 = jsonData[0];
    var dataF = jsonData0.map(function(e){
        return e.Moyenne;
    });
    jsonData1 = jsonData[1];
    var dataH = jsonData1.map(function(e){
        return e.Moyenne;
    });

    new Chart(document.getElementById("bar-chart-horizontal"), {
        type: 'horizontalBar',
        data: {
          labels: ["2019", "2020", "2021"],
          datasets: [
            {
                label: "Femmes",
                backgroundColor: "#1d597e",
                data: dataF
            }, {
                label: "Hommes",
                backgroundColor: "#ca5a00",
                data: dataH
            }
          ]
        },
        options: {
            responsive: false,
            maintainAspectRatio: true,
            title: {
              display: true,
              text: 'Moyenne Générale des Étudiants par Genre'
            },
            legend:{
              position:'top'
            }
          }
    });
}
function updateGroupedBar_Denied(jsonData){
    jsonData0 = jsonData[0];
    var labels = jsonData0.map(function(e){
        return e.Spec;
    });
    var data19 = jsonData0.map(function(e){
        return e.Count;
    });
    jsonData1 = jsonData[1];
    var data20 = jsonData1.map(function(e){
        return e.Count;
    });
    jsonData2 = jsonData[2];
    var data21 = jsonData2.map(function(e){
        return e.Count;
    });

    new Chart(document.getElementById("denied_grouped_bar"), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: "2019",
                    backgroundColor: "#1D2B53",
                    data: data19
                }, {
                    label: "2020",
                    backgroundColor: "#7E2553",
                    data: data20
                }, {
                    label: "2021",
                    backgroundColor: "#FF004D",
                    data: data21
                }
            ]
        },
        options: {
            responsive: false,
            maintainAspectRatio: true,
            title: {
              display: true,
              text: "Nombre d'Étudiants Ajournés par Année en fonction de la Specialité"
            },
            legend:{
              position:'top'
            },
            scale: {
                ticks: {
                    beginAtZero: true,
                    suggestedMax: 50
                }
            }
          }
    });
}
function updateLines(jsonData){

    jsonData0 = jsonData[0]; //femmes
    var dataF = jsonData0.map(function(e){
        return e.Moyenne;
    });
    jsonData1 = jsonData[1]; //hommes
    var dataH = jsonData1.map(function(e){
        return e.Moyenne;
    });

    new Chart(document.getElementById("line-chart"), {
        type: 'line',
        data: {
          labels: [2019,2020,2021],
          datasets: [{ 
              data: dataF,
              label: "Femme",
              borderColor: "#3e95cd",
              fill: false
            }, { 
              data: dataH,
              label: "Homme",
              borderColor: "#8e5ea2",
              fill: false
            }
          ]
        },
        options: {
          title: {
            display: true,
            text: 'Moyenne Maximale par Année suivant le Genre'
          }
        }
      });
}
/*
function updateScatter19(jsonData){
    jsonData0 = jsonData[0];
    var labels = jsonData0.map(function(e){
        return e.Spec;
    });
    var data19 = jsonData0.map(function(e){
        return e.Moyennes;
    });

    datasets = [];
    data = [];
    for (let i = 0; i < labels.length; i++) {
        for (let j = 0; j < data19[i].length; j++){
            data.push(labels[i]);
            data.push(data19[i][j]);
            datasets.push(data);
            data = [];
        }
    }
    
    var options = {
        series: [{
        name: "Étudiant",
        data: [
            ['SPECIALITE_2', 10.2], ['SPECIALITE_4', 15.8]]
      }],
        chart: {
        height: 350,
        type: 'scatter',
        zoom: {
          enabled: true,
          type: 'xy'
        }
      },
      xaxis: {
        type: 'category',
        categories: labels,
        tickAmount: 7
      },
      yaxis: {
        decimalsInFloat: 2,
        min: 4
      },
      axisBorder: {show: false}
      };

      var chart = new ApexCharts(document.querySelector("#avg_scatter"), options);
      chart.render();
}
*/