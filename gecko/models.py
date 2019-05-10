from django.db import models
class Administrators(models.Model):
        '''运维信息表'''
        name = models.CharField(max_length=32,blank=True,null=True)
        department_choices = (
            (0,'研发部'),
            (1,'运营部'),
            (2,'人力资源部'),
            (3,'财务部'),
            (4,'运维部')
        )
        department = models.SmallIntegerField(choices=department_choices)
        consult_course = models.ForeignKey("Course",on_delete=models.CASCADE,verbose_name="咨询课程")
        position = models.CharField(max_length=32,blank=True,null=True)
        qq = models.CharField(max_length=64, unique=True)
        date = models.DateTimeField(auto_now_add=True)
        tags = models.ManyToManyField("Tag", blank=True)
        class Meta:
            verbose_name = "维护人"
            verbose_name_plural = "维护人"
        def __str__(self):
            return self.name

class Tag(models.Model):
    name = models.CharField(unique=True,max_length=32)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

class Course(models.Model):
    '''课程表'''
    name = models.CharField(max_length=64,unique=True)
    price = models.PositiveSmallIntegerField()
    period = models.PositiveSmallIntegerField(verbose_name="周期(月)")
    outline = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "课程表"
        verbose_name_plural = "课程表"
