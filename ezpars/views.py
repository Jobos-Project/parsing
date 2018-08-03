from django.shortcuts import render, HttpResponse
import requests, json
from ezpars.models import data_jobs

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from ezpars.serializers import JobSerializer

def get_adzuna(request):
    # Данные с адзуна
    service = 'adzuna'
    r = requests.get('https://api.adzuna.com/v1/api/jobs/gb/search/10?app_id=7c781e1b&app_key=14d8134416f7ad529c2432041d4095cc&content-type=application/json')

    data_jobs.objects.all().delete()

    response = r.json()
    data = json.dumps(response)
    x = json.loads(data)
    y = x.get("results")

    for z in y:

        description = z.get("description")
        company = z.get("company").get("display_name")
        location = get_location_adzuna(z.get("location").get("area"))
        contract_type = z.get("contract_type")
        contract_time = z.get("contract_time")
        title = z.get("title")
        url = z.get("redirect_url")

        if description is None:
            description = "None"
        if company is None:
            company = "None"
        if contract_type is None:
            contract_type = "None"
        if contract_time is None:
            contract_time = "None"
        if title is None:
            title = "None"
        if url is None:
            url = "None"

        data_jobs.objects.create(description=description, company=company,
                                 location=location, contract_type=contract_type,
                                 contract_time=contract_time, title=title,
                                 service=service, url=url)
    return HttpResponse("gg")


def get_location_adzuna(location):
    s = ''
    for t in location:
        s = s + ', ' + t
    return s[2:]


class JobsView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):

        products = data_jobs.objects.all()
        serializer = JobSerializer(products, many=True)
        return Response(serializer.data)






