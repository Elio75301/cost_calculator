from django.contrib import admin
from .models import OliveOilCalculation

@admin.register(OliveOilCalculation)
class OliveOilCalculationAdmin(admin.ModelAdmin):
    list_display = ('date_calculated', 'total_oil_production', 'get_cost_per_kg')
    list_filter = ('date_calculated',)
    
    fieldsets = (
        ('Κόστος Καλλιέργειας', {
            'fields': (
                'fertilizer_cost',
                'irrigation_cost',
                'other_works_cost',
                'elga_cost',
                'osde_cost',
                'agronomist_cost',
                'certification_cost',
                
            )
        }),
        ('Κόστος Συγκομιδής', {
            'fields': (
                'daily_wage',
                'working_days',
                'machinery_maintenance',
                'fuel_cost',
                'equipment_cost',
                'transport_cost',
            )
        }),
        ('Κόστος Έκθλιψης', {
            'fields': (
                'total_oil_production',
                'mill_percentage',
            )
        }),
    )

    def get_cost_per_kg(self, obj):
        return f"{obj.get_cost_per_kg():.2f} €/kg"
    get_cost_per_kg.short_description = "Κόστος ανά κιλό"
