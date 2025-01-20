# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
    _inherit = "quintopet.persona"
    _name = 'quintopet.cliente' # modulo.modelo
    _description = 'Un cliente'
    
    direccion = fields.Char("Dirección", size=64, required=False)
    tipo = fields.Selection([
        ('particular', 'Particular'),
        ('fundacion', 'Fundación'),
        ('empresa_publica', 'Empresa Pública'),
        ('empresa_privada', 'Empresa Privada')
    ], "Tipo de cliente", default='particular', required=True)
    
    mascota_ids = fields.One2many(
        'quintopet.mascota',  # Nombre técnico del modelo relacionado
        'cliente_id',         # Nombre del campo Many2one en el modelo 'Mascota'
        string='Mascotas'
    )
    
    # Relación One2many correctamente definida
    #mascotas_ids = fields.One2many(
    #    "quintopet.mascotas",  # Modelo relacionado
    #    "cliente_id",          # Campo inverso en el modelo relacionado
    #    string="Mascotas registradas"
    #)