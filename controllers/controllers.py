# -*- coding: utf-8 -*-
# from odoo import http


# class Quintopet(http.Controller):
#     @http.route('/quintopet/quintopet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quintopet/quintopet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quintopet.listing', {
#             'root': '/quintopet/quintopet',
#             'objects': http.request.env['quintopet.quintopet'].search([]),
#         })

#     @http.route('/quintopet/quintopet/objects/<model("quintopet.quintopet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quintopet.object', {
#             'object': obj
#         })
