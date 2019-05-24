from ..models import articleModel
from django.conf import settings
import csv
import os
from enum import Enum
# job_id,,,,,,,,,,,,,,,,


# Green-Fertiliser-Comes-Laced-With-Chemicals,green-fertiliser-comes-laced-with-chemicals,,d26b5faa2e9b20fc2167ab3459930d4f.jpg,a,5/10/2019--3:34:45-PM,5/10/2019--3:34:45-PM,Environment,deccan-chronicle,2016
class FieldReference(Enum):
    job_id = 0
    ns_category_id=1
    location_id = 2
    job_type_id = 3
    filename = 4
    job_title = 5
    job_slug = 6
    job_description = 7
    job_image = 8
    job_status = 9
    location = 12
    House_of = 13
    Year = 14
    epaper_link = 15
    image_link =16

def run():
    path = os.path.join(settings.BASE_DIR, "files", "sudhakar_u.csv")
    with open(path,"r") as f:
        lines = csv.reader(f)
        i=0

        for row in lines:
            if i ==0:
                i+=1
                continue
            # article = articleModel.objects.get_or_create(job_slug=FieldReference.job_slug, job_description=FieldReference.job_description, job_image=FieldReference.job_image, job_status =FieldReference.job_status, job_title=FieldReference.job_title, Year= FieldReference.Year, House_of=FieldReference.House_of)
            kwargs = {}
            for field in FieldReference:
              kwargs[field.name] = field.value


            object, created = articleModel.objects.get_or_create(**kwargs)
            print(object)

