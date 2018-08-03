from django.db import models

class data_jobs(models.Model):
    # location — место работы
    # contract_type — тип контракта
    # contract_time — тип занятости
    # title — наименование вакансии
    # description — описание вакансии
    # company — наименование компании
    # service — наименование сайта, откуда вакансия

    location = models.CharField(max_length=500)
    contract_type = models.CharField(max_length=500)
    contract_time = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    company = models.CharField(max_length=500)
    service = models.CharField(max_length=500)

    class Meta:
        db_table = "parsing_data"
