from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=255, null=False)
    position = models.CharField(max_length=255)
    Salary = models.IntegerField(max_length=255)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return 'ID: {}, Name: {}, Position:{}, Salart:{}'.format(self.id, self.name,self.position,self.Salary)


class Todo(models.Model):
    name = models.CharField(max_length=255, null=False)
    done = models.BooleanField(default=False, null=False)
    todo_list = models.ForeignKey(TodoList, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)
    

