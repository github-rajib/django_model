from django.db import models


class PostCASCADE(models.Model):
    """For on_delete=models.CASCADE"""
    name = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Post CASCADE'


class CommentCASCADE(models.Model):
    """For on_delete=models.CASCADE"""
    description = models.TextField(blank=True, null=True)
    post = models.ForeignKey(PostCASCADE, on_delete=models.CASCADE, related_name='comments_cascade')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Comment CASCADE'


class PostPROTECT(models.Model):
    """For on_delete=models.PROTECT"""
    name = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Post PROTECT'


class CommentPROTECT(models.Model):
    """For on_delete=models.PROTECT"""
    description = models.TextField(max_length=120, blank=True, null=True)
    post = models.ForeignKey(PostPROTECT, on_delete=models.PROTECT, related_name='comments_protect')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Comment PROTECT'


class PostSETNULL(models.Model):
    """For on_delete=models.SET_NULL"""
    name = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Post SET_NULL'


class CommentSETNULL(models.Model):
    """For on_delete=models.SET_NULL"""
    description = models.TextField(max_length=120, blank=True, null=True)
    post = models.ForeignKey(PostSETNULL, on_delete=models.SET_NULL, related_name='comments_set_null', null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Comment SET_NULL'


class PostSETDEFAULT(models.Model):
    """For on_delete=models.SET_DEFAULT"""
    name = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Post SET_DEFAULT'


class CommentSETDEFAULT(models.Model):
    """For on_delete=models.SET_DEFAULT"""
    description = models.TextField(max_length=120, blank=True, null=True)
    post = models.ForeignKey(PostSETDEFAULT, on_delete=models.SET_DEFAULT, related_name='comments_set_default', default=5)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Comment SET_DEFAULT'


class PostSET(models.Model):
    """For on_delete=models.SET"""
    name = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Post SET'


def get_sentinel_post_set():
    return PostSET.objects.get_or_create(name='deleted')[0]


class CommentSET(models.Model):
    """For on_delete=models.SET"""
    description = models.TextField(max_length=120, blank=True, null=True)
    post = models.ForeignKey(PostSET, on_delete=models.SET(get_sentinel_post_set), related_name='comments_set')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Comment SET'


class PostDONOTHING(models.Model):
    """For on_delete=models.DO_NOTHING"""
    name = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Post DO_NOTHING'


class CommentDONOTHING(models.Model):
    """For on_delete=models.DO_NOTHING"""
    description = models.TextField(max_length=120, blank=True, null=True)
    post = models.ForeignKey(PostDONOTHING, on_delete=models.DO_NOTHING, related_name='comments_do_nothing')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Comment DO_NOTHING'
