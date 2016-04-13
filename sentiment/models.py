# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
from .utils import SENTIMENT_LABELS


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45, blank=True)
    idcategoria = models.ForeignKey('Categoria', db_column='idcategoria', blank=True, null=True)
    ignore = models.IntegerField(blank=True, null=True)
    inserted_on = models.IntegerField(blank=True, null=True)
    updated_on = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_brand'


class Canalesocial(models.Model):
    id = models.IntegerField(primary_key=True)
    idbrand = models.ForeignKey(Brand, db_column='idbrand', blank=True, null=True, related_name='idbrand')
    idsocial = models.ForeignKey('Social', db_column='idsocial', blank=True, null=True)
    official = models.IntegerField(blank=True, null=True)
    discovered_by = models.ForeignKey(Brand, db_column='discovered_by', blank=True, null=True, related_name='discovered_by')
    username = models.CharField(max_length=45, blank=True)
    lastupdated = models.IntegerField(blank=True, null=True)
    usernameid = models.TextField(blank=True)
    authtoken = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'im_canalesocial'


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=140)
    slug = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'im_categoria'


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    idpost = models.ForeignKey('Post', db_column='idpost', blank=True, null=True)
    content = models.TextField(blank=True)
    from_id = models.TextField(blank=True)
    created_on = models.IntegerField(blank=True, null=True)
    originalidcomment = models.TextField(db_column='originalIdCommento', blank=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'im_commento'

    def __str__(self):
        return 'comment_id: %s, %s, content: %s' % (self.id, self.idpost, self.content[:20])


class Contratto(models.Model):
    id = models.IntegerField(primary_key=True)
    datainizio = models.IntegerField(blank=True, null=True)
    datascadenza = models.IntegerField(blank=True, null=True)
    iduser = models.ForeignKey('User', db_column='iduser', blank=True, null=True)
    idbrand = models.ForeignKey(Brand, db_column='idbrand', blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'im_contratto'


class Followers(models.Model):
    id = models.IntegerField(primary_key=True)
    idcanalesocial = models.ForeignKey(Canalesocial, db_column='idcanalesocial', blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_followers'


class Following(models.Model):
    id = models.IntegerField(primary_key=True)
    idcanalesocial = models.ForeignKey(Canalesocial, db_column='idcanalesocial', blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_following'


class Mention(models.Model):
    id = models.IntegerField(primary_key=True)
    idpost = models.ForeignKey('Post', db_column='idpost', blank=True, null=True)
    idbrand = models.ForeignKey(Brand, db_column='idbrand', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_mention'


class Metrica(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=120, blank=True)
    slug = models.CharField(max_length=120, blank=True)
    descrizione = models.TextField(blank=True)
    icona = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'im_metrica'


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    idcanalesocial = models.ForeignKey(Canalesocial, db_column='idcanalesocial', blank=True, null=True)
    content = models.TextField(blank=True)
    link = models.TextField(blank=True)
    likes = models.IntegerField(blank=True, null=True)
    var_likes = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    var_comments = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)
    var_shares = models.IntegerField(blank=True, null=True)
    img = models.TextField(blank=True)
    originalidpost = models.TextField(db_column='originalIdPost', blank=True) # Field name made lowercase.
    timestamp = models.IntegerField(blank=True, null=True)
    inserted_on = models.IntegerField(blank=True, null=True)
    updated_on = models.IntegerField(blank=True, null=True)
    postlink = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'im_post'

    def __str__(self):
        return 'post_id: %s' % self.id


class Ruolo(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    nomeruolo = models.CharField(max_length=45)
    class Meta:
        managed = False
        db_table = 'im_ruolo'


class Social(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    slug = models.CharField(unique=True, max_length=45, blank=True)
    likesterm = models.CharField(max_length=40, blank=True)
    basepath = models.CharField(max_length=200, blank=True)
    data_available = models.IntegerField(blank=True, null=True)
    has_login = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_social'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45, blank=True)
    password = models.CharField(max_length=45, blank=True)
    email = models.CharField(max_length=100, blank=True)
    nome = models.CharField(max_length=45, blank=True)
    idruolo = models.ForeignKey(Ruolo, db_column='idruolo', blank=True, null=True)
    idbrand = models.ForeignKey(Brand, db_column='idbrand', blank=True, null=True)
    usertoken = models.CharField(max_length=100, blank=True)
    lastlogin = models.IntegerField(blank=True, null=True)
    tokenexpires = models.IntegerField(blank=True, null=True)
    createdon = models.IntegerField(blank=True, null=True)
    pic = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'im_user'


class Valoremetrica(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    timestamp = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    idcanalesociale = models.ForeignKey(Canalesocial, db_column='idcanalesociale', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_valoremetrica'


class PostSentiment(models.Model):
    id = models.AutoField(primary_key=True)
    idpost = models.OneToOneField('Post', db_column='idpost', related_name='post_sentiment')
    real_sentiment = models.CharField(choices=SENTIMENT_LABELS, max_length=8, blank=True, null=True)
    sentiment_api1 = JSONField(blank=True, null=True)
    sentiment_api2 = JSONField(blank=True, null=True)
    sentiment_api3 = JSONField(blank=True, null=True)
    sentiment_api4 = JSONField(blank=True, null=True)

    sentiment_api1_en = JSONField(blank=True, null=True)
    sentiment_api2_en = JSONField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'im_post_sentiment'


class CommentSentiment(models.Model):
    id = models.AutoField(primary_key=True)
    idcomment = models.OneToOneField('Comment', db_column='idcommento', related_name='comment_sentiment')
    language = models.CharField(max_length=45, blank=True)
    english_translation = models.TextField(blank=True)
    real_sentiment = models.CharField(choices=SENTIMENT_LABELS, max_length=8, blank=True, null=True)
    sentiment_api1 = models.CharField(choices=SENTIMENT_LABELS, max_length=8, blank=True, null=True)
    sentiment_api2 = models.CharField(choices=SENTIMENT_LABELS, max_length=8, blank=True, null=True)
    sentiment_api3 = models.CharField(choices=SENTIMENT_LABELS, max_length=8, blank=True, null=True)
    sentiment_api4 = models.CharField(choices=SENTIMENT_LABELS, max_length=8, blank=True, null=True)

    sentiment_api1_en = models.CharField(choices=SENTIMENT_LABELS, max_length=8, blank=True, null=True)
    sentiment_api2_en = models.CharField(choices=SENTIMENT_LABELS, max_length=8, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'im_commento_sentiment'
