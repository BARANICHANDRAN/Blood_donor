from django.db import models

TAMIL_NADU_DISTRICTS = [
    ("Chennai", "Chennai"),
    ("Coimbatore", "Coimbatore"),
    ("Madurai", "Madurai"),
    ("Tiruchirappalli", "Tiruchirappalli"),
    ("Salem", "Salem"),
    ("Erode", "Erode"),
    ("Vellore", "Vellore"),
    ("Thanjavur", "Thanjavur"),
    ("Thoothukudi", "Thoothukudi"),
    ("Tirunelveli", "Tirunelveli"),
    ("Dindigul", "Dindigul"),
    ("Cuddalore", "Cuddalore"),
    ("Kancheepuram", "Kancheepuram"),
    ("Tiruvannamalai", "Tiruvannamalai"),
    ("Nagapattinam", "Nagapattinam"),
    ("Mayiladuthurai", "Mayiladuthurai"),
    ("Ramanathapuram", "Ramanathapuram"),
    ("Sivaganga", "Sivaganga"),
    ("Krishnagiri", "Krishnagiri"),
    ("Namakkal", "Namakkal"),
    ("Perambalur", "Perambalur"),
    ("Pudukkottai", "Pudukkottai"),
    ("Theni", "Theni"),
    ("Villupuram", "Villupuram"),
    ("Virudhunagar", "Virudhunagar"),
]

BLOOD_GROUPS = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
]

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    city = models.CharField(max_length=100, choices=TAMIL_NADU_DISTRICTS)
    contact = models.CharField(max_length=15, primary_key=True)
    last_donated = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"
