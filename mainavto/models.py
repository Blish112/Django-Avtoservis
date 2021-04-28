from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    patronomic = models.CharField(max_length=255, verbose_name='Отчество')
    phone = PhoneNumberField(verbose_name='Номер телефона')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Clientcar(models.Model):
    id_client = models.ForeignKey('Client', verbose_name='Имя клиента', on_delete=models.DO_NOTHING, null=True)
    car_brand = models.CharField(max_length=255, verbose_name='Бренд автомобиля')
    car_type = models.CharField(max_length=255, verbose_name='Тип автомобиля')
    regist_num = models.IntegerField(max_length=9, verbose_name='Регистрационный номер')
    police = models.BooleanField(verbose_name='Учёт в полиции')

    def __str__(self):
        return self.car_brand

    class Meta:
        verbose_name = 'Автомобиль клиента'
        verbose_name_plural = 'Автомобили клиентов'


class Profession(models.Model):
    name_prof = models.CharField(max_length=255, verbose_name='Название профессии')

    def __str__(self):
        return self.name_prof

    class Meta:
        verbose_name = 'Профессии рабочих'
        verbose_name_plural = 'Профессии рабочих'


class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    patronomic = models.CharField(max_length=255, verbose_name='Отчество')
    pass_num = models.IntegerField(max_length=6, verbose_name='Номер пасспорта')
    pass_ser = models.IntegerField(max_length=4, verbose_name='Серия пасспорта')
    phone = PhoneNumberField(verbose_name='Номер телефона')
    id_prof = models.ForeignKey('Profession', verbose_name='Название профессии', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'

    def __str__(self):
        return self.name


class CreateBrigade(models.Model):
    num_brigade = models.IntegerField(max_length=6, verbose_name='Номер бригады')

    def __str__(self):
        return str(self.num_brigade)

    class Meta:
        verbose_name = 'Создание номера бригады'
        verbose_name_plural = 'Создание номера бригады'


class Brigade(models.Model):
    id_worker = models.ForeignKey('Worker', verbose_name='Имя рабочего', on_delete=models.DO_NOTHING)
    id_brigade = models.ForeignKey('CreateBrigade', verbose_name='Номер бригады', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.id_brigade)

    class Meta:
        verbose_name = 'Бригада'
        verbose_name_plural = 'Бригады'


class List_equpment(models.Model):
    name_eq = models.CharField(max_length=255, verbose_name='Название оборудования')
    count = models.IntegerField(verbose_name='Количество')
    guarantee = models.BooleanField(verbose_name='Гарантия')

    class Meta:
        verbose_name = 'Список оборудования'
        verbose_name_plural = 'Список оборудования'


class Char_repaircar(models.Model):
    id_brigade = models.ForeignKey('Brigade', verbose_name='Номер бригады', on_delete=models.DO_NOTHING)
    id_clientcar = models.ForeignKey('Clientcar', verbose_name='Автомобиль клиента', on_delete=models.DO_NOTHING)
    datatime = models.DateTimeField(auto_now_add=True, verbose_name='Время работы', null=True)
    description = models.CharField(max_length=255, verbose_name='Описание работ')

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'График работ'


class Details(models.Model):
    name_model = models.CharField(max_length=255, verbose_name='Название детали')
    count = models.IntegerField(verbose_name='Количество')
    cost = models.IntegerField(verbose_name='Цена')
    stock_availability = models.BooleanField(verbose_name='Наличие на складе')
    stock_onzakaz = models.BooleanField(verbose_name='Нуждаеться в заказе', null=True)

    def __str__(self):
        return self.name_model

    class Meta:
        verbose_name = 'Детали'
        verbose_name_plural = 'Детали'


class Accountingwork(models.Model):
    id_clientcar = models.ForeignKey('Clientcar', verbose_name='Автомобиль клиента', on_delete=models.DO_NOTHING)
    id_details = models.ForeignKey('Details', verbose_name='Деталь', on_delete=models.DO_NOTHING, null=True)
    id_listwork = models.ForeignKey('Listwork', verbose_name='Название услуги', on_delete=models.DO_NOTHING, null=True)
    total_cost = models.IntegerField(verbose_name='Итоговая цена', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Описание работ')

    def save(self, *args, **kwargs):
        self.total_cost = self.id_listwork.cost_listwork + self.id_details.cost
        super().save()

    class Meta:
        verbose_name = 'Учет работ'
        verbose_name_plural = 'Учет работ'


class Listwork(models.Model):
    name_listwork = models.CharField(max_length=255, verbose_name='Название услуги')
    cost_listwork = models.IntegerField(verbose_name='Цена услуги', null=True)

    def __str__(self):
        return self.name_listwork

    class Meta:
        verbose_name = 'Лист услуг'
        verbose_name_plural = 'Предоставляемые услуги'


class Zakazdetails(models.Model):
    model = models.CharField(max_length=255, verbose_name='Название детали')
    count = models.IntegerField(verbose_name='Количество')
    cost_det = models.IntegerField(verbose_name='Цена')
    total_zak = models.IntegerField(verbose_name='Итоговая цена закупку', null=True, blank=True)
    stock_zakaz = models.BooleanField(verbose_name='Привезли на склад', null=True)
    id_clientcar = models.ForeignKey('Clientcar', verbose_name='Автомобиль клиента', on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        self.total_zak = self.count * self.cost_det
        super().save()

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Заказ деталей'
        verbose_name_plural = 'Заказ деталей'