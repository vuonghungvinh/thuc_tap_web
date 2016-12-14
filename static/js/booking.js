var total = 0;
var total_person = 0;
var adults=0;
function changeperson(){
	adults = parseInt($("input[name='adult_booking']").val());
	var children = parseInt($("input[name='child_booking']").val());
	var total_slot = parseInt($("input[name='slot']").val());
	total = 0;
	total_person = 0;
	$(".listcustomer tbody").empty();
	if (!isNaN(adults))
	{
		renderlistcustomer(adults, true);
		total_person+=adults;
	}
	if (!isNaN(children)){
		renderlistcustomer(children, false);
		total_person+=children;
	}
	$('input[name="total_customer"]').val(total_person);
	if (total>0){
		$('.datepicker').datepicker({
			format: 'yyyy-mm-dd',
			todayHighlight: true,
			maxDate: '0'
		});
		rendertotal();
	}
}

function renderlistcustomer(n, is_adult)
{
	for (var i=0; i<n; i++){
		$('.listcustomer tbody').append('\
				<tr>\
	                <td><input data-val="true" class="form-control" data-val-required="*" name="name"  type="text" value=""></td>\
	                <td><input type="text" readonly="true" name="date" class="form-control datepicker" placeholder="Ngày Sinh"></td>\
	                <td><select name="gender" class="form-control" name="gender"><option value="0">Nữ</option><option value="1">Nam</option></select></td>\
	                <td><input class="form-control" name="address" type="text" value=""></td>\
	                <td>\
	                	<input type="hidden" name="personkind" value="'+ (is_adult?"1":"0") +'">\
	                	<input class="form-control" type="text" readonly="true" value="'+ (is_adult?"Người lớn":"Trẻ em") +'" />\
	                </td>\
	                <td class="price right" ><input class="form-control" readonly="true" id="price" name="price" type="text" value="'+ sum(is_adult) +'"></td>\
				</tr>\
			');
		// $('.listcustomer tbody').append('\
		// 	<tr>\                  
  //           </tr>\
		// ');
	}
}

function rendertotal(){
	$('.listcustomer tbody').append('\
				<tr>\
	                <td colspan="4"></td>\
                    <td><strong>Tổng cộng</strong></td>\
                    <td class="price right"><input value="'+ total +'" class="form-control" type="text" id="TotalPrice" disabled="disabled" ></td>\
				</tr>\
			');
}

function sum(is_adult){
	var cost = parseFloat($("input[name='cost']").val());
	var cost_sale = parseFloat($("input[name='cost_sale']").val());
	var is_sale = $("input[name='is_sale']").val();
	var percent = parseFloat($("input[name='percent']").val());
	if (is_sale == 'True'){
		cost = cost_sale;
	}
	if (!is_adult){
		total+=cost*percent/100;
		return cost*percent/100;
	}
	total+=cost;
	return cost;
}

$(document).ready(function(){
	$("#btnbooking").click(function(){
		if (total_person > parseInt($("input[name='slot']").val()))
		{
			$.notify("Quá số người cho phép", "error");
			return '';
		}
		if (adults <= 0 || isNaN(adults)){
			$.notify("Phải có ít nhất 1 người lớn", "warn");
			return '';
		}
		var arr = [];
		var isbreak = false;
		$(".listcustomer tbody tr").each(function(){
			if ($(this).find("td").length==6){
				var i=0;
				var ob = {};
				var tds = $(this).find("td").each(function(){
					if(i != 2 && (typeof($(this).find("input").val()) == 'undefined' || $(this).find("input").val().length <= 0)){
						if (!isbreak){
							$.notify("Vui lòng nhập tất cả các field", "warn");
						}
						isbreak = true;
						return '';
					}
					if (i==0){
						ob['name'] = $(this).find("input").val();
					}
					if (i==1){
						ob['date'] = $(this).find("input").val();
					}
					if (i==2){
						ob['gender'] = $(this).find("select").val();
					}
					if (i==3){
						ob['address'] = $(this).find("input").val();
					}
					if (i==4){
						ob['type_customer'] = $(this).find("input").val();
					}
					if (i==5){
						ob['cost'] = $(this).find("input").val();
					}
					i++;
				});
				if (isbreak)
					return '';
				arr.push(ob);
			}
		});
		if (isbreak)
			return '';
		info = {};
		info['tour'] = $("input[name='id']").val();
		info['name'] = $("input[name='name_booking']").val();
		info['email'] = $("input[name='email_booking']").val();
		info['address'] = $("input[name='add_booking']").val();
		info['phone'] = $("input[name='phone_booking']").val();
		info['note'] = $("input[name='note_booking']").val();
		info['adult'] = $("input[name='adult_booking']").val();
		info['children'] = $("input[name='child_booking']").val();
		info['total'] = total;
		$.ajax({    
	        type: "POST",
	        url: '/booking/save/',
	        // data: JSON.stringify([{'info': info}, {'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()}, {'listcustomer': arr}]),
	        // data: {info: info, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), listcustomer: arr},
	        // data: {data: JSON.stringify({info: info, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), listcustomer: arr})},
	        data: JSON.stringify({'info': info, 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(), 'listcustomer': arr}),
	        // contentType: 'application/json',
	        dataType: 'json',
	        success: function(datas){
	        	if(datas['status']==0){
	        		$.notify(datas['data'], "error");
	        	} else {
	        		// $.notify(datas['data'], "success");
	        		window.location.href = '/booking/edit/'+datas['data'];
	        	}
	        }, 
	        error: function(datas){
	        	console.log(datas);     
	        }       
	    });
	});
	$("#editbooking a").click(function(){
		$.ajax({    
	        type: "POST",
	        url: '/booking/delete/'+$("#editbooking input[name='id']").val()+'/',
	        data: {type: $(this).val(), csrfmiddlewaretoken: $('.fabtransaction input[name=csrfmiddlewaretoken]').val()},
	        dataType: 'json',       
	        success: function(datas){
	        	window.location.href = '/booking/mybooking';
	        }, 
	        error: function(){
	        	$.notify("Xoa khong thanh cong", "error");      
	        }       
	    });
	});
});