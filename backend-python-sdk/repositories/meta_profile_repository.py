class MetaProfileRepository:
    def __init__(self, meta_collector, profile_collector, meta_validator, profile_validator):
        self.meta_collector = meta_collector
        self.profile_collector = profile_collector
        self.meta_validator = meta_validator
        self.profile_validator = profile_validator
        self.meta_data = None
        self.profile_data = None
        self.init_data()

    def init_data(self):
        # Эта функция вызывается при создании экземпляра класса
        self.meta_data = self.meta_collector.collect_data()
        self.profile_data = self.profile_collector.collect_data()

    def get_meta_map(self) -> dict:
        self.meta_data.set_current_time_stamp()
        self.meta_validator.validate(self.meta_data)
        return self.meta_data.get_data_map()

    def get_profile_map(self) -> dict:
        self.profile_data.set_current_session_id()
        self.profile_validator.validate(self.profile_data)
        return self.profile_data.get_data_map()