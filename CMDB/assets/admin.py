from django.contrib import admin
from assets import asset_handler
from .models import (
    Asset,
    Server,
    SecurityDevice,
    StorageDevice,
    NetworkDevice,
    Software,
    IDC,
    Manufacturer,
    BusinessUnit,
    Contract,
    Tag,
    CPU,
    RAM,
    Disk,
    NIC,
    EventLog,
    NewAssetApprovalZone
)


class NewAssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'sn', 'model', 'manufacturer', 'c_time', 'm_time']
    list_filter = ['asset_type', 'manufacturer', 'c_time']
    search_fields = ('sn', )

    actions = ['approve_selected_new_assets']

    def approve_selected_new_assets(self, request, queryset):
        # 获得被打钩的checkbox对应的资产
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        success_upline_number = 0
        for asset_id in selected:
            obj = asset_handler.ApproveAsset(request, asset_id)
            ret = obj.asset_upline()
            if ret:
                success_upline_number += 1
        # 顶部绿色提醒信息
        self.message_user(request, "成功批准  %s  条新资产上线！" % success_upline_number)
    approve_selected_new_assets.short_description = "批准选择的新资产"


class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', 'm_time']


admin.site.register(Asset, AssetAdmin)
admin.site.register(Server)
admin.site.register(SecurityDevice)
admin.site.register(StorageDevice)
admin.site.register(NetworkDevice)
admin.site.register(Software)
admin.site.register(IDC)
admin.site.register(Manufacturer)
admin.site.register(BusinessUnit)
admin.site.register(Contract)
admin.site.register(Tag)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Disk)
admin.site.register(NIC)
admin.site.register(EventLog)
admin.site.register(NewAssetApprovalZone, NewAssetAdmin)
