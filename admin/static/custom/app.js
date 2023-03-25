$(document).ready(function(){

function _(param) {
    return document.getElementById(param)
}


async function CheckClientAppointment(el){
    let str =  "";
    str += el;
    console.log(str);
}



async function calculateLaborandbills(el) {
    let unit_price = _('id_unity_price_0').value;
    let target_val =  el.target.value;

    let res =  parseFloat(target_val) * parseFloat(unit_price);
    _('id_amount_0').value = res;

}

_('id_qty').addEventListener('keyup', calculateLaborandbills, true)
  
    // inside jquery
})
