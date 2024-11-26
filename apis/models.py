from django.db import models



class Dish(models.Model):
    CHOICE_TIME = (
        ("BREAKFEST","breakfast"),
        ("LUNCH","lunch"),
        ("DINNER","dinner"),
        ("dessert","dessert"),
        ("Drinks","drinks"),
        ("Snacks","snacks")
    )
    name_dish = models.CharField(max_length=50)
    descriptions = models.TextField()
    time_category = models.CharField(max_length=50, choices=CHOICE_TIME)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    prf_time = models.CharField(max_length=50)
    img = models.ImageField(upload_to="media/images",)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_dish

class Table(models.Model):
    CHOICE_STATUS=(
        ("Full", "FULL"),
        ("Free", "Free"),

    )
    CHOICE_TABLE =(
        ("vip", "vip"),
        ("table", "table"),
        ("Cud", "cud")
    )
    type = models.CharField(max_length=50, choices=CHOICE_TABLE)
    max_person = models.IntegerField()
    status = models.CharField(max_length=50, choices=CHOICE_STATUS, null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.type
    

class Bill(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    castumername = models.CharField(max_length=50)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    is_paid = models.BooleanField(default=False,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    def save(self, *args, **kwargs):
        if self.is_paid:
            self.table.status = "Free"
            self.is_active = False
        else:
            self.table.status = "Full"
        self.table.save()
        super().save(*args, **kwargs) 
    def __str__(self):
        return self.castumername
    

class Order(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='orders')
    count = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total = self.dish.price * self.count
        self.bill.total_sum += self.total 
        self.bill.save() 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.dish} -> {self.bill}"


    

