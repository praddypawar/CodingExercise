from rest_framework import serializers
from django import forms
from .models import Weather,Corn_grain_yield,DataAnalysis

class WeatherDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Weather
        fields = ["id","dates","max_temp","min_temp","precipitation"]


class Corn_grain_yieldDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Corn_grain_yield
        fields = ["id","year","harvested"]


class DataAnalysisSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DataAnalysis
        fields = ["id","year","max_temp_avg","min_temp_avg","total_precipitation"]