from django.db import models

# Create your models here.
class Them(models.Model):
    title = models.CharField('title', max_length=80, null=False)
    theory = models.TextField('theory')

    class Meta:
        db_table = 'Them'

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField('text')
    comment = models.TextField('comment')
    them = models.ForeignKey(Them, on_delete=models.CASCADE, db_column='Them_id')

    class Meta:
        db_table = 'Question'


class AnswerOptions(models.Model):
    text = models.TextField('text')
    right_ans = models.BooleanField('right_ans')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='Question_id')

    class Meta:
        db_table = 'Answer_options'