# Generated by Django 5.0.4 on 2024-04-21 12:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "book_id",
                    models.PositiveBigIntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "book_name",
                    models.CharField(db_index=True, max_length=512, unique=True),
                ),
                (
                    "number_of_copies",
                    models.PositiveBigIntegerField(
                        default=0,
                        help_text="Number of available/remaining copies of a book",
                    ),
                ),
            ],
            options={
                "db_table": "books",
            },
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "member_id",
                    models.PositiveBigIntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "member_name",
                    models.CharField(
                        db_index=True,
                        help_text="Member name who checked out a book",
                        max_length=512,
                        unique=True,
                    ),
                ),
            ],
            options={
                "db_table": "members",
            },
        ),
        migrations.CreateModel(
            name="Circulation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[("checkout", "checkout"), ("return", "return")],
                        help_text="Checkout ? Return",
                        max_length=512,
                    ),
                ),
                ("datetime", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "book_id",
                    models.ForeignKey(
                        help_text="The reserved book",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book_reservations.book",
                    ),
                ),
                (
                    "member_id",
                    models.ForeignKey(
                        help_text="The member who reserved the book",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book_reservations.member",
                    ),
                ),
            ],
            options={
                "db_table": "circulations",
            },
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reserved_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("is_fulfilled", models.BooleanField(default=False)),
                (
                    "fulfilled_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "book_id",
                    models.ForeignKey(
                        help_text="The reserved book",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book_reservations.book",
                    ),
                ),
                (
                    "fulfilled_by",
                    models.ForeignKey(
                        help_text="The circulation which fulfilled the book",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book_reservations.circulation",
                    ),
                ),
                (
                    "member_id",
                    models.ForeignKey(
                        help_text="The member who reserved the book",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book_reservations.member",
                    ),
                ),
            ],
            options={
                "db_table": "reservations",
                "unique_together": {("member_id", "book_id")},
            },
        ),
    ]
