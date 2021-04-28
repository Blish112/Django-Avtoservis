from django.contrib import admin
from . import models

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronomic', 'phone')

@admin.register(models.Clientcar)
class ClientcarAdmin(admin.ModelAdmin):
    list_display = ('id_client', 'car_brand', 'car_type', 'regist_num', 'police')

@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name_prof',)

@admin.register(models.CreateBrigade)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('num_brigade',)

@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronomic', 'pass_num', 'pass_ser', 'phone', 'id_prof')

@admin.register(models.Brigade)
class Brigade(admin.ModelAdmin):
    list_display = ('id_worker', 'id_brigade')

@admin.register(models.Char_repaircar)
class Char_repaircar(admin.ModelAdmin):
    list_display = ('id_brigade', 'id_clientcar', 'datatime', 'description')

@admin.register(models.Details)
class Details(admin.ModelAdmin):
    list_display = ('name_model', 'count','cost', 'stock_availability', 'stock_onzakaz')

@admin.register(models.Accountingwork)
class Accountingwork(admin.ModelAdmin):
    list_display = ('id_clientcar', 'id_details', 'id_listwork', 'total_cost', 'description')

@admin.register(models.Listwork)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name_listwork', 'cost_listwork')

@admin.register(models.Zakazdetails)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('model', 'count', 'cost_det', 'total_zak', 'stock_zakaz', 'id_clientcar')