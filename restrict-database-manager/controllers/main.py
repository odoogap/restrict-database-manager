# -*- coding: utf-8 -*-
import openerp.addons.web.controllers.main as webmain
from openerp import http
import werkzeug


class RestrictDatabaseManager(webmain.Database):

    # '/web/database/selector', type='http', auth="none"
    @http.route()
    def selector(self, **kw):
        return werkzeug.utils.redirect('/', 303)

    # '/web/database/manager', type='http', auth="none"
    @http.route()
    def manager(self, **kw):
        return werkzeug.utils.redirect('/', 303)

    # '/web/database/create', type='json', auth="none"
    @http.route()
    def create(self, fields):
        return werkzeug.utils.redirect('/', 303)

    # '/web/database/duplicate', type='json', auth="none"
    @http.route()
    def duplicate(self, fields):
        return werkzeug.utils.redirect('/', 303)

    # '/web/database/drop', type='json', auth="none"
    @http.route()
    def drop(self, fields):
        return werkzeug.utils.redirect('/', 303)

    # '/web/database/backup', type='http', auth="none"
    @http.route()
    def backup(self, backup_db, backup_pwd, token):
        return werkzeug.utils.redirect('/', 303)

    # '/web/database/restore', type='http', auth="none"
    @http.route()
    def restore(self, db_file, restore_pwd, new_db, mode):
        return werkzeug.utils.redirect('/', 303)

    # '/web/database/change_password', type='json', auth="none"
    @http.route()
    def change_password(self, fields):
        return werkzeug.utils.redirect('/', 303)
