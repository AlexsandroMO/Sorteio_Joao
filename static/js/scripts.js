$( document ).ready(function() {

    var baseUrl   = 'http://localhost:8000/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter     = $('#filter');
    
    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if(result) {
            window.location.href = delLink;
        }

    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(filter).change(function() {
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });

});

// function PermissionDelite(){
//     console.log('entrou!!')
//     alert('entrou')
// }

//checar Options deletar coluna
var select = document.getElementById("options");
var divEscondida = document.getElementById("ride-div");

select.onchange = function() {
  if (select.value === "S") {
    divEscondida.style.display = "block";
  } else {
    divEscondida.style.display = "none";
  }
}


//Checar checkbox
let lotoM = document.getElementById("customSwitch1");
let mega = document.getElementById("customSwitch2");
let lotoF = document.getElementById("customSwitch3");
let milhoDupla = document.getElementById("customSwitch4");
let quinTime = document.getElementById("customSwitch5");
let dia = document.getElementById("customSwitch6");

let read = document.getElementById("read_check").textContent

if (read == 'lotom') {
    lotoM.checked = true;
}

if (read == 'mega') {
    mega.checked = true;
}

if (read == 'lotof') {
    lotoF.checked = true;
}

if (read == 'milho-dupla') {
    milhoDupla.checked = true;
}

if (read == 'quin-time') {
    quinTime.checked = true;
}

if (read == 'dia') {
   dia.checked = true;
}