from rest_framework import routers
from .views import *

routerAluno = routers.DefaultRouter()
routerAluno.register(r'aluno', AlunoView)

routerProfessores = routers.DefaultRouter()
routerProfessores.register(r'professores', ProfessoresView)

routerDisciplina = routers.DefaultRouter()
routerDisciplina.register(r'disciplina', DisciplinaView)

routerDisciplinaAluno = routers.DefaultRouter()
routerDisciplinaAluno.register(r'disciplina_aluno', DisciplinaAlunoView)

routerPlanoAula = routers.DefaultRouter()
routerPlanoAula.register(r'plano_aula', PlanoAulaView)

routerAtividade = routers.DefaultRouter()
routerAtividade.register(r'atividade', AtividadeView)

routerAtividadeAluno = routers.DefaultRouter()
routerAtividadeAluno.register(r'atividade_aluno', AtividadeAlunoView)

routerFrequencia = routers.DefaultRouter()
routerFrequencia.register(r'frequencia', FrequenciaView)
