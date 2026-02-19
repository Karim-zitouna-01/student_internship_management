# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Supervisor(models.Model):
    """
    Model representing an academic supervisor who oversees student internships.
    Contains supervisor information and relationships to internships.
    """
    _name = 'student.internship.supervisor'
    _description = 'Supervisor'
    _rec_name = 'name'

    # Basic Information
    name = fields.Char(
        string='Supervisor Name',
        required=True,
        help='Full name of the supervisor'
    )
    email = fields.Char(
        string='Email',
        help='Supervisor email address'
    )
    department = fields.Char(
        string='Department',
        help='Academic department of the supervisor'
    )

    # Relational Fields
    internship_ids = fields.One2many(
        comodel_name='student.internship.internship',
        inverse_name='supervisor_id',
        string='Internships',
        help='List of internships supervised by this person'
    )

    # Computed Fields
    internship_count = fields.Integer(
        string='Internship Count',
        compute='_compute_internship_count',
        help='Total number of internships supervised'
    )

    @api.depends('internship_ids')
    def _compute_internship_count(self):
        """Calculate the total number of internships for each supervisor."""
        for supervisor in self:
            supervisor.internship_count = len(supervisor.internship_ids)
