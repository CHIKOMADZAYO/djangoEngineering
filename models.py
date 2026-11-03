from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.FloatField()
    email = models.EmailField(unique=True)
    course = models.JSONField()
    __feeBalance = models.FloatField()

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, course={self.course}, feeBalance={self.__feeBalance})"


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.TextField()
    credits = models.IntegerField()

    def __repr__(self):
        return f"Course(name={self.name}, person_id={self.person_id}, description={self.description}, credits={self.credits})"

    