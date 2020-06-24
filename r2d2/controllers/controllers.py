# -*- coding: utf-8 -*-
# from odoo import http


# class R2d2(http.Controller):
#     @http.route('/r2d2/r2d2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/r2d2/r2d2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('r2d2.listing', {
#             'root': '/r2d2/r2d2',
#             'objects': http.request.env['r2d2.r2d2'].search([]),
#         })

#     @http.route('/r2d2/r2d2/objects/<model("r2d2.r2d2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('r2d2.object', {
#             'object': obj
#         })
