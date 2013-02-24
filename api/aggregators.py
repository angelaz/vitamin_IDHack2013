from vReport.models import *

# aggregate data over one district
def aggregateDistrict(d):
    supplemented_small = 0
    supplemented_big = 0
    dewormed = 0



    if (DistrictUser.objects.filter(user = d)):
        d = DistrictUser.objects.get(user = d)
        for user in d.individuals.all():
            for report in user.reports.all().filter(approved=True):
                supplemented_small += report.supplemented_small
                supplemented_big += report.supplemented_big
                dewormed += report.dewormed

        return (supplemented_small, supplemented_big, dewormed)
    elif (RegionalUser.objects.filter(user = d)):
        d = RegionalUser.objects.get(user = d)
        for district in d.districts.all():
            for user in district.individuals.all():
                for report in user.reports.all().filter(approved=True):
                    supplemented_small += report.supplemented_small
                    supplemented_big += report.supplemented_big
                    dewormed += report.dewormed

        return (supplemented_small, supplemented_big, dewormed)
    elif (NationalUser.objects.filter(user = d)):
        d = NationalUser.objects.get(user = d)
        for region in d.regions.all():
            for district in region.districts.all():
                for user in district.individuals.all():
                    for report in user.reports.all().filter(approved=True):
                        supplemented_small += report.supplemented_small
                        supplemented_big += report.supplemented_big
                        dewormed += report.dewormed

        return (supplemented_small, supplemented_big, dewormed)


# aggregate data over a region
#def aggregateRegion(up):
#    region = RegionalUser.objects.get(user=up)

    



    
    
