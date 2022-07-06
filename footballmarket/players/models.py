from django.db import models


class Club(models.Model):
    club_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.club_name}"


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="clubs", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Match(models.Model):
    date = models.DateField()
    teams = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.teams


class Rating(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="ratings", blank=True, null=True)
    rate = models.IntegerField()

    def __str__(self):


