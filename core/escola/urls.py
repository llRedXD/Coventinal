from django.urls import include, path
from rest_framework import routers
from core.escola import views

router = routers.DefaultRouter()
router.register(r'alunos', views.AlunoViewSet)
router.register(r'cursos', views.CursoViewSet)
router.register(r'matriculas', views.MatriculaViewSet)


