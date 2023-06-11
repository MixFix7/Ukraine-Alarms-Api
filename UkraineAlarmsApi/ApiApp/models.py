from django.db import models

class UkraineAlarmsStatus(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    Вінницька = models.BooleanField()
    Волинська = models.BooleanField()
    Дніпропетровська = models.BooleanField()
    Донецька = models.BooleanField()
    Житомирська = models.BooleanField()
    Закарпатська = models.BooleanField()
    Запорізька = models.BooleanField()
    Івано_Франківська = models.BooleanField()
    Київська = models.BooleanField()
    Кіровоградська = models.BooleanField()
    Луганська = models.BooleanField()
    Львівська = models.BooleanField()
    Миколаївська = models.BooleanField()
    Одеська = models.BooleanField()
    Полтавська = models.BooleanField()
    Рівненська = models.BooleanField()
    Сумська = models.BooleanField()
    Тернопільська = models.BooleanField()
    Харківська = models.BooleanField()
    Херсонська = models.BooleanField()
    Хмельницька = models.BooleanField()
    Черкаська = models.BooleanField()
    Чернігівська = models.BooleanField()
    Чернівецька = models.BooleanField()
    Автономна_Республіка_Крим = models.BooleanField()

    def __str__(self):
        return f"Status of alarms in Ukraine on {self.datetime}"
