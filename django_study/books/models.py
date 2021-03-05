from django.db import models


# Create your models here.


class BookInfoManager(models.Manager):
    def get_queryset(self):
        # tiaojian shaixuan
        return super(BookInfoManager, self).get_queryset().filter(isDetelte=False)

    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDetelte = models.BooleanField(default=False)

    # table setting
    class Meta:
        db_table = 'bookinfo'
        # ordering = ['id']

    books1 = models.Manager()
    # zi ding yi jie guo guan li qi
    # result get : BookInfo.objects.all() = BookInfo.books2.all()
    books2 = BookInfoManager()
    # guanliqi moren objects

    # zidingyi kuaisu chuangjianduixiang
    @classmethod
    def create(cls, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, )
