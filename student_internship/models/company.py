# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Company(models.Model):
    """
    Model representing a company that offers internship positions.
    Contains company contact information and relationships to internships.
    """
    _name = 'student.internship.company'
    _description = 'Company'
    _rec_name = 'name'

    # Basic Information
    name = fields.Char(
        string='Company Name',
        required=True,
        help='Official name of the company'
    )
    address = fields.Char(
        string='Address',
        help='Physical address of the company'
    )
    email = fields.Char(
        string='Email',
        help='Company contact email'
    )
    phone = fields.Char(
        string='Phone',
        help='Company contact phone number'
    )

    # Relational Fields
    internship_ids = fields.One2many(
        comodel_name='student.internship.internship',
        inverse_name='company_id',
        string='Internships',
        help='List of internships offered by this company'
    )

    # Computed Fields
    internship_count = fields.Integer(
        string='Internship Count',
        compute='_compute_internship_count',
        help='Total number of internships at this company'
    )

    @api.depends('internship_ids')
    def _compute_internship_count(self):
        """Calculate the total number of internships for each company."""
        for company in self:
            company.internship_count = len(company.internship_ids)
