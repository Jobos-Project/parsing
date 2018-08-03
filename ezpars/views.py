from django.shortcuts import render, HttpResponse
import requests, json

def get_adzuna(request):
    # Данные с адзуна
    r = requests.get('https://api.adzuna.com/v1/api/jobs/gb/search/10?app_id=7c781e1b&app_key=14d8134416f7ad529c2432041d4095cc&content-type=application/json')

    response = r.json()
    data = json.dumps(response)
    x = json.loads(data)
    y = x.get("results")

    for z in y:
        description = z.get("description")
        company = z.get("company")
        location = z.get("location").get("area")
        s = ''
        for t in location:
            s = s + ', ' + t
        location = s[2:]

        # print(description + " " + str(salary_min) + " " + str(salary_max) + " " + company + " " + location)
        print(" ")

    return HttpResponse("gg")

