from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, label='Email')
    password = serializers.CharField(required=True, label='Password', style={'input_type': 'password'},
                                     trim_whitespace=False)

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        if email and password:
            if validate_email(email):
                user_request = get_object_or_404(
                    User,
                    email=email
                )
                email = user_request.email
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)
            else:
                raise serializers.ValidationError('Unable to login with provided credentials.')
        else:
            raise serializers.ValidationError('Must include email and password')
        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
