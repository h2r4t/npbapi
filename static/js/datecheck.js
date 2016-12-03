// remove invalid dates
function dateCheck(){
  var y = $('#id_year').val();
  var m = $('#id_month').val();
  var d = $('#id_day').val();
  if(y && m){
    var ds = new Date(y, m, 0);
    var lastday = Number(ds.getDate());
    var option = '<option value="">--</option>';
    for(var i = 1; i <= lastday; i++){
      if(i == d){
        if(i < 10){
          option += '<option value="0' + i + '" selected>' + i + '日</option>';
        } else{
          option += '<option value="' + i + '" selected>' + i + '日</option>';
        }
      } else {
        if(i < 10){
          option += '<option value="0' + i + '">' + i + '日</option>';
        }else{
          option += '<option value="' + i + '">' + i + '日</option>';
        }
      }
    }
    $('#id_day').html(option);
  }
}

// show json & check if selected date is the past day
function buttonClick(){
  var warning = document.getElementById('warning');
  var y = $('#id_year').val();
  var m = $('#id_month').val();
  var d = $('#id_day').val();
  var t = new Date();
  var t_y = t.getFullYear();
  var t_m = t.getMonth() + 1;
  if(t_m < 10){
    t_m = "0" + t_m;
  }
  var t_d = t.getDate();
  if(t_d < 10){
    t_d = "0" + t_d;
  }
  var today = "" + t_y + t_m + t_d;
  var date = y + m + d;
  if (Number(today) > Number(date)) {
    warning.innerHTML = "";
    var val = 'http://127.0.0.1:8000/npbapi/score/' + date + '/';
    window.open(val);
  } else {
    warning.innerHTML = "今日より前の日付を選択してください。";
  }
}