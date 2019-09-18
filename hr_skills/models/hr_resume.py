# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ResumeLine(models.Model):
    _name = 'hr.resume.line'
    _description = "Resumé line of an employee"
    _order = "line_type_id, date_end desc, date_start desc"

    employee_id = fields.Many2one('hr.employee', required=True, ondelete='cascade')
    name = fields.Char(required=True)
    date_start = fields.Date(required=True)
    date_end = fields.Date()
    description = fields.Text(string="Description")
    line_type_id = fields.Many2one('hr.resume.line.type', string="Type")

    # Used to apply specific template on a line
    display_type = fields.Selection([('classic', 'Classic')], string="Display Type", default='classic')

    _sql_constraints = [
        ('date_check', "CHECK ((date_start <= date_end OR date_end = NULL))", "The start date must be anterior to the end date."),
    ]


class ResumeLineType(models.Model):
    _name = 'hr.resume.line.type'
    _description = "Type of a resumé line"
    _order = "sequence"

    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence', default=10)
