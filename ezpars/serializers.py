from rest_framework import serializers
from ezpars.models import data_jobs


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = data_jobs
        fields = ("location", "contract_type", "contract_time", "title",
                  "description", "company", "service")


