from rest_framework import serializers
from django.contrib.auth import get_user_model
from book.models import Book
from user.models import Reader

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'address')

    def create(self, validated_data):
        address = validated_data.pop('address', '')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role='Читатель'
        )
        Reader.objects.create(user=user,
                              address=address)
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']


class BookDetailSerializer(serializers.ModelSerializer):
    borrowed_date = serializers.DateTimeField()
    days_borrowed = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'borrowed_date', 'days_borrowed']

    def get_days_borrowed(self, obj):
        from django.utils import timezone
        now = timezone.now()
        if obj.borrowed_date:
            return (now - obj.borrowed_date).days
        return 0
