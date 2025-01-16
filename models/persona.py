# -*- coding: utf-8 -*-

from odoo import models, fields, api


class persona(models.Model):
    _name = 'quintopet.persona' # modulo.modelo
    _description = 'Una persona'

    nombre = fields.Char('Nombre',size=64, required=True, readonly = False)
    dni = fields.Char('DNI',size=9, required=True, readonly = False)
    email = fields.Char('Email',size=64, required=True, readonly = False)
    telefono = fields.Char('Teléfono',size=20, required=True, readonly = False)