from rest_framework import serializers
from django.core.exceptions import ValidationError
from puzzle.models import Word, Category, Group, Puzzle


class WordSerializer(serializers.ModelSerializer):
    """Serializer for Word objects"""
    class Meta:
        model = Word
        fields = ("id", "word",)
        read_only_fields = ("id",)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category objects"""
    class Meta:
        model = Category
        fields = ("id", "category",)
        read_only_fields = ("id",)


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group objects"""

    def validate(self, data):
        if len(data["words"]) != 4:
            raise ValidationError("Groups require exactly 4 words.")
        return data

    class Meta:
        model = Group
        fields = ("id", "group", "user", "categories", "words",)
        read_only_fields = ("id", "user",)


class GroupDetailSerializer(GroupSerializer):
    """ Detail Serializer for Group object"""
    words = WordSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)


class PuzzleSerializer(serializers.ModelSerializer):
    """Serializer for Puzzle object"""

    def validate(self, data):
        if len(data["groups"]) != 4:
            raise ValidationError("Puzzles require exactly 4 groups.")
        return data

    class Meta:
        model = Puzzle
        fields = ("id", "puzzle", "user", "groups")
        read_only_fields = ("id", "user",)


class PuzzleDetailSerialzer(PuzzleSerializer):
    """Detail Serializer for Puzzle object"""
    groups = GroupDetailSerializer(many=True, read_only=True)
