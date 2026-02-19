# -*- coding: utf-8 -*-
{
    'name': 'Student Internship Management',
    'version': '17.0.1.0.0',
    'category': 'Education',
    'summary': 'Manage student internships, companies, and supervisors',
    'description': """
        Student Internship Management System
        =====================================
        This module allows universities to manage:
        - Students enrolled in internship programs
        - Partner companies offering internships
        - Academic supervisors
        - Internship assignments and evaluations
        
        Features:
        - Track internship status workflow
        - Automatic duration calculation
        - Evaluation scoring system
    """,
    'author': 'University ERP Project',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/company_views.xml',
        'views/supervisor_views.xml',
        'views/internship_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
