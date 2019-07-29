from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CommonDatesModel(models.Model):
    """
    :Common Date Model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(CommonDatesModel):
    """
    :Product schema keeping only name for now.
    """
    name = models.CharField(max_length=255, null=True, blank=False)

    def __str__(self):
        return 'Product {}'.format(self.name)


class Order(CommonDatesModel):
    """
    :Order Schema . For this project harcoding the values
    :Auth User schema contains all possible detail for user
    :like first name, last name , email etc
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    amount = models.FloatField(null=True, blank=False)

    def __str__(self):
        return 'Order {}'.format(self.id)


class Comment(CommonDatesModel):
    """
    :Schema where users comment and post replies with respect to order.
    :Text: Where user will post the comments
    :Display: this field is to temporary hide/show the comment
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    comment_text = models.TextField()
    # deactivate inappropriate comments
    active = models.BooleanField(default=True)
    # for replies
    parent = models.ForeignKey('self', null=True,
                               related_name='replies',
                               on_delete=models.CASCADE)

    class Meta:
        # latest comment displaying first
        ordering = ('-created_at',)

    def __str__(self):
        return 'Comment by {}'.format(self.user.username)
