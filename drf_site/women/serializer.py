from rest_framework import serializers
from .models import Women

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title','content','cat') # cat вместо cat_id и в запроса тоже нужно отправлять cat




"""class WomenSerializer(serializers.Serializer):  # создается на основе модели
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()  # внешний ключ записывается вот так

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        content = validated_data.get('content', instance.content)
        time_update = validated_data.get('time_update', instance.time_update)
        is_published = validated_data.get('is_published', instance.is_published)
        cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance"""

