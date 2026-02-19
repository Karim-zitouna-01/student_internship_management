# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    """
    Model representing a student enrolled in the internship program.
    Contains basic student information and relationships to internships.
    """
    _name = 'student.internship.student'
    _description = 'Student'
    _rec_name = 'name'

    # Basic Information
    name = fields.Char(
        string='Student Name',
        required=True,
        help='Full name of the student'
    )
    student_id = fields.Char(
        string='Student ID',
        help='Unique student identification number'
    )
    email = fields.Char(
        string='Email',
        help='Student email address'
    )
    class_name = fields.Char(
        string='Class',
        help='Student class or year (e.g., 3rd Year, Master 1)'
    )

    # Relational Fields
    internship_ids = fields.One2many(
        comodel_name='student.internship.internship',
        inverse_name='student_id',
        string='Internships',
        help='List of internships associated with this student'
    )

    # Computed Fields
    internship_count = fields.Integer(
        string='Internship Count',
        compute='_compute_internship_count',
        help='Total number of internships for this student'
    )

    @api.depends('internship_ids')
    def _compute_internship_count(self):
        """Calculate the total number of internships for each student."""
        for student in self:
            student.internship_count = len(student.internship_ids)
