// Alert, Settings, Menu popups.
$(document).ready(function(){
  $(".alert").mouseover(function() {
    $(this).css("background", "url('/static/images/alerthover.png')");
  })

  $(".alert").mouseout(function() {
    $(this).css("background", "url('/static/images/alert.png')");
  })

  $(".settings").mouseover(function() {
    $(this).css("background", "url('/static/images/settingshover.png')");
  })

  $(".settings").mouseout(function() {
    $(this).css("background", "url('/static/images/settings.png')");
  })

  $(".menu").mouseover(function() {
    $(this).css("background", "url('/static/images/menuhover.png')");
  })

  $(".menu").mouseout(function() {
    $(this).css("background", "url('/static/images/menu.png')");
  })
})
