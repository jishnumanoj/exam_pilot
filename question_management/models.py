from django.db import models

from django.utils.text import slugify

# Create your models here.

from assessment_management.models import Assessment

class Question(models.Model):
    title = models.CharField(max_length=200)
    
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )
    
    description = models.TextField(blank=True)
    
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name="questions")
    
    order = models.PositiveIntegerField(null=True)
    
    sample_input = models.CharField(max_length=200,null=True)
    
    sample_output = models.CharField(max_length=220,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self,*args,**kwargs):
        question_insatance = Question.objects.filter(assessment=self.assessment).last()
        if question_insatance:
            self.order = question_insatance.order + 1
        else:
            self.order = 1
        
        if not self.slug:
            self.slug = slugify(self.title)
            
        super().save(*args,**kwargs)
            
    def __str__(self):
        return f"{self.assessment.title} - {self.title}"
    
    class Meta:
        ordering = ["order"]
        unique_together = ["assessment","order"]
        