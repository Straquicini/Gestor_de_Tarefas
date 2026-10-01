from django.db import models

# Classe Employee
class Employee(models.Model):
    name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


# Classe Task
class Task(models.Model):
    task = models.CharField(max_length=200)
    duration = models.IntegerField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.task