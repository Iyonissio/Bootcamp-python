from django.db import models



class Topic(models.Model):
    top_name=models.CharField(max_length=258,unique=True)

    def __str__(self):
        return self.top_name

class Paginaweb(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=258,unique=True)
    url =models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Paginaweb, on_delete=models.CASCADE)
    data=models.DateField()

    def __str__(self):
        return str(self.data)
