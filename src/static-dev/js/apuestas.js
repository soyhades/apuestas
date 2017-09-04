function open_modal_register(){
  $('#modal_register').modal('show');
}
function cancel_modal_register(){
  $('#modal_register').find('#id_username').val('');
  $('#modal_register').find('#id_password1').val('');
  $('#modal_register').find('#id_password2').val('');
$('#modal_register').modal('hide');
}
