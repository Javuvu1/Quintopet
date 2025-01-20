# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Mascota(models.Model):
    _name = 'quintopet.mascota' # modulo.modelo
    _description = 'Una mascota'
    
    nombreMascota = fields.Char("Nombre", size=64, required=True)
    sexo = fields.Selection([
        ('macho', 'Macho'), 
        ('hembra', 'Hembra')
        ], 'Sexo', required=True)
    numChip = fields.Integer("Número de chip", size=2, required=True)
    especie = fields.Char("Especie", size=64, required=True)
    edad = fields.Integer("Edad", size=2, required=True)
    color = fields.Char("Color", size=64, required=True)
    peso = fields.Float( 'Peso', size=3, required=True)
    raza = fields.Char( 'Raza', size=64, required=True)
    foto = fields.Binary('Foto', attachment=True)
    
    cliente_id = fields.Many2one(
        'quintopet.cliente',  # Nombre técnico del modelo relacionado
        string='Cliente',     # Etiqueta del campo
        required=True         # Hace que la relación sea obligatoria
    )
    
    
    
    # Relación Many2one correctamente definida
    #mascotas_ids = fields.Many2one(
    #    "quintopet.mascota",  # Modelo relacionado
    #    "cliente_id",          # Campo inverso en el modelo relacionado
    #    string="Mascotas registradas"
    #)