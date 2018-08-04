from rest_framework import serializers
from ezpars.models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ("location", "contract_type", "contract_time", "title",
                  "description", "company", "service", "url", "salary")


