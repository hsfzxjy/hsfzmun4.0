from rest_framework import serializers
from .models import Article, Tag, Comment

from files.models import Attachment
from users.models import User
from files.serializers import AttachmentSerializer
from users.serializers import UserSerializer, normalize_user
from language.serializers import AbstractLanguageSerializer


class TagSerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    class Meta:
        model = Tag
        fields = ['name']

    def to_internal_value(self, data):
        if isinstance(data, (int, str)):
            return data

        return super(TagSerializer, self).to_internal_value(data)


class ArticleSerializer(AbstractLanguageSerializer):

    author = UserSerializer(validators=[])
    tags = TagSerializer(many=True)
    attachments = AttachmentSerializer(
        many=True, validators=[], required=False)
    mentions = UserSerializer(many=True, validators=[], required=False)
    url = serializers.CharField(read_only=True)
    is_article = serializers.BooleanField(read_only=True)
    content = serializers.CharField(required=False, allow_blank=True)
    article_tag = serializers.CharField(read_only=True)

    def create(self, validated_data):
        tag_list = validated_data.pop('tags', [])
        attachments = validated_data.pop('attachments', [])
        mentions = validated_data.pop('mentions', [])
        normalize_user(validated_data, 'author')
        validated_data['lang_code'] = validated_data['author'].lang_code

        article = Article.objects.create(**validated_data)

        article.tags.add(*Tag.objects.create_from_list(tag_list))
        article.attachments.set(Attachment.objects.filter(
            pk__in=attachments))
        article.mentions.set(User.objects.filter(
            nickname__in=mentions).only('id'), bulk=True)

        return article

    def update(self, instance, validated_data):
        tag_list = validated_data.pop('tags', [])
        attachments = validated_data.pop('attachments', [])
        old_tags = instance.tags.values_list('name', flat=True)
        normalize_user(validated_data, 'author')

        article = super(ArticleSerializer, self).update(
            instance, validated_data)

        article.tags.set(Tag.objects.update_from_list(
            old_tags, tag_list), clear=True)
        article.attachments.set(Attachment.objects.filter(
            pk__in=attachments))

        return article

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    author = UserSerializer(validators=[])
    reply_to = UserSerializer(validators=[], required=False)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        normalize_user(validated_data, 'author')
        normalize_user(validated_data, 'reply_to')
        return super(CommentSerializer, self).create(validated_data)
