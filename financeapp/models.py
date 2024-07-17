from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date
from PIL import Image
from tinymce.models import HTMLField


class IncomeCategory(models.Model):
    category = models.CharField('Category', max_length=100)

    class Meta:
        verbose_name = 'Income category'
        verbose_name_plural = 'Income categories'

    def __str__(self):
        return f"{self.category}"


class ExpenseCategory(models.Model):
    category = models.CharField('Category', max_length=100)

    class Meta:
        verbose_name = 'Expense category'
        verbose_name_plural = 'Expense categories'

    def __str__(self):
        return f"{self.category}"


class Income(models.Model):
    amount = models.IntegerField('Amount')
    date = models.DateField('Date')
    note = HTMLField(null=True, blank=True)
    income_category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('date', 'amount')
        verbose_name = 'Income'
        verbose_name_plural = 'Income'

    @property
    def get_total_amount(self):
        income = Income.objects.all()
        total_amount = sum(row.amount for row in income)
        return total_amount

    def __str__(self):
        return f'{self.date} {self.amount} {self.note}'


class Company(models.Model):
    name = models.CharField('Name', max_length=100)
    address = models.CharField('Address', max_length=100)
    phone = models.CharField('Phone', max_length=100)
    email = models.CharField('Email', max_length=100)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.name} {self.address} {self.phone} {self.email}'


class Expense(models.Model):
    amount = models.IntegerField('Amount')
    date = models.DateField('Date')
    note = HTMLField(null=True, blank=True)
    pic = models.ImageField('Invoice', upload_to='pics', null=True, blank=True)
    expense_category = models.ManyToManyField(ExpenseCategory)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('date', 'amount')

    def __str__(self):
        return f'{self.date} {self.amount} {self.note}'

    def display_categories(self):
        return ', '.join(elem.category for elem in self.expense_category.all())


class BillIssuer(models.Model):
    name = models.CharField('Name', max_length=100)
    address = models.CharField('Address', max_length=100)
    phone = models.CharField('Phone', max_length=100)
    email = models.CharField('Email', max_length=100)

    def __str__(self):
        return f'{self.name} {self.address} {self.phone} {self.email}'


class BillCategory(models.Model):
    category = models.CharField('Category', max_length=100)

    class Meta:
        verbose_name = 'Bill category'
        verbose_name_plural = 'Bill categories'

    def __str__(self):
        return f"{self.category}"


class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    amount = models.IntegerField('Amount')
    date_due = models.DateField('Date due')
    date_paid = models.DateField('Date paid', null=True, blank=True)
    note = HTMLField(null=True, blank=True)
    pic = models.ImageField('Bill', upload_to='pics', null=True, blank=True)
    bill_issuer = models.ForeignKey(BillIssuer, on_delete=models.CASCADE)
    bill_category = models.ForeignKey(BillCategory, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    BILL_STATUS = (
        ('u', 'Unpaid'),
        ('p', 'Paid on time'),
        ('o', 'Overdue'),
        ('l', 'Paid late')
    )

    status = models.CharField(
        max_length=1,
        choices=BILL_STATUS,
        blank=True,
        default='u',
        help_text='Bill status'
    )

    def __str__(self):
        return f"{self.date_due} {self.date_paid} {self.amount}"


class Profile(models.Model):
    picture = models.ImageField(upload_to='profile_pics', default='default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        thumb_size = (200, 200)
        img.thumbnail(thumb_size)
        img.save(self.picture.path)


class AppReview(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Review', max_length=2000)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.date_created}, {self.reviewer}, {self.content[:50]}'
