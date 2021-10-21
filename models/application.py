from peewee import *

database = MySQLDatabase('dapp', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'port': 3306, 'user': 'root', 'password': 'lwh135190.'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class ApplicationCategory(BaseModel):
    count = IntegerField()
    create_time = DateTimeField()
    icon = CharField()
    icon_chosen = CharField()
    id = BigAutoField()
    name = CharField()
    name_en = CharField(null=True)
    name_zh_hans = CharField(null=True)
    rank = IntegerField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'application_category'

class ApplicationChains(BaseModel):
    background = CharField()
    color = CharField()
    color_icon = CharField()
    create_time = DateTimeField()
    explorer = CharField()
    icon = CharField()
    id = BigAutoField()
    name = CharField()
    name_en = CharField(null=True)
    name_zh_hans = CharField(null=True)
    token = IntegerField()
    unit = CharField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'application_chains'

class ApplicationApps(BaseModel):
    category = ForeignKeyField(column_name='category_id', field='id', model=ApplicationCategory, null=True)
    chains = ForeignKeyField(column_name='chains_id', field='id', model=ApplicationChains, null=True)
    create_time = DateTimeField()
    dapp_social = UnknownField(column_name='dappSocial', null=True)  # json
    desc = TextField()
    desc_en = TextField(null=True)
    desc_zh_hans = TextField(null=True)
    has_token = IntegerField(column_name='hasToken')
    icon = CharField()
    id = BigAutoField()
    identifier = CharField(unique=True)
    name = CharField()
    name_en = CharField(null=True)
    name_zh_hans = CharField(null=True)
    picture = CharField()
    social_signal = FloatField(column_name='socialSignal')
    social_signal_gr = FloatField(column_name='socialSignalGr')
    token_identifier = CharField(column_name='tokenIdentifier')
    update_time = DateTimeField()
    visit_website = CharField(column_name='visitWebsite')

    class Meta:
        table_name = 'application_apps'

class ApplicationTag(BaseModel):
    create_time = DateTimeField()
    id = BigAutoField()
    name = CharField()
    name_en = CharField(null=True)
    name_zh_hans = CharField(null=True)
    update_time = DateTimeField()

    class Meta:
        table_name = 'application_tag'

class ApplicationAppsTags(BaseModel):
    apps = ForeignKeyField(column_name='apps_id', field='id', model=ApplicationApps)
    id = BigAutoField()
    tag = ForeignKeyField(column_name='tag_id', field='id', model=ApplicationTag)

    class Meta:
        table_name = 'application_apps_tags'
        indexes = (
            (('apps', 'tag'), True),
        )

class ApplicationAppsdata(BaseModel):
    active_address = UnknownField(column_name='activeAddress')  # json
    amount24h = FloatField()
    amount24h_gr = FloatField(column_name='amount24hGr')
    amount30d = FloatField()
    amount30d_gr = FloatField(column_name='amount30dGr')
    amount7d = FloatField()
    amount7d_gr = FloatField(column_name='amount7dGr')
    app = ForeignKeyField(column_name='app_id', field='id', model=ApplicationApps, unique=True)
    create_time = DateTimeField()
    date_labels = UnknownField(column_name='dateLabels')  # json
    holders = UnknownField()  # json
    id = BigAutoField()
    price_data = UnknownField(column_name='priceData')  # json
    social_signal_ath = FloatField(column_name='socialSignalAth')
    social_signal_ath_date = CharField(column_name='socialSignalAthDate')
    social_signal_data = UnknownField(column_name='socialSignalData')  # json
    total_days = FloatField(column_name='totalDays')
    transactions_ath = FloatField(column_name='transactionsAth')
    transactions_ath_date = CharField(column_name='transactionsAthDate')
    transactions_data = UnknownField(column_name='transactionsData')  # json
    transactions_total = FloatField(column_name='transactionsTotal')
    transfer_count = UnknownField(column_name='transferCount')  # json
    transfer_volume = UnknownField(column_name='transferVolume')  # json
    update_time = DateTimeField()
    usd24h = FloatField()
    usd24h_gr = FloatField(column_name='usd24hGr')
    usd30d = FloatField()
    usd30d_gr = FloatField(column_name='usd30dGr')
    usd7d = FloatField()
    usd7d_gr = FloatField(column_name='usd7dGr')
    user24h = FloatField()
    user24h_gr = FloatField(column_name='user24hGr')
    user30d = FloatField()
    user30d_gr = FloatField(column_name='user30dGr')
    user7d = FloatField()
    user7d_gr = FloatField(column_name='user7dGr')
    user_ath = FloatField(column_name='userAth')
    user_ath_date = CharField(column_name='userAthDate')
    user_total = FloatField(column_name='userTotal')
    users_data = UnknownField(column_name='usersData')  # json
    volume_ath = FloatField(column_name='volumeAth')
    volume_ath_date = CharField(column_name='volumeAthDate')
    volume_data = UnknownField(column_name='volumeData')  # json
    volume_total = FloatField(column_name='volumeTotal')

    class Meta:
        table_name = 'application_appsdata'

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = 'auth_group'

class DjangoContentType(BaseModel):
    app_label = CharField()
    model = CharField()

    class Meta:
        table_name = 'django_content_type'
        indexes = (
            (('app_label', 'model'), True),
        )

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType)
    name = CharField()

    class Meta:
        table_name = 'auth_permission'
        indexes = (
            (('content_type', 'codename'), True),
        )

class AuthGroupPermissions(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    id = BigAutoField()
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)

    class Meta:
        table_name = 'auth_group_permissions'
        indexes = (
            (('group', 'permission'), True),
        )

class AuthenticationAuthuser(BaseModel):
    date_joined = DateTimeField()
    email = CharField(null=True)
    id = BigAutoField()
    ip = CharField(null=True)
    is_active = IntegerField()
    is_staff = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField(null=True)
    password = CharField()
    phone = CharField(null=True)
    uid = CharField(unique=True)
    username = CharField(null=True, unique=True)

    class Meta:
        table_name = 'authentication_authuser'

class AuthenticationAuthuserGroups(BaseModel):
    authuser = ForeignKeyField(column_name='authuser_id', field='id', model=AuthenticationAuthuser)
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    id = BigAutoField()

    class Meta:
        table_name = 'authentication_authuser_groups'
        indexes = (
            (('authuser', 'group'), True),
        )

class AuthenticationAuthuserUserPermissions(BaseModel):
    authuser = ForeignKeyField(column_name='authuser_id', field='id', model=AuthenticationAuthuser)
    id = BigAutoField()
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)

    class Meta:
        table_name = 'authentication_authuser_user_permissions'
        indexes = (
            (('authuser', 'permission'), True),
        )

class AuthenticationUserprofile(BaseModel):
    avatar = CharField(null=True)
    id = BigAutoField()
    nickname = CharField(null=True)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthenticationAuthuser, unique=True)

    class Meta:
        table_name = 'authentication_userprofile'

class DjangoAdminLog(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = TextField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType, null=True)
    object_id = TextField(null=True)
    object_repr = CharField()
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthenticationAuthuser)

    class Meta:
        table_name = 'django_admin_log'

class DjangoApschedulerDjangojob(BaseModel):
    id = CharField(primary_key=True)
    job_state = TextField()
    next_run_time = DateTimeField(index=True, null=True)

    class Meta:
        table_name = 'django_apscheduler_djangojob'

class DjangoApschedulerDjangojobexecution(BaseModel):
    duration = DecimalField(null=True)
    exception = CharField(null=True)
    finished = DecimalField(null=True)
    id = BigAutoField()
    job = ForeignKeyField(column_name='job_id', field='id', model=DjangoApschedulerDjangojob)
    run_time = DateTimeField(index=True)
    status = CharField()
    traceback = TextField(null=True)

    class Meta:
        table_name = 'django_apscheduler_djangojobexecution'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    id = BigAutoField()
    name = CharField()

    class Meta:
        table_name = 'django_migrations'

class DjangoSession(BaseModel):
    expire_date = DateTimeField(index=True)
    session_data = TextField()
    session_key = CharField(primary_key=True)

    class Meta:
        table_name = 'django_session'

class SitecfgBanner(BaseModel):
    banner_image = CharField(null=True)
    create_time = DateTimeField()
    enable = IntegerField()
    id = BigAutoField()
    no = IntegerField()
    target = CharField()
    title = CharField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'sitecfg_banner'

class SitecfgContactus(BaseModel):
    category = IntegerField()
    content = CharField()
    create_time = DateTimeField()
    id = BigAutoField()
    image = CharField(null=True)
    title = CharField()
    title_en = CharField(null=True)
    title_zh_hans = CharField(null=True)
    update_time = DateTimeField()

    class Meta:
        table_name = 'sitecfg_contactus'

class SitecfgSupport(BaseModel):
    category = IntegerField()
    content = TextField()
    content_en = TextField(null=True)
    content_zh_hans = TextField(null=True)
    create_time = DateTimeField()
    enable = IntegerField()
    icon = CharField(null=True)
    id = BigAutoField()
    image = CharField(null=True)
    no = IntegerField()
    remark = CharField()
    title = CharField()
    title_en = CharField(null=True)
    title_zh_hans = CharField(null=True)
    type = CharField(null=True)
    update_time = DateTimeField()

    class Meta:
        table_name = 'sitecfg_support'

class SocialEmail(BaseModel):
    content = TextField()
    create_time = DateTimeField()
    id = BigAutoField()
    send_state = IntegerField()
    send_time = DateTimeField(null=True)
    title = CharField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'social_email'

class SocialEmailrecord(BaseModel):
    create_time = DateTimeField()
    email = ForeignKeyField(column_name='email_id', field='id', model=SocialEmail)
    id = BigAutoField()
    messages = CharField(null=True)
    state = IntegerField()
    to = CharField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'social_emailrecord'

class SocialNews(BaseModel):
    content = TextField()
    content_en = TextField(null=True)
    content_zh_hans = TextField(null=True)
    create_time = DateTimeField()
    enable = IntegerField()
    header = CharField(null=True)
    id = BigAutoField()
    no = IntegerField()
    page_views = IntegerField()
    seo_desc = CharField(null=True)
    seo_desc_en = CharField(null=True)
    seo_desc_zh_hans = CharField(null=True)
    seo_key = CharField(null=True)
    seo_key_en = CharField(null=True)
    seo_key_zh_hans = CharField(null=True)
    seo_title = CharField(null=True)
    seo_title_en = CharField(null=True)
    seo_title_zh_hans = CharField(null=True)
    title = CharField()
    title_en = CharField(null=True)
    title_zh_hans = CharField(null=True)
    update_time = DateTimeField()

    class Meta:
        table_name = 'social_news'

class SocialNewsApprelated(BaseModel):
    apps = ForeignKeyField(column_name='apps_id', field='id', model=ApplicationApps)
    id = BigAutoField()
    news = ForeignKeyField(column_name='news_id', field='id', model=SocialNews)

    class Meta:
        table_name = 'social_news_apprelated'
        indexes = (
            (('news', 'apps'), True),
        )

class SocialNewsNewrelated(BaseModel):
    from_news = ForeignKeyField(column_name='from_news_id', field='id', model=SocialNews)
    id = BigAutoField()
    to_news = ForeignKeyField(backref='social_news_to_news_set', column_name='to_news_id', field='id', model=SocialNews)

    class Meta:
        table_name = 'social_news_newrelated'
        indexes = (
            (('from_news', 'to_news'), True),
        )

class SocialTag(BaseModel):
    create_time = DateTimeField()
    icon = CharField(null=True)
    id = BigAutoField()
    name = CharField()
    name_en = CharField(null=True)
    name_zh_hans = CharField(null=True)
    update_time = DateTimeField()

    class Meta:
        table_name = 'social_tag'

class SocialNewsTags(BaseModel):
    id = BigAutoField()
    news = ForeignKeyField(column_name='news_id', field='id', model=SocialNews)
    tag = ForeignKeyField(column_name='tag_id', field='id', model=SocialTag)

    class Meta:
        table_name = 'social_news_tags'
        indexes = (
            (('news', 'tag'), True),
        )

class SocialProject(BaseModel):
    chain = ForeignKeyField(column_name='chain_id', field='id', model=ApplicationChains)
    content = TextField()
    content_en = TextField(null=True)
    content_zh_hans = TextField(null=True)
    create_time = DateTimeField()
    enable = IntegerField()
    header = CharField(null=True)
    id = BigAutoField()
    no = IntegerField()
    publish_time = DateTimeField(null=True)
    telegram = CharField()
    title = CharField()
    title_en = CharField(null=True)
    title_zh_hans = CharField(null=True)
    tutorial = CharField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'social_project'

class SocialSubscribe(BaseModel):
    create_time = DateTimeField()
    email = CharField()
    id = BigAutoField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'social_subscribe'

