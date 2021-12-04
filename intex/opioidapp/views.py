from django.shortcuts import render

# Create your views here.


# Main nav pages
def indexPageView(request) :
    return render(request, 'opioidapp/index.html')


def aboutPageView(request) :
    return render(request, 'opioidapp/about.html')


# Prescribers
def showPrescribersPageView(request) :
    return render(request, 'opioidapp/showPrescribers.html')

def showSinglePrescriberPageView(request) :
    return render(request, 'opioidapp/showSinglePrescriber.html')

def createPrescriberPageView(request) :
    return render(request, 'opioidapp/createPrescriber.html')

def editPrescriberPageView(request) :
    return render(request, 'opioidapp/editPrescriber.html')


# Drugs
def showDrugsPageView(request) :
    return render(request, 'opioidapp/showDrugs.html')

def showSingleDrugPageView(request) :
    return render(request, 'opioidapp/showSingleDrug.html')
