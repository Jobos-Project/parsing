from django.shortcuts import HttpResponse
import requests, json
from ezpars.models import Job

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from ezpars.serializers import JobSerializer


def get_adzuna(request):
    # Данные с адзуна
    service = 'adzuna'
    r = requests.get(
        'https://api.adzuna.com/v1/api/jobs/gb/search/10?app_id=7c781e1b&app_key=14d8134416f7ad529c2432041d4095cc&content-type=application/json')

    Job.objects.filter(service=service).delete()

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
	salary = z.get("salary_min")

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
        if salary is None:
            salary = "None"

        Job.objects.create(description=description, company=company,
                                 location=location, contract_type=contract_type,
                                 contract_time=contract_time, title=title,
                                 service=service, url=url, salary=salary)

    return HttpResponse("gg")


def get_location_adzuna(location):
    s = ''
    for t in location:
        s = s + ', ' + t
    return s[2:]


# data from Github
class GithubJob(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        message = 'Jobs from Github'
        Job.objects.all().delete()

        for page in range(0, 5):
            response = requests.get(
                'https://jobs.github.com/positions.json?' + "page=" +
                str(page))
            resp = response.json()
            for job in resp:
                new_job = Job()
                new_job.name = job['title' or None]
                new_job.location = job['location' or None]
                new_job.about = job['description' or None]
                new_job.job_url = job['url' or None]
                new_job.company = job['company' or None]
                new_job.service = 'github'
                new_job.save()

        return HttpResponse(message)


class JobsView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        products = Job.objects.all()
        serializer = JobSerializer(products, many=True)
        return Response(serializer.data)
