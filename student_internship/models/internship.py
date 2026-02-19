# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class Internship(models.Model):
    """
    Model representing an internship assignment.
    Links students, companies, and supervisors together with workflow management.
    """
    _name = 'student.internship.internship'
    _description = 'Internship'
    _rec_name = 'student_id'

    # Relational Fields
    student_id = fields.Many2one(
        comodel_name='student.internship.student',
        string='Student',
        required=True,
        help='Student assigned to this internship'
    )
    company_id = fields.Many2one(
        comodel_name='student.internship.company',
        string='Company',
        required=True,
        help='Company hosting the internship'
    )
    supervisor_id = fields.Many2one(
        comodel_name='student.internship.supervisor',
        string='Supervisor',
        required=True,
        help='Academic supervisor overseeing the internship'
    )

    # Date Fields
    start_date = fields.Date(
        string='Start Date',
        help='Date when the internship begins'
    )
    end_date = fields.Date(
        string='End Date',
        help='Date when the internship ends'
    )

    # Computed Fields
    duration = fields.Integer(
        string='Duration (days)',
        compute='_compute_duration',
        store=True,
        help='Automatically calculated duration in days'
    )

    # Workflow Fields
    status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved'),
            ('finished', 'Finished'),
        ],
        string='Status',
        default='draft',
        required=True,
        help='Current status of the internship'
    )

    # Evaluation Fields
    evaluation_score = fields.Float(
        string='Evaluation Score',
        help='Final evaluation score (0-100)'
    )
    evaluation_comment = fields.Text(
        string='Evaluation Comment',
        help='Detailed evaluation comments from the supervisor'
    )

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        """
        Automatically compute the duration in days based on start and end dates.
        Duration is calculated as the difference between end_date and start_date.
        """
        for internship in self:
            if internship.start_date and internship.end_date:
                delta = internship.end_date - internship.start_date
                internship.duration = delta.days
            else:
                internship.duration = 0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """
        Validate that the end date is not before the start date.
        Raises a ValidationError if the constraint is violated.
        """
        for internship in self:
            if internship.start_date and internship.end_date:
                if internship.end_date < internship.start_date:
                    raise ValidationError(
                        'End date cannot be before start date!'
                    )

    # Workflow Action Methods

    def action_submit(self):
        """
        Transition internship from 'draft' to 'submitted' status.
        Called when the student submits their internship proposal.
        """
        for internship in self:
            internship.status = 'submitted'

    def action_approve(self):
        """
        Transition internship from 'submitted' to 'approved' status.
        Called when the supervisor approves the internship.
        """
        for internship in self:
            internship.status = 'approved'

    def action_finish(self):
        """
        Transition internship from 'approved' to 'finished' status.
        Called when the internship is completed.
        """
        for internship in self:
            internship.status = 'finished'
