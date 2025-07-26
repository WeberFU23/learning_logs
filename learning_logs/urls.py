"""定义learning_logs的URL模式"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #homepage
    path('',views.index,name='index'),
    #show all topics
    path('topics/',views.topics,name='topics'),
    #show the detailed page of a specific topic
    path('topic/<int:topic_id>',views.topic,name='topic'),
    #used to add page of new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    #used to add page of new items under topic
    path('new_entry/<int:topic_id>',views.new_entry,name='new_entry'),
    #used to edit current item
    path('edit_entry/<int:entry_id>',views.edit_entry,name='edit_entry'),


]