$(window).scroll(function(){
        // n?u  thanh cu?n >150px thì hi?n thanh di?u hu?ng ?n thanh top
        if($(this).scrollTop()>100){  
        $("#header").css({'position':'fixed','top':'0px'});
     
        //$(".listbox2").css({'position':'fixed','width':'26.9%','top':'400px'});
          // if($(".listbox").css("display") == "none"){
          //   $(".listbox2").hide();
          // }
          // else{
          //      $(".listbox2").show();

          // }
          }
        else{
          $("#header").css({'position':'relative'});
         // $(".listbox2").hide();
        }
      //if($(this).scrollTop()>1700){
        //   $(".listbox2").hide();
        //}
    })