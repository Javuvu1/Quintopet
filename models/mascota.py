# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Mascota(models.Model):
    _name = 'quintopet.mascota' # modulo.modelo
    _description = 'Una mascota'
    
    name = fields.Char("Nombre", size=64, required=True)
    sexo = fields.Selection([
        ('macho', 'Macho'), 
        ('hembra', 'Hembra')
        ], 'Sexo', required=True)
    numChip = fields.Integer("Número de chip", size=2, required=True)
    especie = fields.Char("Especie", size=64, required=True)
    edad = fields.Integer("Edad", size=2, required=True)
    color = fields.Char("Color", size=64, required=False)
    peso = fields.Float( 'Peso', size=3, required=True)
    raza = fields.Char( 'Raza', size=64, required=True)
    foto = fields.Binary('Foto', attachment=True)
    
    cliente_id = fields.Many2one(
        'quintopet.cliente',  # Nombre técnico del modelo relacionado
        string='Cliente',     # Etiqueta del campo
        required=False         # Hace que la relación sea obligatoria
    )
    
    cita_ids = fields.One2many(
        'quintopet.cita',  # Nombre técnico del modelo relacionado
        'mascota_id',      # Nombre del campo inverso en el modelo relacionado
        string='Citas'     # Etiqueta del campo
    )