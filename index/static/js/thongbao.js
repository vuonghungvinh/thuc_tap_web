// $(window).scroll(function(){
//         // n?u  thanh cu?n >150px thì hi?n thanh di?u hu?ng ?n thanh top
//         if($(this).scrollTop()>150){  
//         $("#top1").show();
//         }else if($("#top2").css("display") != "none"){
//             $("#top1").hide();
//         }
//     })


$(window).scroll(function(){
        // n?u  thanh cu?n >150px thì hi?n thanh di?u hu?ng ?n thanh top
        if($(this).scrollTop()>200){  
        $(".listbox").css({'position':'fixed','width':'26.9%','top':'1px','height':'370px'});
        $(".listbox2").show();
        $(".listbox2").css({'position':'fixed','width':'26.9%','top':'400px'});
          if($(".listbox").css("display") == "none"){
            $(".listbox2").hide();
          }
          }
        else{
          $(".listbox").css({'position':'relative','width':'100%','height':'400px'});
          $(".listbox2").hide();
        }
    })





 