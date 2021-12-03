from django.shortcuts import render
from .models import Drug, Prescriber, State, Triple, AvgData, PrescriberOnlyOpioids, highOpioids, OverallPrescriptions
# Create your views here.


# Main nav pages
def indexPageView(request) :
    return render(request, 'opioidapp/index.html')


def aboutPageView(request) :

    return render(request, 'opioidapp/about.html')


# Prescribers
def showPrescribersPageView(request) :
    data = Prescriber.objects.all()
    
    context = {
        "prescribers": data
    }
    return render(request, 'opioidapp/showPrescribers.html', context)

# def displayPrescribersPageView(request) :
#     data = Prescriber.objects.all()

#     context = {
#         "prescribe" : data,
#     }
    
#     return render(request, 'opioidapp/displayPrescribers.html', context)



# CRUD Prescribers
def showSinglePrescriberPageView(request, npi) :
        data = Prescriber.objects.get(npi = npi)

        sQuery = 'Select * from pd_triple where prescriberid = ' + 'cast(' + str(npi) + ' as int)'
        sQueryAverage = 'Select drugname, round(avg(qty)) as average from pd_triple where drugname in (Select drugname from pd_triple where prescriberid =' + 'cast(' + str(npi) + ' as int)' + ') group by drugname'

        tripledata = Triple.objects.raw(sQuery)
        avgdata = AvgData.objects.raw(sQueryAverage)

        context = {
            "record" : data,
            "tripledata": tripledata,
            "avgdata": avgdata,
         }

        return render(request, 'opioidapp/showSinglePrescriber.html', context)




def createPrescriberPageView(request) :
    if request.method == "POST" :
        prescriber = Prescriber()
        
        prescriber.npi = request.POST['npi']
        prescriber.fname = request.POST['fname']
        prescriber.lname = request.POST['lname']
        prescriber.gender = request.POST['gender']
        state = State.objects.get(stateabbrev = request.POST['state'])
        prescriber.state = state
        prescriber.credentials = request.POST['credentials']
        prescriber.specialty = request.POST['specialty']
        prescriber.isopioidprescriber = request.POST['isopioidprescriber']
        prescriber.totalprescriptions = request.POST['totalprescriptions']

        prescriber.save()

        return showPrescribersPageView(request)
    else :
        return render(request, 'opioidapp/createPrescriber.html')




def editPrescriberPageView(request, npi) :
    data = Prescriber.objects.get(npi = npi)

    context = {
        "record" : data,
    }
    return render(request, 'opioidapp/editPrescriber.html', context)


# Drugs
def showDrugsPageView(request) :
    drugs = Drug.objects.all()
    #print(drugs)

    context = {
        "drugs": drugs,
    }
    return render(request, 'opioidapp/showDrugs.html', context)

def showSingleDrugPageView(request, drugid) :
    drug = Drug.objects.get(drugid = drugid)

    sQuery = 'SELECT npi, fname, lname, t.drugname, qty FROM pd_prescriber p INNER JOIN pd_triple t ON p.npi = t.prescriberid INNER JOIN pd_drugs d ON d.drugname = t.drugname WHERE drugid = ' + str(drugid) + ' ORDER BY qty desc LIMIT 10;'
    data = Prescriber.objects.raw(sQuery)

    context = {
        "drug" : drug,
        "top_ten" : data,
    }
    return render(request, 'opioidapp/showSingleDrug.html', context)

def searchDrugsPageView(request):
    drugname = request.GET("drugname")
    isopioid = request.GET("isopioid")

    sQuery = 'SELECT drugid, drugname, isopioid FROM pd_drugs WHERE '

    if drugname != '' :
        sQuery += "AND drugname = '"+ drugname + "'"
    if isopioid != "" :
        sQuery += "AND isopioid = '"+ isopioid + "'"

    sQuery += 'ORDER BY isopioid, drugname;'
    
    data = Drug.objects.raw(sQuery)

    context = {
        "drugs" : data
    }
    
    return render(request, 'opioidapp/searchDrugs.html', context)

def searchPrescriberPageView(request) :
    firstName = request.POST['fname']
    lastName = request.POST['lname']
    gender = request.POST['gender']
    state = request.POST['state']
    isopioidprescriber = request.POST['isopioidprescriber']
    sQuery = 'SELECT npi, fname, lname, gender, state, specialty, isopioidprescriber FROM pd_prescriber WHERE '
    if firstName != '':
        sQuery += "fname = '"+ firstName + "'"
    if lastName != '':
        sQuery += "AND lname = '"+ lastName + "'"
    if gender != '':
        sQuery += "AND gender = '"+ gender + "'"
    if state != '':
        sQuery += "AND state = '"+ state + "'"
    if isopioidprescriber != '':
        sQuery += "isopioidprescriber = '"+ isopioidprescriber + "'"
    sQuery += 'ORDER BY lname, fname, isopioidprescriber, state, specialty'
    data = Prescriber.objects.raw(sQuery)
    context = {
        "prescribers" : data,
    }
    return render(request, 'opioidapp/searchPrescriber.html', context)


def updatePrescriberPageView(request):
    if request.method == 'POST':
        npi = request.POST['npi']

        prescriber = Prescriber.objects.get(npi = npi)

        prescriber.fname = request.POST['fname']
        prescriber.lname = request.POST['lname']
        prescriber.gender = request.POST['gender']
        prescriber.credentials = request.POST['credentials']
        state = State.objects.get(stateabbrev = request.POST['state'])
        prescriber.state = state
        prescriber.specialty = request.POST['specialty']

        prescriber.save()
        return showPrescribersPageView(request)

    return showPrescribersPageView(request)


def deletePrescriberPageView(request, npi):
    data = Prescriber.objects.get(npi = npi)

    data.delete()

    return render(request, 'opioidapp/showPrescribers.html')

def prescriberBehaviorPageView(request):

    sQuery = "SELECT id, prescriberid, drugname, qty FROM pd_triple t  INNER JOIN pd_prescriber p ON t.prescriberid = p.npi WHERE npi NOT IN (SELECT prescriberid FROM pd_triple t2 INNER JOIN pd_drugs d2 ON t2.drugname = d2.drugname WHERE isopioid = 'False' GROUP BY prescriberid)"

    prescribers = Triple.objects.raw(sQuery)

    context = {
        "prescribers" : prescribers,
    }
    return render(request, 'opioidapp/prescriberBehavior.html', context)

def highPrescriptionOpioidsrPageView(request):

    sQuery = "SELECT ot.prescriberid, ROUND((cast(OpioidCount as float)/cast(SUM(qty) as float))::numeric, 2)*100 as PctOpioids FROM pd_triple t INNER JOIN(SELECT prescriberid, SUM(qty) as OpioidCount FROM pd_triple t2 INNER JOIN pd_drugs d2 ON t2.drugname = d2.drugname WHERE isopioid = 'True' GROUP BY prescriberid) as ot ON t.prescriberid = ot.prescriberid GROUP BY ot.prescriberid, OpioidCount HAVING  ROUND((cast(OpioidCount as float)/cast(SUM(qty) as float))::numeric, 2)*100 > 70 ORDER BY PctOpioids desc;"

    prescribers = highOpioids.objects.raw(sQuery)

    context = {
        "prescribers" : prescribers,
    }
    return render(request, 'opioidapp/highOpioids.html', context)

    

def overallPrescriptionsPageView(request):

    sQuery = "SELECT ot.prescriberid, ROUND((cast(OpioidCount as float)/cast(SUM(qty) as float))::numeric, 2)*100 as PctOpioids FROM pd_triple t INNER JOIN(SELECT prescriberid, SUM(qty) as OpioidCount FROM pd_triple t2 INNER JOIN pd_drugs d2 ON t2.drugname = d2.drugname WHERE isopioid = 'True' GROUP BY prescriberid) as ot ON t.prescriberid = ot.prescriberid GROUP BY ot.prescriberid, OpioidCount HAVING  ROUND((cast(OpioidCount as float)/cast(SUM(qty) as float))::numeric, 2)*100 > 70 ORDER BY PctOpioids desc;"

    prescribers = OverallPrescriptions.objects.raw(sQuery)

    context = {
        "prescribers" : prescribers,
    }
    return render(request, 'opioidapp/overallPrescriptions.html', context)