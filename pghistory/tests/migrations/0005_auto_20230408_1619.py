# Generated by Django 3.2.18 on 2023-04-08 16:19
# flake8: noqa

from django.db import migrations, models
import django.db.models.deletion
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pghistory", "0005_events_middlewareevents"),
        ("tests", "0004_auto_20221010_2039"),
    ]

    operations = [
        migrations.CreateModel(
            name="IgnoreAutoFieldsSnapshotModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("my_char_field", models.CharField(max_length=32)),
                ("my_int_field", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="IgnoreAutoFieldsSnapshotModelEvent",
            fields=[
                ("pgh_id", models.AutoField(primary_key=True, serialize=False)),
                ("pgh_created_at", models.DateTimeField(auto_now_add=True)),
                ("pgh_label", models.TextField(help_text="The event label.")),
                ("id", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("my_char_field", models.CharField(max_length=32)),
                ("my_int_field", models.IntegerField()),
                (
                    "pgh_context",
                    models.ForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="pghistory.context",
                    ),
                ),
                (
                    "pgh_obj",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="no_auto_fields_event",
                        to="tests.ignoreautofieldssnapshotmodel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="ignoreautofieldssnapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="ignoreautofieldssnapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."id" IS DISTINCT FROM NEW."id" OR OLD."my_char_field" IS DISTINCT FROM NEW."my_char_field" OR OLD."my_int_field" IS DISTINCT FROM NEW."my_int_field")',
                    func='INSERT INTO "tests_ignoreautofieldssnapshotmodelevent" ("created_at", "id", "my_char_field", "my_int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "updated_at") VALUES (OLD."created_at", OLD."id", OLD."my_char_field", OLD."my_int_field", _pgh_attach_context(), NOW(), \'ignoreautofieldssnapshot\', OLD."id", OLD."updated_at"); RETURN NULL;',
                    hash="ab05b501b515b1532bf15f216646fcebaeebb254",
                    operation="UPDATE",
                    pgid="pgtrigger_ignoreautofieldssnapshot_update_767f2",
                    table="tests_ignoreautofieldssnapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="ignoreautofieldssnapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="ignoreautofieldssnapshot_delete",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_ignoreautofieldssnapshotmodelevent" ("created_at", "id", "my_char_field", "my_int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "updated_at") VALUES (OLD."created_at", OLD."id", OLD."my_char_field", OLD."my_int_field", _pgh_attach_context(), NOW(), \'ignoreautofieldssnapshot\', OLD."id", OLD."updated_at"); RETURN NULL;',
                    hash="d1417f58b12a9a2a895ed6b147f16f8d6af47897",
                    operation="DELETE",
                    pgid="pgtrigger_ignoreautofieldssnapshot_delete_297b6",
                    table="tests_ignoreautofieldssnapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
    ]
