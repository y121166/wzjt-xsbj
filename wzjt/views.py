from django.shortcuts import render
from rbac.models import VehicleInfo, UserInfo, Department
from django.http import JsonResponse
from wzjt.wz_pack import vehicle
from wzjt.wz_pack import detail
from django.http import HttpResponse


# Create your views here.
# 首页信息
def index(request):
    return render(request, 'wzjt/index.html')


# 返回车辆列表
def car_list(request):
    return render(request, 'wzjt/vehicle_table.html')


# ajax初始化车辆列表
def return_car_list(request):
    car_list = vehicle.get_cx_tj(request)
    return JsonResponse(car_list, safe=False, json_dumps_params={'ensure_ascii': False})


# ajax添加车辆
def add_vehicle(request):
    response_data = vehicle.add_vehicle(request)
    return JsonResponse(response_data, safe=False)


# ajax获取车辆详细信息
def vehicle_info(request, nid):
    response_data = {}
    try:
        vehicle_list = list(VehicleInfo.objects.filter(id=nid).values('id', 'vin', 'six_yards',
                                                                      'vehicle_type',
                                                                      'guidance_price', 'status',
                                                                      'storage_date', 'department', 'out_date',
                                                                      'remarks'))
        response_data['vehicledata'] = vehicle_list
        response_data['result'] = 'true'
    except Exception as e:
        response_data['result'] = 'false'
        response_data['message'] = '数据获取失败，请重试！'
        print(e)
    # print(response_data)
    return JsonResponse(response_data, safe=False)


# ajax修改车辆详细信息
def edit_vehicle(request):
    response_data = vehicle.edit_vehicle(request)
    return JsonResponse(response_data, safe=False)


# ajax删除车辆详细信息
def del_vehicle(request):
    response_data = vehicle.del_vehicle(request)
    return JsonResponse(response_data, safe=False)


# ajax获取车辆vin
def get_vehicle_vin(request):
    response_data = vehicle.get_vehicel_vin(request)
    return JsonResponse(response_data, safe=False)


# 订单添加列表
def detail_page(request):
    return render(request, 'wzjt/xsdetail_add_table.html')


# 订单审批列表
def detail_audit_page(request):
    return render(request, 'wzjt/xsdetail_audit_table.html')


# 订单结算列表
def detail_settlement_page(request):
    return render(request, 'wzjt/xsdetail_settlement_table.html')


# ajax初始化车辆列表
def return_detail_list(request):
    detail_list = detail.get_cx_tj(request)
    return JsonResponse(detail_list, safe=False, json_dumps_params={'ensure_ascii': False})


# ajax添加订单
def add_detail(request):
    response_data = detail.add_detail(request)
    return JsonResponse(response_data, safe=False)


# ajax获取订单详细信息
def info_detail(request, nid):
    response_data = detail.info_detail(request, nid)
    #return HttpResponse(response_data, content_type="application/json")
    return JsonResponse(response_data, safe=False)


# ajax修改订单详细信息
def edit_detail(request):
    response_data = detail.edit_detail(request)
    return JsonResponse(response_data, safe=False)


# 撤回订单
def withdraw_detail(request):
    response_data = detail.withdraw_detail(request)
    return JsonResponse(response_data, safe=False)


# 废弃订单
def del_detail(request):
    response_data = detail.del_detail(request)
    return JsonResponse(response_data, safe=False)


# 审核订单
def audit_detail(request):
    response_data = detail.audit_detail(request)
    return JsonResponse(response_data, safe=False)


def settlement_detail(request):
    response_data = detail.settlement_detail(request)
    return JsonResponse(response_data, safe=False)

