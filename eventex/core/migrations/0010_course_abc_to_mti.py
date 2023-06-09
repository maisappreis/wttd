# Generated by Django 4.1.7 on 2023-04-19 13:04
from django.db import migrations


def copy_src_to_dst(Sourse, Destination): # ABC (Abstract) to MTI(Multi Table Inheritance)
    for src in Sourse.objects.all(): # 1
        dst = Destination(
            title=src.title,
            start=src.start,
            description=src.description,
            slots=src.slots
        )
        dst.save() # 2
        dst.speakers.set(src.speakers.all()) # 3
        src.delete() # 4


def forward_course_abc_to_mti(apps, schema_editor):
    """
    Para fazer tabela ir para frente:
    1. Para cada ABC (Abstract), instanciar um MTI(Multi Table Inheritance) com todos os atributos.
    2. Salvar o MTI.
    3. Associar os speakers do ABC no MTI.
    4. Deletar o ABC.
    """
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'), # CourseAbc - Sourse (fonte)
        apps.get_model('core', 'Course') # CourseMti - Destination (destino)
    )


def backward_course_abc_to_mti(apps, schema_editor):
    """
    Para fazer tabela ir para trás:
    """
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'), # CourseAbc - Sourse (fonte)
        apps.get_model('core', 'Course') # CourseMti - Destination (destino)
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_course'),
    ]

    operations = [
        # Código adicionado por mim.
        migrations.RunPython(forward_course_abc_to_mti,
                             backward_course_abc_to_mti)
    ]
