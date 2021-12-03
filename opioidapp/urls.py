from django.urls import path
from .views import indexPageView, aboutPageView, createPrescriberPageView, editPrescriberPageView
from .views import showDrugsPageView, showPrescribersPageView, showSingleDrugPageView 
from .views import showSinglePrescriberPageView, searchDrugsPageView, searchPrescriberPageView, updatePrescriberPageView, deletePrescriberPageView
from.views import prescriberBehaviorPageView, highPrescriptionOpioidsrPageView, overallPrescriptionsPageView



urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path("createPrescriber/", createPrescriberPageView, name="createPrescriber"),
    path("editPrescriber/<int:npi>/", editPrescriberPageView, name="editPrescriber"),
    path("deletePrescriber/<int:npi>/", deletePrescriberPageView, name="deletePrescriber"),
    path("updatePrescriber/", updatePrescriberPageView, name="updatePrescriber"),
    path("showDrugs/", showDrugsPageView, name="showDrugs"),
    path("showPrescribers/", showPrescribersPageView, name="showPrescribers"),
    path("showSingleDrug/<int:drugid>", showSingleDrugPageView, name="showSingleDrug"),
    path("showSinglePrescriber/<int:npi>/", showSinglePrescriberPageView, name="showSinglePrescriber"),
    path("searchDrugs", searchDrugsPageView, name="searchDrugs"),
    path("searchPrescriber", searchPrescriberPageView, name = "searchPrescriber"),
    path("prescriberBehavior", prescriberBehaviorPageView, name = "prescriberBehavior"),
    path("highPrescriptionOpioids", highPrescriptionOpioidsrPageView, name = "highOpioids"),
    path("overallPrescriptions", overallPrescriptionsPageView, name = "overallPrescriptions"),
    path("", indexPageView, name="index"),    
]
