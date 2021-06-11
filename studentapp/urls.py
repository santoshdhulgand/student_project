

from django.urls import path
from studentapp import views

urlpatterns = [
    path('home/' , views.home_page_view),
    path('add/' , views.add_student_view),
    path('list/' , views.get_all_student_view),
    path('detail/<int:id>/' , views.student_detail_view),
    path('update/<int:id>/' , views.student_update_view),
    path('delete/<int:id>/' , views.student_delete_view),


]
