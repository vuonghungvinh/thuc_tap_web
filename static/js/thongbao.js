// $(window).scroll(function(){
//         // n?u  thanh cu?n >150px thì hi?n thanh di?u hu?ng ?n thanh top
//         if($(this).scrollTop()>150){  
//         $("#top1").show();
//         }else if($("#top2").css("display") != "none"){
//             $("#top1").hide();
//         }
//     })


// $(window).scroll(function(){
//         // n?u  thanh cu?n >150px thì hi?n thanh di?u hu?ng ?n thanh top
//         if($(this).scrollTop()>200){  
//         $(".listbox").css({'position':'fixed','width':'26.9%','top':'1px','height':'370px'});
//         $(".listbox2").show();
//         $(".listbox2").css({'position':'fixed','width':'26.9%','top':'400px'});
//           if($(".listbox").css("display") == "none"){
//             $(".listbox2").hide();
//           }
//           }
//         else{
//           $(".listbox").css({'position':'relative','width':'100%','height':'400px'});
//           $(".listbox2").hide();
//         }
//     })





$(window).scroll(function(){
        console.log($('#footer').position());
        if($(this).scrollTop()>350){  
        $(".listbox").css({'position':'fixed','width':'26.9%','top':'52px','height':'370px'});
     
        $(".listbox2").css({'position':'fixed','width':'26.9%','top':'452px'});
          if($(".listbox").css("display") == "none"){
            $(".listbox2").hide();
          }
          else{
               $(".listbox2").show();

          }
          }
        else{
          $(".listbox").css({'position':'relative','width':'100%','height':'400px', 'top': '0px'});
          $(".listbox2").hide();
        }
      if($(this).scrollTop()>2100){
           $(".listbox2").hide();
        }
    })