
from django.contrib import admin
from django.urls import path, include
from api.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('professores/', include(routerProfessores.urls)),
    path('aluno/', include(routerAluno.urls)),
    path('disciplina/', include(routerDisciplina.urls)),
    path('atividade/', include(routerAtividade.urls)),
    path('disciplina_aluno/', include(routerDisciplinaAluno.urls)),
    path('plano_aula/', include(routerPlanoAula.urls)),
    path('atividade/', include(routerAtividade.urls)),
    path('atividade_aluno/', include(routerAtividadeAluno.urls)),
    path('frequencia/', include(routerFrequencia.urls)),








]
