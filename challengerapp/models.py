from django.db import models

class Product(models.Model):
    product_code = models.CharField(max_length=6,null=True,default='Auto')
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    price = models.IntegerField()
    sellflag = models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        #新規作成時処理（pkが存在しない場合）
        if not self.pk:
            last_id = Product.objects.order_by('-id').first()
            new_id = 1 if last_id is None else last_id.id + 1
            self.product_code = '{0:06}'.format(new_id)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name