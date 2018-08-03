from django.db import models

class data_jobs(models.Model):
    # location — место работы
    # contract_type — тип контракта
    # contract_time — тип занятости
    # title — наименование вакансии
    # description — описание вакансии
    # company — наименование компании
    # service — наименование сайта, откуда вакансия

    location = models.CharField(max_length=500, default='None')
    contract_type = models.CharField(max_length=500, default='None')
    contract_time = models.CharField(max_length=500, default='None')
    title = models.CharField(max_length=500, default='None')
    description = models.CharField(max_length=10000, default='None')
    company = models.CharField(max_length=500, default='None')
    service = models.CharField(max_length=500, default='None')
    url = models.CharField(max_length=3000, default='None')

    class Meta:
        db_table = "parsing_data"
