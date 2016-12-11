var total = 0;
function changeperson(){
	var adults = parseInt($("input[name='adult_booking']").val());
	var children = parseInt($("input[name='child_booking']").val());
	var total_slot = parseInt($("input[name='slot']").val());
	total = 0;
	$(".listcustomer tbody").empty();
	if (!isNaN(adults))
	{

		renderlistcustomer(adults, true);
	}
	if (!isNaN(children)){
		renderlistcustomer(children, false);
	}
	if (total>0){
		rendertotal();
	}
}

function renderlistcustomer(n, is_adult)
{
	for (var i=0; i<n; i++){
		$('.listcustomer tbody').append('\
				<tr>\
	                <td><input data-val="true" class="form-control" data-val-required="*" name="name"  type="text" value=""></td>\
	                <td><input type="date" name="date" class="form-control" placeholder="Ngày Sinh"></td>\
	                <td><select name="gender" class="form-control" name="gender"><option value="0">Nữ</option><option value="1">Nam</option></select></td>\
	                <td><input class="form-control" name="address" type="text" value=""></td>\
	                <td>\
	                	<input type="hidden" name="personkind" value="'+ (is_adult?"1":"0") +'">\
	                	<input class="form-control" type="text" disabled="disabled" value="'+ (is_adult?"Người lớn":"Trẻ em") +'" />\
	                </td>\
	                <td class="price right" ><input class="form-control" disabled="disabled" id="price" name="price" type="text" value="'+ sum(is_adult) +'"></td>\
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
	if (is_sale){
		cost = cost-cost_sale;
	}
	if (!is_adult){
		total+=cost*percent/100;
		return cost*percent/100;
	}
	total+=cost;
	return cost;
}