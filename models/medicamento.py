# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medicamento(models.Model):
    _name = 'quintopet.medicamento' # modulo.modelo
    _description = 'Un medicamento'
    
    nombreMedicamento = fields.Char("Nombre del Medicamento", size=64, required=True)
    referencia = fields.Char("Referencia", size=32, required=True)
    precio = fields.Float("Precio", (5, 2), required=True)
    prospecto = fields.Binary("Prospecto")
    fechaCaducidad = fields.Date("Fecha de caducidad", default=fields.Date.context_today)