"""
Olive Oil Cost Calculator
Copyright (c) 2024 [Ηλίας Χατζηγεωργίου - Ilias Chatzigeorgiou]
All rights reserved.

This application calculates the production cost of olive oil.
Created by [Ηλίας Χατζηγεωργίου - Ilias Chatzigeorgiou]
Contact: [art_ilias@yahoo.com]
Version: 1.0

This code is protected by copyright law. Unauthorized copying, 
modification, or distribution of this code is strictly prohibited.
First release: February 2024
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class OliveOilCalculation(models.Model):
    # Α. Κόστος καλλιέργειας
    fertilizer_cost = models.DecimalField(
        "Λίπανση και φυτοπροστασία", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    irrigation_cost = models.DecimalField(
        "Άρδευση", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    other_works_cost = models.DecimalField(
        "Λοιπές εργασίες",
        max_digits=10, 
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    elga_cost = models.DecimalField(
        "ΕΛΓΑ", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    osde_cost = models.DecimalField(
        "Κόστος ΟΣΔΕ", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    agronomist_cost = models.DecimalField(
        "Κόστος Γεωπόνου", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    certification_cost = models.DecimalField(
        "Πιστοποιήσεις", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    # Β. Κόστος συγκομιδής
    daily_wage = models.DecimalField(
        "Ημερομίσθιο", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    working_days = models.PositiveIntegerField(
        "Ημέρες εργασίας",
        validators=[MinValueValidator(1)]
    )
    machinery_maintenance = models.DecimalField(
        "Συντήρηση μηχανημάτων", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    fuel_cost = models.DecimalField(
        "Καύσιμα", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    equipment_cost = models.DecimalField(
        "Παρελκόμενα", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    transport_cost = models.DecimalField(
        "Μεταφορικά", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    # Γ. Κόστος έκθλιψης
    total_oil_production = models.DecimalField(
        "Συνολική παραγωγή (kg)", 
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    mill_percentage = models.DecimalField(
        "Ποσοστό ελαιοτριβείου (%)", 
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    date_calculated = models.DateTimeField(auto_now_add=True)

    def get_cultivation_cost(self):
        return (self.fertilizer_cost +
                self.irrigation_cost + 
                self.elga_cost +
                self.osde_cost + 
                self.agronomist_cost +
                self.certification_cost +
                self.other_works_cost)

    def get_harvest_cost(self):
        return (self.daily_wage * self.working_days + 
                self.machinery_maintenance + self.fuel_cost + 
                self.equipment_cost + self.transport_cost)

    def get_mill_cost(self):
        total_cost = self.get_cultivation_cost() + self.get_harvest_cost()
        return total_cost * (self.mill_percentage / 100)

    def get_total_cost(self):
        return self.get_cultivation_cost() + self.get_harvest_cost() + self.get_mill_cost()

    def get_cost_per_kg(self):
        if self.total_oil_production > 0:
            return self.get_total_cost() / self.total_oil_production
        return 0
