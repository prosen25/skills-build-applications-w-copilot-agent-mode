from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create Users
        user1 = User.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith')
        user2 = User.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Jones')
        user3 = User.objects.create(username='carol', email='carol@example.com', first_name='Carol', last_name='Lee')

        # Create Teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Create Activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, calories_burned=250, date=timezone.now().date())
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, calories_burned=400, date=timezone.now().date())
        Activity.objects.create(user=user3, activity_type='Swimming', duration=60, calories_burned=500, date=timezone.now().date())

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='30 min run + 15 min cycling', suggested_for='Cardio')
        Workout.objects.create(name='Strength Circuit', description='Pushups, squats, lunges', suggested_for='Strength')

        # Create Leaderboard
        Leaderboard.objects.create(user=user1, score=1200, rank=1)
        Leaderboard.objects.create(user=user2, score=950, rank=2)
        Leaderboard.objects.create(user=user3, score=800, rank=3)

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
