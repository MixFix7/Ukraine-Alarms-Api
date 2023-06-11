from django.db import models

class UkraineAlarmsStatus(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    Вінницька = models.BooleanField(default=False)
    Волинська = models.BooleanField(default=False)
    Дніпропетровська = models.BooleanField(default=False)
    Донецька = models.BooleanField(default=False)
    Житомирська = models.BooleanField(default=False)
    Закарпатська = models.BooleanField(default=False)
    Запорізька = models.BooleanField(default=False)
    Івано_Франківська = models.BooleanField(default=False)
    Київська = models.BooleanField(default=False)
    Кіровоградська = models.BooleanField(default=False)
    Луганська = models.BooleanField(default=False)
    Львівська = models.BooleanField(default=False)
    Миколаївська = models.BooleanField(default=False)
    Одеська = models.BooleanField(default=False)
    Полтавська = models.BooleanField(default=False)
    Рівненська = models.BooleanField(default=False)
    Сумська = models.BooleanField(default=False)
    Тернопільська = models.BooleanField(default=False)
    Харківська = models.BooleanField(default=False)
    Херсонська = models.BooleanField(default=False)
    Хмельницька = models.BooleanField(default=False)
    Черкаська = models.BooleanField(default=False)
    Чернігівська = models.BooleanField(default=False)
    Чернівецька = models.BooleanField(default=False)
    Автономна_Республіка_Крим = models.BooleanField(default=False)

    def __str__(self):
        return f"Status of alarms in Ukraine on {self.datetime}"
