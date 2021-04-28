from django.test import TestCase
from datetime import datetime
from .models import Client,Clientcar,Profession,CreateBrigade,Worker,Brigade,Char_repaircar,Details,Accountingwork,Listwork,Zakazdetails

class ClientTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client.objects.create(name='Витя', surname='Батьков', patronomic='Витальевич', phone='+79825188990')

    def test_client(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя')
        expected_object_surname = client.surname
        self.assertEquals(expected_object_surname, 'Батьков')
        max_length = client._meta.get_field('patronomic').max_length
        self.assertEquals(max_length, 255)

class ClientcarTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client.objects.create(name='Витя', surname='Батьков', patronomic='Витальевич', phone='+79825188990')
        cls.k2 = Clientcar.objects.create(id_client=cls.client, car_brand='BMWX5', car_type='Легковая', regist_num=89843841, police=True)

    def test_carclient(self):
        clientcar = Clientcar.objects.get(id=1)
        field_label = clientcar._meta.get_field('car_brand').verbose_name
        self.assertEquals(field_label, 'Бренд автомобиля')
        expected_object_surname = clientcar.car_brand
        self.assertEquals(expected_object_surname, 'BMWX5')
        max_length = clientcar._meta.get_field('car_type').max_length
        self.assertEquals(max_length, 255)

    def tearDown(self):
        self.k2.delete()

class ProfessionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.p1 = Profession.objects.create(name_prof='Слесарь')

    def test_prof(self):
        prof = Profession.objects.get(id=1)
        field_label = prof._meta.get_field('name_prof').verbose_name
        self.assertEquals(field_label, 'Название профессии')
        max_length = prof._meta.get_field('name_prof').max_length
        self.assertEquals(max_length, 255)

    def tearDown(self):
        self.p1.delete()

class WorkerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.p1 = Profession.objects.create(name_prof='Слесарь')
        cls.w1 = Worker.objects.create(name='Витя', surname='Батьков', patronomic='Витальевич', pass_num=506743, pass_ser=3214, phone='+79825188990', id_prof=cls.p1)

    def test_worker(self):
        worker = Worker.objects.get(id=1)
        field_label = worker._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя')
        expected_object_surname = worker.surname
        self.assertEquals(expected_object_surname, 'Батьков')
        max_length = worker._meta.get_field('patronomic').max_length
        self.assertEquals(max_length, 255)

    def tearDown(self):
        self.w1.delete()

class CreateBrigadeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cr1 = CreateBrigade.objects.create(num_brigade=11111)

    def test_createbr(self):
        createbr = CreateBrigade.objects.get(id=1)
        field_label = createbr._meta.get_field('num_brigade').verbose_name
        self.assertEquals(field_label, 'Номер бригады')

    def tearDown(self):
        self.cr1.delete()

class BrigadeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.p1 = Profession.objects.create(name_prof='Слесарь')
        cls.w1 = Worker.objects.create(name='Витя', surname='Батьков', patronomic='Витальевич', pass_num=506743, pass_ser=3214, phone='+79825188990', id_prof=cls.p1)
        cls.cr1 = CreateBrigade.objects.create(num_brigade=11111)
        cls.br=Brigade.objects.create(id_worker=cls.w1,id_brigade=cls.cr1)

    def test_br(self):
        br = Brigade.objects.get(id=1)
        field_label = br._meta.get_field('id_worker').verbose_name
        self.assertEquals(field_label, 'Имя рабочего')

    def tearDown(self):
        self.br.delete()

class Char_repaircarTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.p1 = Profession.objects.create(name_prof='Слесарь')
        cls.w1 = Worker.objects.create(name='Витя', surname='Батьков', patronomic='Витальевич', pass_num=506743,
                                       pass_ser=3214, phone='+79825188990', id_prof=cls.p1)
        cls.cr1 = CreateBrigade.objects.create(num_brigade=11111)
        cls.br = Brigade.objects.create(id_worker=cls.w1, id_brigade=cls.cr1)
        cls.client = Client.objects.create(name='Витя', surname='Батьков', patronomic='Витальевич',
                                           phone='+79825188990')
        cls.k2 = Clientcar.objects.create(id_client=cls.client, car_brand='BMWX5', car_type='Легковая',
                                          regist_num=89843841, police=True)
        cls.char = Char_repaircar.objects.create(id_brigade=cls.br, id_clientcar=cls.k2, datatime=datetime(2021, 1, 1, 1, 1, 1), description='OOOOOOOO daaaaaaa')

    def test_char(self):
        char = Char_repaircar.objects.get(id=1)
        field_label = char._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание работ')

class DetailsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.det = Details.objects.create(name_model='OOO may', count=3, cost=100000000, stock_availability=False, stock_onzakaz=True)

    def test_det(self):
        det = Details.objects.get(id=1)
        field_label = det._meta.get_field('name_model').verbose_name
        self.assertEquals(field_label, 'Название детали')
        expected_object_surname = det.name_model
        self.assertEquals(expected_object_surname, 'OOO may')
        max_length = det._meta.get_field('name_model').max_length
        self.assertEquals(max_length, 255)

class ListworkTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.list = Listwork.objects.create(name_listwork='Ti kto takou davay dosvidania', cost_listwork=300000)

    def test_list(self):
        list = Listwork.objects.get(id=1)
        field_label = list._meta.get_field('name_listwork').verbose_name
        self.assertEquals(field_label, 'Название услуги')
        expected_object_surname = list.name_listwork
        self.assertEquals(expected_object_surname, 'Ti kto takou davay dosvidania')
        max_length = list._meta.get_field('name_listwork').max_length
        self.assertEquals(max_length, 255)

class AccountingworkTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.det = Details.objects.create(name_model='OOO may', count=3, cost=100000000, stock_availability=False,stock_onzakaz=True)
        cls.list = Listwork.objects.create(name_listwork='Ti kto takou davay dosvidania', cost_listwork=300000)
        cls.client = Client.objects.create(name='Витя', surname='Батьков', patronomic='Витальевич', phone='+79825188990')
        cls.k2 = Clientcar.objects.create(id_client=cls.client, car_brand='BMWX5', car_type='Легковая', regist_num=89843841, police=True)
        cls.acc = Accountingwork.objects.create(id_clientcar=cls.k2, id_details=cls.det,id_listwork=cls.list,total_cost=322,description='YFYFYFYYFYFYFYFY')

    def test_acc(self):
        acc = Accountingwork.objects.get(id=1)
        field_label = acc._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание работ')
        max_length = acc._meta.get_field('description').max_length
        self.assertEquals(max_length, 255)

class ZakazdetailsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client.objects.create(name='Витя', surname='Батьков', patronomic='Витальевич',phone='+79825188990')
        cls.k2 = Clientcar.objects.create(id_client=cls.client, car_brand='BMWX5', car_type='Легковая',regist_num=89843841, police=True)
        cls.zakaz = Zakazdetails.objects.create(model='OOO may', count=3, cost_det=100000000,total_zak=321321, stock_zakaz=False, id_clientcar=cls.k2)

    def test_zakaz(self):
        zakaz = Zakazdetails.objects.get(id=1)
        field_label = zakaz._meta.get_field('model').verbose_name
        self.assertEquals(field_label, 'Название детали')
        expected_object_surname = zakaz.model
        self.assertEquals(expected_object_surname, 'OOO may')
        max_length = zakaz._meta.get_field('model').max_length
        self.assertEquals(max_length, 255)