from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class ProfessoresView(viewsets.ModelViewSet):
    queryset = Professores.objects.all()
    serializer_class = ProfessorSerializer

class DisciplinaView(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinaSerializer

class AlunoView(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = AlunoSerializer

class DisciplinaAlunoView(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinaAlunoSerializer

class PlanoAulaView(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = PlanoAulaSerializer

class AtividadeView(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = AtividadeSerializer

class AtividadeAlunoView(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = AtividadeAlunoSerializer

class FrequenciaView(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = FrequenciaSerializer





