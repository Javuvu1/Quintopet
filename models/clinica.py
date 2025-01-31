from odoo import models, fields, api


class clinica(models.Model):
    _name = 'quintopet.clinica'

    nombreClinica= fields.Char("Nombre de la Clinica", size=30, required=True)
    direccionClinica= fields.Char("Dirección de la Clinica", size=100, required=True)
    telefonoClinica = fields.Integer("Telefono de la clinica", size=15, required=True)
    cp= fields.Integer("Codigo Postal", size=5, required=True)
    
    