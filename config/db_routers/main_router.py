class MainRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'store':
            return 'store'
        elif model._meta.app_label == 'warehouse':
            return 'warehouse'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'store':
            return 'store'
        elif model._meta.app_label == 'warehouse':
            return 'warehouse'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'store' or obj2._meta.app_label == 'store':
            return True
        elif 'store' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'warehouse' or obj2._meta.app_label == 'warehouse':
            return True
        elif 'warehouse' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'store':
            return db == 'store'
        elif app_label == 'warehouse':
            return db == 'warehouse'
        return None
