(function () {
    let timeHoraIni1 = document.querySelector('#timeHoraIni1');
    let timeHoraFin1 = document.querySelector('#timeHoraFin1');
      
    let timeHoraIni2 = document.querySelector('#timeHoraIni2');
    let timeHoraFin2 = document.querySelector('#timeHoraFin2');

    let timeHoraIni3 = document.querySelector('#timeHoraIni3');
    let timeHoraFin3 = document.querySelector('#timeHoraFin3');

    let timeHoraIni4 = document.querySelector('#timeHoraIni4');
    let timeHoraFin4 = document.querySelector('#timeHoraFin4');

    let timeHoraIni5 = document.querySelector('#timeHoraIni5');
    let timeHoraFin5 = document.querySelector('#timeHoraFin5');

    let timeHoraIni6 = document.querySelector('#timeHoraIni6');
    let timeHoraFin6 = document.querySelector('#timeHoraFin6');

    let timeHoraIni7 = document.querySelector('#timeHoraIni7');
    let timeHoraFin7 = document.querySelector('#timeHoraFin7');


    let alerta = document.getElementById('alerta');

    const mostraralerta = () => {
        alerta.style.display="block";
    }

    window.addEventListener('click', (evt) => {
        if(timeHoraFin1.value<timeHoraIni1.value){
            timeHoraFin1.value = timeHoraIni1.value
            mostraralerta();
        }

        if(timeHoraFin2.value<timeHoraIni2.value){
            timeHoraFin2.value = timeHoraIni2.value
            mostraralerta();
        }

        if(timeHoraFin3.value<timeHoraIni3.value){
            timeHoraFin3.value = timeHoraIni3.value
            mostraralerta();
        }

        if(timeHoraFin4.value<timeHoraIni4.value){
            timeHoraFin4.value = timeHoraIni4.value
            mostraralerta();
        }


        if(timeHoraFin5.value<timeHoraIni5.value){
            timeHoraFin5.value = timeHoraIni5.value
            mostraralerta();
        }

        if(timeHoraFin6.value<timeHoraIni6.value){
            timeHoraFin6.value = timeHoraIni6.value
            mostraralerta();
        }


        if(timeHoraFin7.value<timeHoraIni7.value){
            timeHoraFin7.value = timeHoraIni7.value
            mostraralerta();
        }

      });

    
})();