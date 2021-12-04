from django.urls import path
from .views import indexPageView, aboutPageView, createPrescriberPageView, editPrescriberPageView, showDrugsPageView, showPrescribersPageView, showSingleDrugPageView, showSinglePrescriberPageView




urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path("createPrescriber/", createPrescriberPageView, name="createPrescriber"),
    path("editPrescriber/", editPrescriberPageView, name="editPrescriber"),
    path("showDrugs/", showDrugsPageView, name="showDrugs"),
    path("showPrescribers/", showPrescribersPageView, name="showPrescribers"),
    path("showSingleDrug/", showSingleDrugPageView, name="showSingleDrug"),
    path("showSinglePrescriber/", showSinglePrescriberPageView, name="showSinglePrescriber"),
    path("", indexPageView, name="index"),    
]
