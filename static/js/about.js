function check(){
  if(window.confirm('送信してよろしいですか？')){
    var frm = document.getElementsByName('mailform')[0];
    frm.submit();
  }
  else{
    window.alert('キャンセルされました');
    return false;
  }
}