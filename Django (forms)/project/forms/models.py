from django.db import models

# Soruları temsil eden model
class Question(models.Model):
    text = models.CharField(max_length=255)  # Soru metni

    def __str__(self):
        return self.text  # Soru metnini döndür

# Cevapları temsil eden model
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)  # Hangi soruya ait
    text = models.CharField(max_length=255)  # Cevap metni
    is_correct = models.BooleanField(default=False)  # Doğru mu yanlış mı olduğunu belirtir

    def __str__(self):
        return self.text  # Cevap metnini döndür
