# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tratamiento(models.Model):
    _name = 'quintopet.tratamiento' # modulo.modelo
    _description = 'Un tratamiento'
    
    nombreMedicamento = fields.Char("Nombre del Medicamento", size=64, required=True)
    descripcion = fields.Text("Descripción", size=200, required=True)
    patologia = fields.Char("Patología", size=64, required=True)
    inicioTratamiento = fields.Date("Inicio Tratamiento", default=fields.Date.context_today)
    finTratamiento = fields.Date("Fin Tratamiento", default=fields.Date.context_today)
    
    
    
    # Relación Many2many correctamente definida
    #medicamento_ids = fields.Many2many(
    #    "quintopet.medicamento",  # Modelo relacionado
    #    "  ",          # Campo inverso en el modelo relacionado
    #    string="Medicamentos registrados"
    #)